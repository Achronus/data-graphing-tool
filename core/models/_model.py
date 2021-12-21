from abc import abstractmethod
from typing import Protocol

class Model(Protocol):
    """Basic representation of a model interface."""
    @abstractmethod
    def test(self) -> None:
        """Prints a string."""
        ...