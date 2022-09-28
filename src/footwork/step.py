from functools import wraps
from typing import Callable, Optional

from pydantic import BaseModel


class Step(BaseModel):
    name: str
    fn: Callable

    # def __call__(self, **kwargs):
    #     # Graph.current_graph.add_node(self)
    #     for key, kwarg_value in kwargs.items():
    #         if isinstance(kwarg_value, Step):
    #             if isinstance(Graph.current_graph, Graph):
    #                 Graph.current_graph.draw_edge(self, kwarg_value)
    #                 return self
    #             raise Exception("CURRENT_GRAPH has not been created")
    #         raise Exception("you done goofed")
    #     return self

    class Config:
        exclude = {"lfunc"}


_STEP_REGISTRY: dict[str, Step] = {}


def step(name: Optional[str] = None) -> Callable:
    def step_decorator(func) -> Callable:
        @wraps(func)
        def wrapper_node(*args, **kwargs) -> Step:
            node_name = name if name else func.__name__
            _STEP_REGISTRY[node_name] = Step(fn=func, name=node_name)
            return _STEP_REGISTRY[node_name]
        return wrapper_node
    return step_decorator
