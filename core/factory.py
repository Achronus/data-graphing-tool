"""A factor that enables registering and unregistering models."""
from typing import Callable, Any

from core.models._model import BaseModel

model_creation_funcs: dict[str, Callable[..., BaseModel]] = {}

def register(model_type: str, creation_func: Callable[..., BaseModel]) -> None:
    """Registers a new model."""
    model_creation_funcs[model_type] = creation_func

def unregister(model_type: str) -> None:
    """Unregisters a model."""
    model_creation_funcs.pop(model_type, None)

def create(arguments: dict[str, Any]) -> BaseModel:
    """Create a model of a specific type, given a dictionary of arguments."""
    args_copy = arguments.copy()
    model_type = args_copy.pop("type")

    try:
        creation_func = model_creation_funcs[model_type]
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown model type: {model_type!r}")
