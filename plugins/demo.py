from dataclasses import dataclass

from core import factory

@dataclass
class Demo:
    """A dummy model for demo purposes."""
    name: str
    
    def test(self) -> None:
        print(f"This is a demo. My name is: {self.name}.")

def initialize() -> None:
    factory.register("demo", Demo)