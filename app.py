import json

from core import loader, factory
from core.logic.data_retriever import DataRetriever
from core.models.regression import LinearRegression, PolynomialRegression

def get_json_data(filename: str):
    """Reads and returns data from a given json file."""
    with open(f"./{filename}.json") as file:
        data = json.load(file)
    file.close()
    return data

def main() -> None:
    """Runs main functionality of the app."""
    # Register default model types
    factory.register("LinReg", LinearRegression)
    factory.register("PolyReg", PolynomialRegression)

    # Read data and load plugins
    data = get_json_data("map")
    loader.load_plugins(data["plugins"])

    # Initialise variables
    dr = DataRetriever(
        delimiters=loader.dict_list_to_lists(data["delimiters"]), 
        md_methods=loader.dict_list_to_lists(data["md_methods"])
    )

    # Create models
    models = [factory.create(model) for model in data['models']]

    for model in models:
        print(model, end="\n\t")
        model.load_data()

if __name__ == "__main__":
    main()
