
class InvalidMissingDataMethod(Exception):
    """Exception for handling invalid missing data methods."""
    def __init__(self, method: str, valid_methods: list[str]):
        self.method = method
        self.valid_methods = valid_methods

    def __str__(self):
        return f"Invalid method type entered: '{self.method}'. \n\tPlease enter a valid method type: {self.valid_methods}"
