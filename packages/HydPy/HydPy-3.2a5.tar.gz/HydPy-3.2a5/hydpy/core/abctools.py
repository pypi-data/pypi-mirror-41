# -*- coding: utf-8 -*-
"""This module provides some abstract base classes.

There are some type checks within the HydPy framework relying on the
build in  function |isinstance|.  In order to keep HydPy "pythonic",
the following abstract base classes are defined.  All calls to |isinstance|
should rely these abstract base classes instead of the respective
original classes.  This helps to build e.g. a new parameter class when
one wants to avoid to inherit from |Parameter|.

At the moment, the provided classes do not provide things like abstract
methods (should be added later).  Just use them to register new classes
that are not actual subclasses of the respective HydPy classes, but
should be handled as if they were.  See class |anntools.ANN| as an example.
"""
# import...
# ...from standard library
from typing import Any, Union
import abc
import datetime
# ...from site-packages
import numpy
# ...from HydPy
from hydpy.core import autodoctools


class DocABC(object, metaclass=abc.ABCMeta):
    """ABC base class automatically documenting is registered subclasses."""

    _registry_empty = True

    @classmethod
    def register(cls, subclass):
        """Add information to the documentation of the given abstract base
        class and register the subclass afterwards.

        Subclass the new abstract base class `NewABC` and define some new
        concrete classes (`New1`, `New2`, `New3`) which do not inherit
        from `NewABC`:

        >>> from hydpy.core.abctools import DocABC
        >>> class NewABC(DocABC):
        ...    "A new base class."
        >>> class New1(object):
        ...     "First new class"
        >>> class New2(object):
        ...     "Second new class"
        >>> class New3(object):
        ...     "Third new class"

        The docstring `NewABC` is still the same as defined above:

        >>> print(NewABC.__doc__)
        A new base class.

        Now we register the concrete classes `New1` and `New2`:

        >>> NewABC.register(New2)
        >>> NewABC.register(New1)
        >>> NewABC.register(New2)

        Now the docstring of `NewABC` includes the information about
        the concrete classes already registered:

        >>> print(NewABC.__doc__)
        A new base class.
        <BLANKLINE>
        At the moment, the following classes are registered:
             * :class:`~hydpy.core.abctools.New2`
             * :class:`~hydpy.core.abctools.New1`

        Note that the docstring order is the registration order.
        Also note that the "accidental reregistration" of class
        `New2` does not modify the docstring.

        Now the concrete classes `New1` and `New2` are handled as
        if they were actual subclasses of `NewABC`, but class `New3`
        -- which had not been registered -- is not:

        >>> issubclass(New1, NewABC)
        True
        >>> isinstance(New1(), NewABC)
        True
        >>> issubclass(New2, NewABC)
        True
        >>> isinstance(New2(), NewABC)
        True
        >>> issubclass(New3, NewABC)
        False
        >>> isinstance(New3(), NewABC)
        False
        """
        if cls._registry_empty:
            cls._registry_empty = False
            cls.__doc__ += \
                '\n\nAt the moment, the following classes are registered:'
        if not issubclass(subclass, cls):
            cls.__doc__ += ('\n     * :class:`~%s`'
                            % str(subclass).split("'")[1])
            abc.ABCMeta.register(cls, subclass)


class IterableNonStringABC(object, metaclass=abc.ABCMeta):
    """Abstract base class for checking if an object is iterable but not a
    string."""

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is IterableNonStringABC:
            return (hasattr(subclass, '__iter__') and
                    not (isinstance(subclass, str) or
                         issubclass(subclass, str)))
        return NotImplemented


class ElementABC(DocABC):
    """Abstract base class for registering custom |Element| classes."""
    pass


class NodeABC(DocABC):
    """Abstract base class for registering custom |Node| classes."""
    pass


class DevicesABC(DocABC):
    """Abstract base class for registering custom |Devices| classes."""


class ElementsABC(DocABC):
    """Abstract base class for registering custom |Elements| classes."""


class NodesABC(DocABC):
    """Abstract base class for registering custom |Nodes| classes."""


class ConnectionsABC(DocABC):
    """Abstract base class for registering custom |Connections| classes."""


class VariableABC(DocABC):
    """Abstract base class for registering custom |Variable| classes.

    Usually, new classes should either be registered as a parameter
    or a sequence.  Afterwards, they are automatically handled as
    |Variable| subclasses:

    >>> from hydpy.core.abctools import VariableABC, ParameterABC
    >>> class New(object):
    ...     pass
    >>> issubclass(New, VariableABC)
    False
    >>> ParameterABC.register(New)
    >>> issubclass(New, VariableABC)
    True
    """
    value: Union[float, int, numpy.ndarray]
    values: Union[float, int, numpy.ndarray]
    initvalue: Union[float, int]
    fastaccess: Any


class ParameterABC(VariableABC):
    """Abstract base class for registering custom |Parameter| classes."""


class ANNABC(DocABC):
    """Abstract base class for registering custom |anntools.ANN| classes."""


class SeasonalANNABC(DocABC):
    """Abstract base class for registering custom |anntools.SeasonalANN|
    classes."""


class IOSequencesABC(DocABC):
    """Abstract base class for registering custom |IOSequences| classes."""


class InputSequencesABC(DocABC):
    """Abstract base class for registering custom |InputSequences| classes."""


class OutputSequencesABC(DocABC):
    """Abstract base class for registering custom "OutputSequences" classes
    like |FluxSequences|."""


class SequenceABC(VariableABC):
    """Abstract base class for registering custom |Sequence| classes."""
    pass


class IOSequenceABC(SequenceABC):
    """Abstract base class for registering custom |IOSequence| classes."""
    pass


class ModelSequenceABC(IOSequenceABC):
    """Abstract base class for registering custom |ModelSequence| classes."""
    pass


class InputSequenceABC(ModelSequenceABC):
    """Abstract base class for registering custom |InputSequence| classes."""
    pass


class FluxSequenceABC(ModelSequenceABC):
    """Abstract base class for registering custom |FluxSequence| classes."""
    pass


class ConditionSequenceABC(ModelSequenceABC):
    """Abstract base class for registering custom |ConditionSequence| classes.
    """
    pass


class StateSequenceABC(ConditionSequenceABC):
    """Abstract base class for registering custom |StateSequence| classes."""
    pass


class LogSequenceABC(ConditionSequenceABC):
    """Abstract base class for registering custom |LogSequence| classes."""
    pass


class AideSequenceABC(SequenceABC):
    """Abstract base class for registering custom |AideSequence| classes."""
    pass


class LinkSequenceABC(SequenceABC):
    """Abstract base class for registering custom |LinkSequence| classes."""
    pass


class NodeSequenceABC(IOSequenceABC):
    """Abstract base class for registering custom |NodeSequence| classes."""
    pass


class MaskABC(DocABC):
    """Abstract base class for registering custom `Mask` classes."""
    pass


class DateABC(DocABC):
    """Abstract base class for registering custom |Date| classes."""
    pass

    datetime: datetime.datetime


class PeriodABC(DocABC):
    """Abstract base class for registering custom |Period| classes."""
    pass


class TimegridABC(DocABC):
    """Abstract base class for registering custom |Timegrid| classes."""
    pass
    firstdate: DateABC
    lastdate: DateABC
    stepsize: PeriodABC


class TimegridsABC(DocABC):
    """Abstract base class for registering custom |Timegrids| classes."""
    pass


class TOYABC(DocABC):
    """Abstract base class for registering custom |TOY| classes."""
    pass
    month: int
    day: int
    hour: int
    minute: int
    second: int


class ModelABC(DocABC):
    """Abstract base class for registering custom |Model| classes."""

    @abc.abstractmethod
    def connect(self):
        ...

    @abc.abstractmethod
    def doit(self, idx):
        ...


autodoctools.autodoc_module()
