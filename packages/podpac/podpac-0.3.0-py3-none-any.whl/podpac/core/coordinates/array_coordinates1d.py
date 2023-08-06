"""
One-Dimensional Coordinates: Array
"""


from __future__ import division, unicode_literals, print_function, absolute_import

import copy
from collections import OrderedDict

import numpy as np
import traitlets as tl
from collections import OrderedDict

from podpac.core.utils import ArrayTrait
from podpac.core.units import Units
from podpac.core.coordinates.utils import make_coord_value, make_coord_array
from podpac.core.coordinates.coordinates1d import Coordinates1d

class ArrayCoordinates1d(Coordinates1d):
    """
    1-dimensional array of coordinates.

    ArrayCoordinates1d is a basic array of 1d coordinates created from an array of coordinate values. Numerical
    coordinates values are converted to ``float``, and time coordinate values are converted to numpy ``datetime64``.
    For convenience, podpac automatically converts datetime strings such as ``'2018-01-01'`` to ``datetime64``. The
    coordinate values must all be of the same type.

    Parameters
    ----------
    name : str
        Dimension name, one of 'lat', 'lon', 'time', or 'alt'.
    coordinates : array, read-only
        Full array of coordinate values.
    units : podpac.Units
        Coordinate units.
    coord_ref_sys : str
        Coordinate reference system.
    ctype : str
        Coordinates type: 'point', 'left', 'right', or 'midpoint'.
    segment_lengths : array, float, timedelta
        When ctype is a segment type, the segment lengths for the coordinates.

    See Also
    --------
    :class:`Coordinates1d`, :class:`UniformCoordinates1d`
    """

    coords = ArrayTrait(ndim=1, read_only=True)
    coords.__doc__ = ":array: User-defined coordinate values"

    def __init__(self, coords,
                       name=None, ctype=None, units=None, segment_lengths=None, coord_ref_sys=None):
        """
        Create 1d coordinates from an array.

        Arguments
        ---------
        coords : array-like
            coordinate values.
        name : str, optional
            Dimension name, one of 'lat', 'lon', 'time', or 'alt'.
        units : Units, optional
            Coordinate units.
        coord_ref_sys : str, optional
            Coordinate reference system.
        ctype : str, optional
            Coordinates type: 'point', 'left', 'right', or 'midpoint'.
        segment_lengths : array, optional
            When ctype is a segment type, the segment lengths for the coordinates. The segment_lengths are required
            for nonmonotonic coordinates. The segment can be inferred from coordinate values for monotonic coordinates.
        """

        # validate and set coords
        self.set_trait('coords', make_coord_array(coords))

        # precalculate once
        if self.coords.size == 0:
            self._is_monotonic = None
            self._is_descending = None
            self._is_uniform = None

        elif self.coords.size == 1:
            self._is_monotonic = True
            self._is_descending = None
            self._is_uniform = True

        else:
            deltas = (self.coords[1:] - self.coords[:-1]).astype(float) * (self.coords[1] - self.coords[0]).astype(float)
            if np.any(deltas <= 0):
                self._is_monotonic = False
                self._is_descending = None
                self._is_uniform = False
            else:
                self._is_monotonic = True
                self._is_descending = self.coords[1] < self.coords[0]
                self._is_uniform = np.allclose(deltas, deltas[0])
        
        # set common properties
        super(ArrayCoordinates1d, self).__init__(
            name=name, ctype=ctype, units=units, segment_lengths=segment_lengths, coord_ref_sys=coord_ref_sys)

        # check segment lengths
        if segment_lengths is None:
            if self.ctype == 'point' or self.size == 0:
                self.set_trait('segment_lengths', None)
            elif self.dtype == np.datetime64:
                raise TypeError("segment_lengths required for datetime coordinates (if ctype != 'point')")
            elif self.size == 1:
                raise TypeError("segment_lengths required for coordinates of size 1 (if ctype != 'point')")
            elif not self.is_monotonic:
                raise TypeError("segment_lengths required for nonmonotonic coordinates (if ctype != 'point')")

    @tl.default('ctype')
    def _default_ctype(self):
        if self.size == 0 or self.size == 1 or not self.is_monotonic or self.dtype == np.datetime64:
            return 'point'
        else:
            return 'midpoint'

    @tl.default('segment_lengths')
    def _default_segment_lengths(self):
        if self.is_uniform:
            return np.abs(self.coords[1] - self.coords[0])

        deltas = np.abs(self.coords[1:] - self.coords[:-1])
        if self.is_descending:
            deltas = deltas[::-1]

        segment_lengths = np.zeros(self.coords.size)
        if self.ctype == 'left':
            segment_lengths[:-1] = deltas
            segment_lengths[-1] = segment_lengths[-2]
        elif self.ctype == 'right':
            segment_lengths[1:] = deltas
            segment_lengths[0] = segment_lengths[1]
        elif self.ctype == 'midpoint':
            segment_lengths[:-1] = deltas
            segment_lengths[1:] += deltas
            segment_lengths[1:-1] /= 2

        if self.is_descending:
            segment_lengths = segment_lengths[::-1]
        
        segment_lengths.setflags(write=False)
        return segment_lengths

    def __eq__(self, other):
        if not super(ArrayCoordinates1d, self).__eq__(other):
            return False

        if not np.array_equal(self.coordinates, other.coordinates):
            return False

        return True

    # ------------------------------------------------------------------------------------------------------------------
    # Alternate Constructors
    # ------------------------------------------------------------------------------------------------------------------

    @classmethod
    def from_xarray(cls, x, **kwargs):
        """
        Create 1d Coordinates from named xarray coords.

        Arguments
        ---------
        x : xarray.DataArray
            Nade DataArray of the coordinate values
        units : Units, optional
            Coordinate units.
        coord_ref_sys : str, optional
            Coordinate reference system.
        ctype : str, optional
            Coordinates type: 'point', 'left', 'right', or 'midpoint'.
        segment_lengths : (low, high), optional
            When ctype is a segment type, the segment lengths for the coordinates. The segment_lengths are required
            for nonmonotonic coordinates. The segment can be inferred from coordinate values for monotonic coordinates.

        Returns
        -------
        :class:`ArrayCoordinates1d`
            1d coordinates
        """

        return cls(x.data, name=x.name, **kwargs)

    @classmethod
    def from_definition(cls, d):
        """
        Create 1d coordinates from a coordinates definition.

        The definition must contain the coordinate values::

            c = ArrayCoordinates1d.from_definition({
                "values": [0, 1, 2, 3]
            })

        The definition may also contain any of the 1d Coordinates properties::

            c = ArrayCoordinates1d.from_definition({
                "values": [0, 1, 2, 3],
                "name": "lat",
                "ctype": "points"
            })

        Arguments
        ---------
        d : dict
            1d coordinates array definition

        Returns
        -------
        :class:`ArrayCoordinates1d`
            1d Coordinates

        See Also
        --------
        definition
        """

        if 'values' not in d:
            raise ValueError('ArrayCoordinates1d definition requires "values" property')

        coords = d.pop('values')
        return cls(coords, **d)

    def copy(self):
        """
        Make a deep copy of the 1d Coordinates array.

        Returns
        -------
        :class:`ArrayCoordinates1d`
            Copy of the coordinates.
        """

        kwargs = self.properties
        if self._segment_lengths:
            kwargs['segment_lengths'] = self.segment_lengths
        return ArrayCoordinates1d(self.coords, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------
    # standard methods, array-like
    # ------------------------------------------------------------------------------------------------------------------

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        coords = self.coords[index]
        kwargs = self.properties
        
        if self.ctype != 'point':
            if isinstance(self.segment_lengths, np.ndarray):
                kwargs['segment_lengths'] = self.segment_lengths[index]
            else:
                kwargs['segment_lengths'] = self.segment_lengths
            
            if (coords.size == 0 or coords.size == 1) and 'ctype' not in self.properties:
                kwargs['ctype'] = self.ctype

        return ArrayCoordinates1d(coords, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def coordinates(self):
        """:array, read-only: Coordinate values."""

        # get coordinates and ensure read-only array with correct dtype
        coordinates = self.coords.copy()
        coordinates.setflags(write=False)
        return coordinates

    @property
    def size(self):
        """ Number of coordinates. """
        return self.coords.size

    @property
    def dtype(self):
        """:type: Coordinates dtype.

        ``float`` for numerical coordinates and numpy ``datetime64`` for datetime coordinates.
        """

        if self.size == 0:
            return None
        elif self.coords.dtype == float:
            return float
        elif np.issubdtype(self.coords.dtype, np.datetime64):
            return np.datetime64

    @property
    def is_monotonic(self):
        return self._is_monotonic

    @property
    def is_descending(self):
        return self._is_descending

    @property
    def is_uniform(self):
        return self._is_uniform

    @property
    def bounds(self):
        """ Low and high coordinate bounds. """

        # TODO are we sure this can't be a tuple?

        if self.size == 0:
            lo, hi = np.nan, np.nan
        elif self.is_monotonic:
            lo, hi = sorted([self.coords[0], self.coords[-1]])
        elif self.dtype is np.datetime64:
            lo, hi = np.min(self.coords), np.max(self.coords)
        else:
            lo, hi = np.nanmin(self.coords), np.nanmax(self.coords)

        # read-only array with the correct dtype
        bounds = np.array([lo, hi], dtype=self.dtype)
        bounds.setflags(write=False)
        return bounds

    @property
    def argbounds(self):
        if not self.is_monotonic:
            return np.argmin(self.coords), np.argmax(self.coords)
        elif not self.is_descending:
            return 0, -1
        else:
            return -1, 0

    @property
    def definition(self):
        """:dict: Serializable 1d coordinates array definition.

        The ``definition`` can be used to create new ArrayCoordinates1d::

            c = podpac.ArrayCoordinates1d([0, 1, 2, 3])
            c2 = podpac.ArrayCoordinates1d.from_definition(c.definition)

        See Also
        --------
        from_definition
        """

        d = OrderedDict()
        d['values'] = self.coords
        if self._segment_lengths:
            d['segment_lengths'] = self.segment_lengths
        d.update(self.properties)
        return d

    # ------------------------------------------------------------------------------------------------------------------
    # Methods
    # ------------------------------------------------------------------------------------------------------------------

    def select(self, bounds, outer=False, return_indices=False):
        """
        Get the coordinate values that are within the given bounds.

        The default selection returns coordinates that are within the other coordinates bounds::

            In [1]: c = ArrayCoordinates1d([0, 1, 2, 3], name='lat')

            In [2]: c.select([1.5, 2.5]).coordinates
            Out[2]: array([2.])

        The *outer* selection returns the minimal set of coordinates that contain the other coordinates::
        
            In [3]: c.intersect([1.5, 2.5], outer=True).coordinates
            Out[3]: array([1., 2., 3.])

        The *outer* selection also returns a boundary coordinate if the other coordinates are outside this
        coordinates bounds but *inside* its area bounds::
        
            In [4]: c.intersect([3.25, 3.35], outer=True).coordinates
            Out[4]: array([3.0], dtype=float64)

            In [5]: c.intersect([10.0, 11.0], outer=True).coordinates
            Out[5]: array([], dtype=float64)
        
        Arguments
        ---------
        bounds : low, high
            selection bounds
        outer : bool, optional
            If True, do an *outer* selection. Default False.
        return_indices : bool, optional
            If True, return slice or indices for the selection in addition to coordinates. Default False.

        Returns
        -------
        selection : :class:`ArrayCoordinates1d`
            ArrayCoordinates1d object with coordinates within the other coordinates bounds.
        I : slice or list
            index or slice for the intersected coordinates (only if return_indices=True)
        """

        bounds = make_coord_value(bounds[0]), make_coord_value(bounds[1])

        # empty
        if self.size == 0:
            return self._select_empty(return_indices)

        # full
        if self.bounds[0] >= bounds[0] and self.bounds[1] <= bounds[1]:
            return self._select_full(return_indices)

        # none
        if self.area_bounds[0] > bounds[1] or self.area_bounds[1] < bounds[0]:
            return self._select_empty(return_indices)

        if not outer:
            gt = self.coordinates >= bounds[0]
            lt = self.coordinates <= bounds[1]
            I = np.where(gt & lt)[0]

        elif self.is_monotonic:
            gt = np.where(self.coords >= bounds[0])[0]
            lt = np.where(self.coords <= bounds[1])[0]
            lo, hi = bounds[0], bounds[1]
            if self.is_descending:
                lt, gt = gt, lt
                lo, hi = hi, lo
            if self.coords[gt[0]] != lo:
                gt[0] -= 1
            if self.coords[lt[-1]] != hi:
                lt[-1] += 1
            start = max(0, gt[0])
            stop = min(self.size-1, lt[-1])
            I = slice(start, stop+1)

        else:
            try:
                gt = self.coords >= max(self.coords[self.coords <= bounds[0]])
            except ValueError as e:
                gt = self.coords >= -np.inf
            try:
                lt = self.coords <= min(self.coords[self.coords >= bounds[1]])
            except ValueError as e:
                lt = self.coords <= np.inf
            I = np.where(gt & lt)[0]

        if return_indices:
            return self[I], I
        else:
            return self[I]
