# -*- coding: utf-8 -*-
"""This module implements masking features to define which entries of
|Parameter| or |Sequence| arrays are relevant and which are not."""
# import...
# ...from standard library
import inspect
# ...from site-packages
import numpy
# ...from HydPy
from hydpy import pub
from hydpy.core import abctools
from hydpy.core import autodoctools
from hydpy.core import metatools
from hydpy.core import objecttools


class _MaskDescriptor(object):

    def __init__(self, cls_mask):
        self.cls_mask = cls_mask

    def __get__(self, obj, type_=None):
        if obj is None:
            return self
        return self.cls_mask(obj)


class _BaseMask(numpy.ndarray):

    def __new__(cls, array=None, **kwargs):
        return cls.array2mask(array)

    @classmethod
    def array2mask(cls, array=None):
        """Create a new mask object based on the given |numpy.ndarray|
        and return it."""
        if array is None:
            return numpy.ndarray.__new__(cls, 0, dtype=bool)
        return numpy.asarray(array, dtype=bool).view(cls)

    def __call__(self):
        raise NotImplementedError()

    def __contains__(self, other):
        return numpy.all(self()[other])

    def __repr__(self):
        return numpy.ndarray.__repr__(self).replace(', dtype=bool', '')


abctools.MaskABC.register(_BaseMask)


class CustomMask(_BaseMask):
    """Mask that awaits all |bool| values to be set manually.

    Class |CustomMask| is the most basic applicable mask and provides
    no special features, excepts that it allows its |bool| values
    to be defined manually.  Use it when you require a masking behaviour
    that is not captured by an available mask.

    Like the more advanced masks, |CustomMask| can either work via
    Python's descriptor protocoll or can be applied directly, but is
    thought to be applied in the last way only:

    >>> from hydpy.core.variabletools import Variable
    >>> from hydpy.core.masktools import CustomMask
    >>> mask1 = CustomMask([[True, False, False],
    ...                     [True, False, False]])

    Note that calling any mask object (not only those of type |CustomMask|)
    returns a new mask, but does not change the old one (all masks are
    derived from |numpy.ndarray|):

    >>> mask2 = mask1([[False, True, False],
    ...                [False, True, False]])
    >>> mask1
    CustomMask([[ True, False, False],
                [ True, False, False]])
    >>> mask2
    CustomMask([[False,  True, False],
                [False,  True, False]])

    All features of class |numpy.ndarray| thought for |bool| values
    can be applied.  Some useful examples:

    >>> mask3 = mask1 + mask2
    >>> mask3
    CustomMask([[ True,  True, False],
                [ True,  True, False]])
    >>> mask3 ^ mask1
    CustomMask([[False,  True, False],
                [False,  True, False]])
    >>> ~mask3
    CustomMask([[False, False,  True],
                [False, False,  True]])
    >>> mask1 & mask2
    CustomMask([[False, False, False],
                [False, False, False]])
    """

    def __call__(self, bools):
        return type(self)(bools)


class DefaultMask(_BaseMask):
    """A mask with all entries being |True| of the same shape as
    its master |Variable| object.

    See the documentation on class |CustomMask| for the basic usage
    of class |DefaultMask|.

    The following example shows how |DefaultMask| can be applied via
    Python's descriptor protocoll, which should be the common situation:

    >>> from hydpy.core.variabletools import Variable
    >>> from hydpy.core.masktools import DefaultMask
    >>> class Var1(Variable):
    ...     shape = (2, 3)
    >>> var1 = Var1()
    >>> mask = DefaultMask(var1)
    >>> mask
    DefaultMask([[ True,  True,  True],
                 [ True,  True,  True]])
    """

    def __new__(cls, variable=None, **kwargs):
        if variable is None:
            return _MaskDescriptor(cls)
        self = cls.new(variable, **kwargs)
        self.variable = variable
        return self

    def __call__(self, **kwargs):
        return type(self)(self.variable, **kwargs)

    @classmethod
    def new(cls, variable, **kwargs):
        """Return a new |DefaultMask| object associated with the
        given |Variable| object."""
        return cls.array2mask(numpy.full(variable.shape, True))


class IndexMask(DefaultMask):
    """A mask depending on a referenced index parameter containing integers.

    |IndexMask| must subclassed.  See the masks |hland_masks.Complete|
    and |hland_masks.Soil| of base model |hland| for two concrete example
    classes, which are applied on the |hland| specific parameter classes
    |hland_parameters.ParameterComplete| and |hland_parameters.ParameterSoil|.
    The documentation on the two parameter classes provides some application
    examples.  Further, see the documentation on class |CustomMask| for the
    basic usage of class |DefaultMask|.
    """
    RELEVANT_VALUES = ()

    @classmethod
    def new(cls, variable):
        """Return a new |IndexMask| object of the same shape as the
        parameter referenced by |property| |IndexMask.refindices|.
        Entries are only |True|, if the integer values of the
        respective entries of the referenced parameter are contained
        in the |IndexMask| class attribute tuple `RELEVANT_VALUES`.
        """
        indices = cls.get_refindices(variable)
        if numpy.min(indices) < 1:
            raise RuntimeError(
                'The mask of parameter %s cannot be determined, as '
                'long as parameter `%s` is not prepared properly.'
                % (objecttools.elementphrase(variable), indices.name))
        mask = numpy.full(indices.shape, False, dtype=bool)
        refvalues = indices.values
        for relvalue in cls.RELEVANT_VALUES:
            mask[refvalues == relvalue] = True
        return cls.array2mask(mask)

    @classmethod
    def get_refindices(cls, variable):
        """Return the |MultiParameter| object for determining which
        entries of |IndexMask| are |True| and which are |False|.

        The given `variable` must be concrete |Variable| object, the
        |IndexMask| is thought for.

        Needs to be overwritten by subclasses:

        >>> from hydpy.core.variabletools import Variable
        >>> from hydpy.core.masktools import IndexMask
        >>> class Var(Variable):
        ...     mask = IndexMask()
        >>> Var().mask
        Traceback (most recent call last):
        ...
        NotImplementedError: Function `get_refindices` of class `IndexMask` \
must be overridden, which is not the case for class `IndexMask`.
        """
        raise NotImplementedError(
            'Function `get_refindices` of class `IndexMask` must be '
            'overridden, which is not the case for class `%s`.'
            % objecttools.classname(cls))

    @property
    def refindices(self):
        """|MultiParameter| object for determining which entries of
        |IndexMask| are |True| and which are |False|."""
        return self.get_refindices(self.variable)


class Masks(metatools.MetaSubgroupClass):
    """Base class for handling groups of masks.

    Attributes:
      * model: The parent |Model| object.

    |Masks| subclasses are basically just containers, who are defined
    similar as |SubParameters| and |SubSequences| subclasses:

    >>> from hydpy.core.masktools import Masks
    >>> from hydpy.core.masktools import IndexMask, DefaultMask, CustomMask
    >>> class Masks(Masks):
    ...     CLASSES = (IndexMask,
    ...                DefaultMask)
    >>> masks = Masks(None)

    The contained mask classes are available via attribute access in
    lower case letters:

    >>> masks
    indexmask of module hydpy.core.masktools
    defaultmask of module hydpy.core.masktools
    >>> masks.indexmask is IndexMask
    True

    The `in` operator is supported:

    >>> IndexMask in masks
    True
    >>> CustomMask in masks
    False
    >>> 'mask' in masks
    Traceback (most recent call last):
    ...
    TypeError: The given value `mask` of type `str` is neither a Mask \
class nor a Mask instance.

    Using item access, strings (in whatever case), mask classes, and
    mask objects are accepted:

    >>> masks['IndexMask'] is IndexMask
    True
    >>> masks['indexmask'] is IndexMask
    True
    >>> masks[IndexMask] is IndexMask
    True
    >>> masks[CustomMask()]
    Traceback (most recent call last):
    ...
    RuntimeError: While trying to retrieve a mask based on key \
`CustomMask([])`, the following error occurred: The key does not \
define an available mask.
    >>> masks['test']
    Traceback (most recent call last):
    ...
    RuntimeError: While trying to retrieve a mask based on key `'test'`, \
the following error occurred: The key does not define an available mask.
    >>> masks[1]
    Traceback (most recent call last):
    ...
    TypeError: While trying to retrieve a mask based on key `1`, the \
following error occurred: The given key is neither a `string` a `mask` type.
    """
    CLASSES = ()

    def __init__(self, model):
        self.model = model
        for cls in self.CLASSES:
            setattr(self, objecttools.instancename(cls), cls)

    @property
    def name(self):
        """`masks`"""
        return 'masks'

    def __iter__(self):
        for cls in self.CLASSES:
            name = objecttools.instancename(cls)
            yield getattr(self, name)

    def __contains__(self, mask):
        if isinstance(mask, abctools.MaskABC):
            mask = type(mask)
        if mask in self.CLASSES:
            return True
        try:
            if issubclass(mask, abctools.MaskABC):
                return False
        except TypeError:
            pass
        raise TypeError(
            'The given %s is neither a Mask class nor a Mask instance.'
            % objecttools.value_of_type(mask))

    def __getitem__(self, key):
        _key = key
        try:
            if inspect.isclass(key):
                if issubclass(key, abctools.MaskABC):
                    key = objecttools.instancename(key)
            elif isinstance(key, abctools.MaskABC):
                if key in self:
                    return key
                raise RuntimeError(
                    'The key does not define an available mask.')
            if isinstance(key, str):
                try:
                    return getattr(self, key.lower())
                except AttributeError:
                    raise RuntimeError(
                        'The key does not define an available mask.')
            raise TypeError(
                'The given key is neither a `string` a `mask` type.')
        except BaseException:
            objecttools.augment_excmessage(
                'While trying to retrieve a mask based on key `%s`'
                % repr(_key))

    def __repr__(self):
        lines = []
        if pub.options.reprcomments:
            lines.append('# %s object defined in module %s.'
                         % (objecttools.classname(self),
                            objecttools.modulename(self)))
            lines.append('# The implemented masks are:')
        for mask in self:
            lines.append('%s of module %s'
                         % (objecttools.instancename(mask), mask.__module__))
        return '\n'.join(lines)

    def __dir__(self):
        return objecttools.dir_(self)


autodoctools.autodoc_module()
