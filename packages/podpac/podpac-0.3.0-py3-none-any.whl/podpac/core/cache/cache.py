"""

"""

from __future__ import division, print_function, absolute_import

import os
from glob import glob
import shutil
from hashlib import md5 as hash_alg
import six

try:
    import cPickle  # Python 2.7
except:
    import _pickle as cPickle

from podpac.core.settings import settings

_cache_types = {'ram','disk','network','all'}

class CacheException(Exception):
    """Summary
    """
    pass

class CacheWildCard(object):

    """Used to represent wildcard matches for inputs to remove operations (`rem`)
    that can match multiple items in the cache.
    """
    
    def __eq__(self, other):
        return True

def validate_inputs(node=None, key=None, coordinates=None, mode=None):
    """Used for validating the type of common cache inputs.
    Will throw an exception if any input is not the correct type.
    `None` is allowed for all inputs
    
    Parameters
    ----------
    node : None, optional
        podpac.core.node.Node
    key : None, optional
        str
    coordinates : None, optional
        podpac.core.coordinates.coordinates.Coordinates
    mode : None, optional
        str
    
    Returns
    -------
    TYPE bool
        Returns true if all specified inputs are of the correct type
    
    Raises
    ------
    CacheException
        Raises exception if any specified input is not of the correct type
    """
    from podpac.core.node import Node
    from podpac.core.coordinates.coordinates import Coordinates
    if not (node is None or isinstance(node, Node) or isinstance(node, CacheWildCard)):
        raise CacheException('`node` should either be an instance of `podpac.core.node.Node` or `None`.')
    if not (key is None or isinstance(key, six.string_types) or isinstance(key, CacheWildCard)):
        raise CacheException('`key` should either be an instance of string or `None`.')
    if not (coordinates is None or isinstance(coordinates, Coordinates) or isinstance(coordinates, CacheWildCard)):
        raise CacheException('`coordinates` should either be an instance of `podpac.core.coordinates.coordinates.Coordinates` or `None`.')
    if not (mode is None or isinstance(mode, six.string_types)):
        raise CacheException('`mode` should either be an instance of string or `None`.')
    return True

class CacheCtrl(object):

    """Objects of this class are used to manage multiple CacheStore objects of different types
    (e.g. RAM, local disk, s3) and serve as the interface to the caching module.
    """
    
    def __init__(self, cache_stores=[]):
        """Initialize a CacheCtrl object with a list of CacheStore objects.
        Care should be taken to provide the cache_stores list in the order that
        they should be interogated. CacheStore objects with faster access times 
        (e.g. RAM) should appear before others (e.g. local disk, or s3).
        
        Parameters
        ----------
        cache_stores : list, optional
            list of CacheStore objects to manage, in the order that they should be interogated.
        """
        self._cache_stores = cache_stores
        self._cache_mode = None

    def _determine_mode(self, mode):
        if mode is None:
            mode = self._cache_mode
            if mode is None:
                mode = 'all'
        return mode

    def put(self, node, data, key, coordinates=None, mode=None, update=False):
        '''Cache data for specified node.
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        data : any
            Data to cache
        key : str
            Cached object key, e.g. 'output'.
        coordinates : Coordinates, optional
            Coordinates for which cached object should be retrieved, for coordinate-dependent data such as evaluation output
        mode : str
            determines what types of the `CacheStore` are affected: 'ram','disk','network','all'. Defaults to `node._cache_mode` or 'all'. Overriden by `self._cache_mode` if `self._cache_mode` is not `None`.
        update : bool
            If True existing data in cache will be updated with `data`, If False, error will be thrown if attempting put something into the cache with the same node, key, coordinates of an existing entry.
        '''
        validate_inputs(node=node, key=key, coordinates=coordinates, mode=mode)
        assert node is not None, "`node` can not be `None`"
        assert key is not None, "`key` can not be `None`"
        assert not isinstance(node, CacheWildCard)
        assert not isinstance(key, CacheWildCard)
        mode = self._determine_mode(mode)
        for c in self._cache_stores:
            if c.cache_modes_matches(set([mode])):
                c.put(node=node, data=data, key=key, coordinates=coordinates, update=update)
        

    def get(self, node, key, coordinates=None, mode=None):
        '''Get cached data for this node.
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        key : str
            Cached object key, e.g. 'output'.
        coordinates : Coordinates, optional
            Coordinates for which cached object should be retrieved, for coordinate-dependent data such as evaluation output
        mode : str
            determines what types of the `CacheStore` are affected: 'ram','disk','network','all'. Defaults to `node._cache_mode` or 'all'. Overriden by `self._cache_mode` if `self._cache_mode` is not `None`.
            
        Returns
        -------
        data : any
            The cached data.
        
        Raises
        -------
        CacheError
            If the data is not in the cache.
        '''
        validate_inputs(node=node, key=key, coordinates=coordinates, mode=mode)
        assert node is not None, "`node` can not be `None`"
        assert key is not None, "`key` can not be `None`"
        assert not isinstance(node, CacheWildCard)
        assert not isinstance(key, CacheWildCard)
        mode = self._determine_mode(mode)
        for c in self._cache_stores:
            if c.cache_modes_matches(set([mode])):
                if c.has(node=node, key=key, coordinates=coordinates):
                    return c.get(node=node, key=key, coordinates=coordinates)
        raise CacheException("Requested data is not in any cache stores.")

    def rem(self, node, key, coordinates=None, mode=None):
        '''Delete cached data for this node.
        
        Parameters
        ----------
        node : Node, str
            node requesting storage. Use `'*'` to match all nodes.
        key : str
            Delete only cached objects with this key. Use `'*'` to match all keys.
        coordinates : Coordinates, str
            Delete only cached objects for these coordinates. Use `'*'` to match all coordinates.
        mode : str
            determines what types of the `CacheStore` are affected: 'ram','disk','network','all'. Defaults to `node._cache_mode` or 'all'. Overriden by `self._cache_mode` if `self._cache_mode` is not `None`.
        '''
        if isinstance(node, six.string_types) and node == '*': 
            node = CacheWildCard()
        if isinstance(coordinates, six.string_types) and coordinates == '*': 
            coordinates = CacheWildCard()
        validate_inputs(node=node, key=key, coordinates=coordinates, mode=mode)
        assert node is not None, "`node` can not be `None`"
        assert key is not None, "`key` can not be `None`"
        if key == '*':
            key = CacheWildCard()
        else:
            key = key.replace('*','_')
        mode = self._determine_mode(mode)
        for c in self._cache_stores:
            if c.cache_modes_matches(set([mode])):
                c.rem(node=node, key=key, coordinates=coordinates)

    def has(self, node, key, coordinates=None, mode=None):
        '''Check for cached data for this node
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        key : str
            Cached object key, e.g. 'output'.
        coordinates: Coordinate, optional
            Coordinates for which cached object should be checked
        mode : str
            determines what types of the `CacheStore` are affected: 'ram','disk','network','all'. Defaults to `node._cache_mode` or 'all'. Overriden by `self._cache_mode` if `self._cache_mode` is not `None`.
        
        Returns
        -------
        has_cache : bool
             True if there as a cached object for this node for the given key and coordinates.
        '''
        validate_inputs(node=node, key=key, coordinates=coordinates, mode=mode)
        assert node is not None, "`node` can not be `None`"
        assert key is not None, "`key` can not be `None`"
        assert not isinstance(node, CacheWildCard)
        assert not isinstance(key, CacheWildCard)
        mode = self._determine_mode(mode)
        for c in self._cache_stores:
            if c.cache_modes_matches(set([mode])):
                if c.has(node=node, key=key, coordinates=coordinates):
                    return True
        return False


class CacheStore(object):

    def get_hash_val(self, obj):
        return hash_alg(obj).hexdigest()

    def hash_node(self, node):
        hashable_repr = 'None' if node is None else node.hash
        return hashable_repr 

    def hash_coordinates(self, coordinates):
        hashable_repr = 'None' if coordinates is None else coordinates.hash
        return hashable_repr 

    def hash_key(self, key):
        #hashable_repr = str(repr(key)).encode('utf-8')
        #return self.get_hash_val(hashable_repr)
        return key

    def put(self, node, data, key, coordinates=None, update=False):
        '''Cache data for specified node.
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        data : any
            Data to cache
        key : str
            Cached object key, e.g. 'output'.
        coordinates : Coordinates, optional
            Coordinates for which cached object should be retrieved, for coordinate-dependent data such as evaluation output
        update : bool
            If True existing data in cache will be updated with `data`, If False, error will be thrown if attempting put something into the cache with the same node, key, coordinates of an existing entry.
        '''
        raise NotImplementedError

    def get(self, node, key, coordinates=None):
        '''Get cached data for this node.
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        key : str
            Cached object key, e.g. 'output'.
        coordinates : Coordinates, optional
            Coordinates for which cached object should be retrieved, for coordinate-dependent data such as evaluation output
            
        Returns
        -------
        data : any
            The cached data.
        
        Raises
        -------
        CacheError
            If the data is not in the cache.
        '''
        raise NotImplementedError

    def rem(self, node=None, key=None, coordinates=None):
        '''Delete cached data for this node.
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        key : str, optional
            Delete only cached objects with this key.
        coordinates : Coordinates
            Delete only cached objects for these coordinates.
        '''
        raise NotImplementedError

    def has(self, node, key, coordinates=None):
        '''Check for cached data for this node
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        key : str
            Cached object key, e.g. 'output'.
        coordinates: Coordinate, optional
            Coordinates for which cached object should be checked
        
        Returns
        -------
        has_cache : bool
             True if there as a cached object for this node for the given key and coordinates.
        '''
        raise NotImplementedError

class CacheListing(object):

    def __init__(self, node, key, coordinates, data=None):
        self._node_def = node.definition
        self.key = key
        self.coordinate_def = None if coordinates is None else coordinates.json
        self.data = data

    @property
    def node_def(self):
        return cPickle.dumps(self._node_def)
    
    def __eq__(self, other):
        return self.node_def == other.node_def and \
               self.key == other.key and \
               self.coordinate_def == other.coordinate_def

class CachePickleContainer(object):

    def __init__(self, listings=[]):
        self.listings = listings

    def save(self, filepath):
        with open(filepath, 'wb') as f:
            cPickle.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, 'rb') as f:
            return cPickle.load(f)

    def put(self, listing):
        self.listings.append(listing)

    def get(self, listing):
        for l in self.listings:
            if l == listing:
                return l
        raise CacheException("Could not find requested listing.")

    def has(self, listing):
        for l in self.listings:
            if l == listing:
                return True
        return False

    def rem(self, listing):
        for i,l in enumerate(self.listings):
            if l == listing:
                self.listings.pop(i)

    @property
    def empty(self):
        if len(self.listings) == 0:
            return True
        return False


class DiskCacheStore(CacheStore):

    def __init__(self, root_cache_dir_path=None, storage_format='pickle'):
        """Initialize a cache that uses a folder on a local disk file system.
        
        Parameters
        ----------
        root_cache_dir_path : None, optional
            Root directory for the files managed by this cache. `None` indicates to use the folder specified in the global podpac settings.
        storage_format : str, optional
            Indicates the file format for storage. Defaults to 'pickle' which is currently the only supported format.
        
        Raises
        ------
        NotImplementedError
            If unsupported `storage_format` is specified
        """
        self._cache_modes = set(['disk','all'])

        # set cache dir
        if root_cache_dir_path is None:
            root_cache_dir_path = settings['CACHE_DIR']
        self._root_dir_path = root_cache_dir_path

        # make directory if it doesn't already exist
        os.makedirs(self._root_dir_path, exist_ok=True)

        # set extension
        if storage_format == 'pickle':
            self._extension = 'pkl'
        else:
            raise NotImplementedError
        self._storage_format = storage_format

    def cache_modes_matches(self, modes):
        """Returns True if this CacheStore matches any caching modes in `modes`
        
        Parameters
        ----------
        modes : List, Set
            collection of cache modes: subset of ['ram','disk','all']
        
        Returns
        -------
        TYPE : bool
            Returns True if this CacheStore matches any specified modes
        """
        if len(self._cache_modes.intersection(modes)) > 0:
            return True
        return False

    def make_cache_dir(self, node):
        """Create subdirectory for caching data for `node`
        
        Parameters
        ----------
        node : podpac.core.node.Node
            Description
        """
        cache_dir = self.cache_dir(node)
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def cache_dir(self, node):
        """subdirectory for caching data for `node`
        
        Parameters
        ----------
        node : podpac.core.node.Node
            Description
        
        Returns
        -------
        TYPE : str
            subdirectory path
        """
        basedir = self._root_dir_path
        subdir = str(node.__class__)[8:-2].split('.')
        dirs = [basedir] + subdir
        return (os.path.join(*dirs)).replace('<', '_').replace('>', '_')

    def cache_filename(self, node, key, coordinates):
        """Filename for storing cached data for specified node,key,coordinates
        
        Parameters
        ----------
        node : podpac.core.node.Node
            Description
        key : str
            Description
        coordinates : podpac.core.coordinates.coordinates.Coordinates
            Description
        
        Returns
        -------
        TYPE : str
            filename (but not containing directory)
        """
        pre = self.cleanse_filename_str(str(node.base_ref))
        self.cleanse_filename_str(pre)
        nKeY = 'nKeY{}'.format(self.hash_node(node))
        kKeY = 'kKeY{}'.format(self.hash_key(key))
        cKeY = 'cKeY{}'.format(self.hash_coordinates(coordinates))
        filename = '_'.join([pre, nKeY, kKeY, cKeY])
        filename = filename + '.' + self._extension
        return filename

    def cache_glob(self, node, key, coordinates):
        """Fileglob to match files that could be storing cached data for specified node,key,coordinates
        
        Parameters
        ----------
        node : podpac.core.node.Node
        key : str, CacheWildCard
            CacheWildCard indicates to match any key
        coordinates : podpac.core.coordinates.coordinates.Coordinates, CacheWildCard, None
            CacheWildCard indicates to match any coordinates
        
        Returns
        -------
        TYPE : str
            Fileglob of existing paths that match the request
        """
        pre = '*'
        nKeY = 'nKeY{}'.format(self.hash_node(node))
        kKeY = 'kKeY*' if isinstance(key, CacheWildCard) else 'kKeY{}'.format(self.cleanse_filename_str(self.hash_key(key)))
        cKeY = 'cKeY*' if isinstance(coordinates, CacheWildCard) else 'cKeY{}'.format(self.hash_coordinates(coordinates))
        filename = '_'.join([pre, nKeY, kKeY, cKeY])
        filename = filename + '.' + self._extension
        return os.path.join(self.cache_dir(node), filename)

    def cache_path(self, node, key, coordinates):
        """Filepath for storing cached data for specified node,key,coordinates
        
        Parameters
        ----------
        node : podpac.core.node.Node
            Description
        key : str
            Description
        coordinates : podpac.core.coordinates.coordinates.Coordinates
            Description
        
        Returns
        -------
        TYPE : str
            filename (including containing directory)
        """
        return os.path.join(self.cache_dir(node), self.cache_filename(node, key, coordinates))

    def cleanse_filename_str(self, s):
        """Remove/replace characters from string `s` that could could interfere with proper functioning of cache if used to construct cache filenames.
        
        Parameters
        ----------
        s : str
            Description
        
        Returns
        -------
        TYPE : str
            Description
        """
        s = s.replace('/', '_').replace('\\', '_').replace(':', '_').replace('<', '_').replace('>', '_')
        s = s.replace('nKeY', 'xxxx').replace('kKeY', 'xxxx').replace('cKeY', 'xxxx')
        return s

    def put(self, node, data, key, coordinates=None, update=False):
        '''Cache data for specified node.
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        data : any
            Data to cache
        key : str
            Cached object key, e.g. 'output'.
        coordinates : Coordinates, optional
            Coordinates for which cached object should be retrieved, for coordinate-dependent data such as evaluation output
        update : bool
            If True existing data in cache will be updated with `data`, If False, error will be thrown if attempting put something into the cache with the same node, key, coordinates of an existing entry.
        '''
        self.make_cache_dir(node)
        listing = CacheListing(node=node, key=key, coordinates=coordinates, data=data)
        if self.has(node, key, coordinates): # a little inefficient but will do for now
            if not update:
                raise CacheException("Existing cache entry. Call put() with `update` argument set to True if you wish to overwrite.")
            else:
                paths = glob(self.cache_glob(node, key, coordinates))
                for p in paths:
                    c = CachePickleContainer.load(p)
                    if c.has(listing):
                        c.rem(listing)
                        c.put(listing)
                        c.save(p)
                        return True
                raise CacheException("Data is cached, but unable to find for update.")
        # listing does not exist in cache
        path = self.cache_path(node, key, coordinates)
        # if file for listing already exists, listing needs to be added to file
        if os.path.exists(path):
            c = CachePickleContainer.load(path)
            c.put(listing)
            c.save(path)
        # if file for listing does not already exist, we need to create a new container, add the listing, and save to file
        else:
            CachePickleContainer(listings=[listing]).save(path)
        return True

    def get(self, node, key, coordinates=None):
        '''Get cached data for this node.
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        key : str
            Cached object key, e.g. 'output'.
        coordinates : Coordinates, optional
            Coordinates for which cached object should be retrieved, for coordinate-dependent data such as evaluation output
            
        Returns
        -------
        data : any
            The cached data.
        
        Raises
        -------
        CacheError
            If the data is not in the cache.
        '''
        listing = CacheListing(node=node, key=key, coordinates=coordinates)
        paths = glob(self.cache_glob(node, key, coordinates))
        for p in paths:
            c = CachePickleContainer.load(p)
            if c.has(listing):
                data = c.get(listing).data
                if data is None:
                    CacheException("Stored data is None.")
                return data
        raise CacheException("Cache miss. Requested data not found.")

    def rem(self, node=CacheWildCard(), key=CacheWildCard(), coordinates=CacheWildCard()):
        '''Delete cached data for this node.
        
        Parameters
        ------------
        node : Node, CacheWildCard
            node requesting storage. If `node` is a `CacheWildCard` then everything in the cache will be deleted.
        key : str, CacheWildCard, optional
            Delete only cached objects with this key, or any key if `key` is a CacheWildCard.
        coordinates : Coordinates, CacheWildCard, None, optional
            Delete only cached objects for these coordinates, or any coordinates if `coordinates` is a CacheWildCard. `None` specifically indicates entries that do not have coordinates.
        '''
        if isinstance(node, CacheWildCard):
            # clear the entire cache store
            shutil.rmtree(self._root_dir_path)
            return True
        removed_something = False
        if isinstance(key, CacheWildCard) or isinstance(coordinates, CacheWildCard):
            # clear all files for data cached for `node`
            # and delete its cache subdirectory if it is empty
            paths = glob(self.cache_glob(node, key=key, coordinates=coordinates))
            for p in paths:
                os.remove(p)
                removed_something = True
            cache_dir = self.cache_dir(node=node)
            if os.path.exists(cache_dir) and os.path.isdir(cache_dir) and not os.listdir(cache_dir):
                os.rmdir(cache_dir)
            return removed_something
        listing = CacheListing(node=node, key=key, coordinates=coordinates)
        paths = glob(self.cache_glob(node, key, coordinates))
        for p in paths:
            c = CachePickleContainer.load(p)
            if c.has(listing):
                c.rem(listing)
                removed_something = True
                if c.empty:
                    os.remove(p)
                else:
                    c.save(p)
        return removed_something
        

    def has(self, node, key, coordinates=None):
        '''Check for cached data for this node
        
        Parameters
        ------------
        node : Node
            node requesting storage.
        key : str
            Cached object key, e.g. 'output'.
        coordinates: Coordinate, optional
            Coordinates for which cached object should be checked
        
        Returns
        -------
        has_cache : bool
             True if there as a cached object for this node for the given key and coordinates.
        '''
        listing = CacheListing(node=node, key=key, coordinates=coordinates)
        paths = glob(self.cache_glob(node, key, coordinates))
        for p in paths:
            c = CachePickleContainer.load(p)
            if c.has(listing):
                return True
        return False


