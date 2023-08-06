from collections import namedtuple
from operator import lt, gt

def new_by_id(attr):
    '''
    Store all initializations of the class.
    Define class.by_id, a function from value to class,
    where the value must be among the known values for that attr.
    '''
    def decorator(cls1):
        class cls2(cls1):
            _index = {}
            def __new__(cls2, *args, **kwargs):
                self = cls1.__new__(cls2, *args, **kwargs)
                identifier = getattr(self, attr)
                if identifier in self._index:
                    msg = 'Identifier "%s" is already in index.'
                    raise KeyError(msg % identifier)
                self._index[identifier] = self
                return self
            @classmethod
            def by_id(cls, identifier):
                if identifier not in cls._index:
                    msg = 'No object identified by "%s" is in the index.'
                    raise KeyError(msg % identifier)
                return cls._index[identifier]
        cls2.__name__ = cls1.__name__
        return cls2
    return decorator

def sort_by(attr):
    '''
    Define __lt__ on an attribute of the namedtuple.
    '''
    def decorator(cls1):
        class cls2(cls1):
            def __lt__(self, other):
                return self._compare(other, lt)
            def __gt__(self, other):
                return self._compare(other, gt)
            def _compare(self, other, operator):
                if isinstance(other, cls2):
                    return operator(getattr(self, attr), getattr(other, attr))
                else:
                    msg = '"%s" not supported between instances of "%s" and "%s"'
                    params = (
                        operator.__name__,
                        self.__class__.__name__,
                        other.__class__.__name__,
                    )
                    raise TypeError(msg % params)
                return getattr(self, attr) + other
        return cls2
    return decorator


def add_attr(attr):
    '''
    Define addition on an attribute of the namedtuple.
    '''
    def decorator(cls1):
        class cls2(cls1):
            def __add__(self, other):
                return getattr(self, attr) + other
            __radd__ = __add__
        return cls2
    return decorator

def mixin(*attrs):
    '''
    Mix a namedtuple into the decorated class.
    '''
    def decorator(cls):
        new_cls = namedtuple(cls.__name__, attrs)
        return _inheret(new_cls, cls)
    return decorator

def _inheret(cls, mix):
    class descendant(cls, mix):
        pass
    descendant.__name__ = cls.__name__
    return descendant
