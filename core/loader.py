import importlib

class PluginInterface:
    """Used for initalizing the plugins interface."""

    @staticmethod
    def initialize() -> None:
        """Initializes a single plugin."""

def import_module(name: str) -> PluginInterface:
    """Import a custom plugin and return it as an interface."""
    return importlib.import_module(name)

def load_plugins(plugins: list[str]) -> None:
    """Load a given list of plugins."""
    for name in plugins:
        plugin = import_module(name)
        plugin.initialize()

def dict_list_to_lists(dict_list: list[dict]) -> list[list]:
    """Converts a list of dictionaries to a list of lists."""
    return [list(items) for items in zip(*[d.values() for d in dict_list])]
