from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Basic representation of a model."""
    @abstractmethod
    def load_data(self) -> None:
        """Loads the data into the model."""
        pass

    @abstractmethod
    def build(self) -> None:
        """Creates the model."""
        pass

    @abstractmethod
    def train(self) -> None:
        """Trains the model."""
        pass

    @abstractmethod
    def evaluate(self) -> None:
        """Evaluates the model."""
        pass