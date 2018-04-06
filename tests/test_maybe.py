import pytest

from maybe import maybe, nothing


def test_map_applies_func_to_just_val():
    assert maybe(1).map(lambda x: x + 1) == maybe(2)


def test_nothing_maps_to_nothing():
    assert maybe(None).map(lambda x: x + 1) == nothing


def test_flatmap_accepts_funcs_returning_maybe():
    assert maybe(1).flatmap(lambda x: maybe(x + 1)) == maybe(2)


def test_unpacking():
    val, exists = maybe(1).unpack()
    assert (val, exists) == (1, True)
    val, exists = maybe(None).unpack()
    assert (val, exists) == (None, False)


def test_iteration():
    for v in maybe(1):
        assert v == 1
        break
    else:
        pytest.fail('Expected value to be unpacked')

    for _ in maybe(None):
        pytest.fail('Expected no value to be unpacked')
    assert True


def test_lazyness():
    add_called = False
    def add1(val):
        nonlocal add_called
        add_called = True
        return val + 1

    assert maybe.lazy(v
        for x in maybe(None)
        for v in add1(x)).is_nothing

    assert not add_called


def test_delegators():
    class Bunch:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    obj = maybe(Bunch(x=Bunch(y=Bunch(z=1))))
    assert obj._.x._.y._.z.val == 1

    obj = maybe(Bunch(x=Bunch(y=None)))

    assert obj._.x._.y._.z.is_nothing


def test_bool():
    assert maybe(1)
    assert not maybe(None)


def  test_get():
    assert maybe(1).get() == 1
    assert maybe(None).get(-1) == -1


def test_getitem():
    d = { 'x': { 'y': { 'z': 1 }, 'p': None } }
    assert maybe(d)._['x']._['y']._['z'].val == 1
    assert maybe(d)._['x']._['p']._['q'].is_nothing

    assert maybe(d)._['x']._['y']._['a'].is_nothing

    l = [[1], [2], None]
    assert maybe(l)._[0]._[0].val == 1
    assert maybe(l)._[0]._[1].is_nothing
    assert maybe(l)._[2]._[1].is_nothing


def test_monad_low():
    def f(x):
        return maybe(x + 1)

    def g(x):
        return maybe(x + 2)

    # 1. bind(unit(x), f) === f(x)


    assert maybe(1).flatmap(f) == f(1)

    # 2. bind(m, unit) === m
    assert maybe(1).flatmap(maybe) == maybe(1)

    # 3. bind(bind(m, f), g) === bind(m, x => bind(f(x), g))
    assert maybe(1).flatmap(f).flatmap(g) == maybe(1).flatmap(lambda x: f(x).flatmap(g))