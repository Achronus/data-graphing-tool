from dataclasses import dataclass

from core import factory
from core.models._model import BaseModel

@dataclass
class Demo(BaseModel):
    """A dummy model for demo purposes."""
    name: str
    
    def load_data(self) -> None:
        """Loads the data into the model."""
        print(f"This is a demo. My name is: {self.name}.")

    def build(self) -> None:
        """Creates the model."""
        pass

    def train(self) -> None:
        """Trains the model."""
        pass

    def evaluate(self) -> None:
        """Evaluates the model."""
        pass

def initialize() -> None:
    factory.register("demo", Demo)
