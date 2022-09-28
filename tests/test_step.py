from typing import Callable

from footwork.step import step, Step, _STEP_REGISTRY


def test_step_wrapper_no_name_arg():
    @step()
    def hello():
        return "world"

    assert isinstance(hello, Callable)
    assert isinstance(hello(), Step)
    assert "hello" in _STEP_REGISTRY
    assert isinstance(_STEP_REGISTRY["hello"], Step)
    assert _STEP_REGISTRY["hello"].name == "hello"
    assert isinstance(_STEP_REGISTRY["hello"].fn, Callable)


def test_step_wrapper_name_arg():
    @step(name="foo")
    def hello():
        return "world"

    assert isinstance(hello, Callable)
    assert isinstance(hello(), Step)
    assert "foo" in _STEP_REGISTRY
    assert _STEP_REGISTRY["foo"].name == "foo"
    assert isinstance(_STEP_REGISTRY["foo"].fn, Callable)
