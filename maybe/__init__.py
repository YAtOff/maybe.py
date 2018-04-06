__all__ = ['maybe']


class NoValueError(Exception):
    pass


class Maybe:
    pass


class Just(Maybe):

    class JustDelegator:

        def __init__(self, val):
            self.val = val

        def __getattr__(self, name):
            return maybe(getattr(self.val, name))

        def __getitem__(self, item):
            try:
                return maybe(self.val[item])
            except (KeyError, IndexError, TypeError):
                return nothing

        def __missing__(self, key):
            return maybe(self.val.__missing__(key))

        def __setitem__(self, key, value):
            self.val.__setitem__(key, value)

        def __delitem__(self, key):
            self.val.__delitem__(key)

        def __repr__(self):
            return maybe(self.val.__repr__())

        def __str__(self):
            return maybe(self.val.__str__())

        def __bytes__(self):
            return maybe(self.val.__bytes__())

        def __format__(self, format_spec):
            return maybe(self.val.__format__(format_spec))

        def __lt__(self, other):
            return maybe(self.val.__lt__(other))

        def __le__(self, other):
            return maybe(self.val.__le__(other))

        def __eq__(self, other):
            return maybe(self.val.__eq__(other))

        def __ne__(self, other):
            return maybe(self.val.__ne__(other))

        def __gt__(self, other):
            return maybe(self.val.__gt__(other))

        def __ge__(self, other):
            return maybe(self.val.__ge__(other))

        def __hash__(self):
            return maybe(self.val.__hash__())

        def __bool__(self):
            return maybe(self.val.__bool__())

        def __dir__(self):
            return maybe(self.val.__dir__())

        def __call__(self, *args, **kwargs):
            return maybe(self.val.__call__(*args, **kwargs))

        def __len__(self):
            return maybe(self.val.__len__())

        def __length_hint__(self):
            return maybe(self.val.__length_hint__())

        def __iter__(self):
            return maybe(self.val.__iter__())

        def __reversed__(self):
            return maybe(self.val.__reversed__())

        def __contains__(self, item):
            return maybe(self.val.__contains__(item))

        def __add__(self, other):
            return maybe(self.val.__add__(other))

        def __sub__(self, other):
            return maybe(self.val.__sub__(other))

        def __mul__(self, other):
            return maybe(self.val.__mul__(other))

        def __matmul__(self, other):
            return maybe(self.val.__matmul__(other))

        def __truediv__(self, other):
            return maybe(self.val.__truediv__(other))

        def __floordiv__(self, other):
            return maybe(self.val.__floordiv__(other))

        def __mod__(self, other):
            return maybe(self.val.__mod__(other))

        def __divmod__(self, other):
            return maybe(self.val.__divmod__(other))

        def __pow__(self, other, modulo=None):
            return maybe(self.val.__pow__(other, modulo))

        def __lshift__(self, other):
            return maybe(self.val.__lshift__(other))

        def __rshift__(self, other):
            return maybe(self.val.__rshift__(other))

        def __and__(self, other):
            return maybe(self.val.__and__(other))

        def __xor__(self, other):
            return maybe(self.val.__xor__(other))

        def __or__(self, other):
            return maybe(self.val__or__(other))

        def __radd__(self, other):
            return maybe(self.val.__radd__(other))

        def __rsub__(self, other):
            return maybe(self.val.__rsub__(other))

        def __rmul__(self, other):
            return maybe(self.val.__rmul__(other))

        def __rmatmul__(self, other):
            return maybe(self.val.__rmatmul__(other))

        def __rtruediv__(self, other):
            return maybe(self.val.__rtruediv__(other))

        def __rfloordiv__(self, other):
            return maybe(self.val.__rfloordiv__(other))

        def __rmod__(self, other):
            return maybe(self.val.__rmod__(other))

        def __rdivmod__(self, other):
            return maybe(self.val__rdivmod__(other))

        def __rpow__(self, other):
            return maybe(self.val.__rpow__(other))

        def __rlshift__(self, other):
            return maybe(self.val.__rlshift__(other))

        def __rrshift__(self, other):
            return maybe(self.val.__rrshift__(other))

        def __rand__(self, other):
            return maybe(self.val.__rand__(other))

        def __rxor__(self, other):
            return maybe(self.val.__rxor__(other))

        def __ror__(self, other):
            return maybe(self.val.__ror__(other))

        def __iadd__(self, other):
            self.val.__iadd__(other)

        def __isub__(self, other):
            self.val.__isub__(other)

        def __imul__(self, other):
            self.val.__imul__(other)

        def __imatmul__(self, other):
            self.val.__imatmul__(other)

        def __itruediv__(self, other):
            self.val.__itruediv__(other)

        def __ifloordiv__(self, other):
            self.val.__ifloordiv__(other)

        def __imod__(self, other):
            self.val.__imod__(other)

        def __ipow__(self, other, modulo=None):
            self.val.__ipow__(other, modulo)

        def __ilshift__(self, other):
            self.val.__ilshift__(other)

        def __irshift__(self, other):
            self.val.__irshift__(other)

        def __iand__(self, other):
            self.val.__iand__(other)

        def __ixor__(self, other):
            self.val.__ixor__(other)

        def __ior__(self, other):
            self.val.__ior__(other)

        def __neg__(self):
            return maybe(self.val.__neg__())

        def __pos__(self):
            return maybe(self.val.__pos__())

        def __abs__(self):
            return maybe(self.val.__abs__())

        def __invert__(self):
            return maybe(self.val.__invert__())

        def __complex__(self):
            return maybe(self.val.__complex__())

        def __int__(self):
            return maybe(self.val.__int__())

        def __float__(self):
            return maybe(self.val.__float__())

        def __index__(self):
            return maybe(self.val.__index__())

        def __round__(self, ndigits=None):
            return maybe(self.val.__round__(ndigits))

        def __trunc__(self):
            return maybe(self.val.__trunc__())

        def __floor__(self):
            return maybe(self.val.__floor__())

        def __ceil__(self):
            return maybe(self.val.__ceil__())


    def __init__(self, val):
        self._val = val
        self._ = self.JustDelegator(val)

    @property
    def val(self):
        return self._val

    def map(self, func):
        return Just(func(self.val))

    def flatmap(self, func):
        result = func(self.val)
        return result

    def unpack(self):
        return (self.val, True)

    def get(self, default=None):
        return self.val

    @property
    def is_nothing(self):
        return False

    def __eq__(self, other):
        return isinstance(other, Just) and self.val == other.val

    def __iter__(self):
        return iter((self.val,))

    def __bool__(self):
        return True

    def __repr__(self):
        return u'Just({!r}'.format(self.val)

    def __str__(self):
        return u'Just {}'.format(self.val)


class Nothing(Maybe):

    class NothingDelegator:

        def return_nothing(self, *args, **kwargs):
            return nothing

        def nop(self, *args, **kwargs):
            pass

        __getattr__ = return_nothing
        __getitem__ = return_nothing
        __missing__ = return_nothing
        __setitem__ = nop
        __delitem__ = nop
        __repr__ = return_nothing
        __str__ = return_nothing
        __bytes__ = return_nothing
        __format__ = return_nothing
        __lt__ = return_nothing
        __le__ = return_nothing
        __eq__ = return_nothing
        __ne__ = return_nothing
        __gt__ = return_nothing
        __ge__ = return_nothing
        __hash__ = return_nothing
        __bool__ = return_nothing
        __dir__ = return_nothing
        __call__ = return_nothing
        __len__ = return_nothing
        __length_hint__ = return_nothing
        __iter__ = return_nothing
        __reversed__ = return_nothing
        __contains__ = return_nothing
        __add__ = return_nothing
        __sub__ = return_nothing
        __mul__ = return_nothing
        __matmul__ = return_nothing
        __truediv__ = return_nothing
        __floordiv__ = return_nothing
        __mod__ = return_nothing
        __divmod__ = return_nothing
        __pow__ = return_nothing
        __lshift__ = return_nothing
        __rshift__ = return_nothing
        __and__ = return_nothing
        __xor__ = return_nothing
        __or__ = return_nothing
        __radd__ = return_nothing
        __rsub__ = return_nothing
        __rmul__ = return_nothing
        __rmatmul__ = return_nothing
        __rtruediv__ = return_nothing
        __rfloordiv__ = return_nothing
        __rmod__ = return_nothing
        __rdivmod__ = return_nothing
        __rpow__ = return_nothing
        __rlshift__ = return_nothing
        __rrshift__ = return_nothing
        __rand__ = return_nothing
        __rxor__ = return_nothing
        __ror__ = return_nothing
        __iadd__ = nop
        __isub__ = nop
        __imul__ = nop
        __imatmul__ = nop
        __itruediv__ = nop
        __ifloordiv__ = nop
        __imod__ = nop
        __ipow__ = nop
        __ilshift__ = nop
        __irshift__ = nop
        __iand__ = nop
        __ixor__ = nop
        __ior__ = nop
        __neg__ = return_nothing
        __pos__ = return_nothing
        __abs__ = return_nothing
        __invert__ = return_nothing
        __complex__ = return_nothing
        __int__ = return_nothing
        __float__ = return_nothing
        __index__ = return_nothing
        __round__ = return_nothing
        __trunc__ = return_nothing
        __floor__ = return_nothing
        __ceil__ = return_nothing

    _ = NothingDelegator()

    @property
    def val(self):
        raise NoValueError

    def map(self, func):
        return self

    def flatmap(self, func):
        return self

    def unpack(self):
        return (None, False)

    def get(self, default=None):
        return default

    @property
    def is_nothing(self):
        return True

    def __eq__(self, other):
        return isinstance(other, Nothing)

    def __iter__(self):
        return iter(())

    def __bool__(self):
        return False

    def __repr__(self):
        return u'Nothing()'

    def __str__(self):
        return u'Nothing'


nothing = Nothing()


def maybe(val):
    return val if isinstance(val, Maybe) \
        else Just(val) if val is not None else nothing


def maybe_lazy(generator):
    return maybe(next(generator, None))
maybe.lazy = maybe_lazy
