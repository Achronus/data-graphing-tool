# Data Graphing Tool

_In development!_

The Data Graphing Tool is a web application that providers users with a Graphical User Interface (GUI) to perform typical Machine Learning (ML) tasks. Once the user uploads a CSV file of data into the app, they are taken through a standard ML process, highlighted in figure 1.

It is designed for users with no prior programming knowledge but understand ML concepts or do not have time to write an algorithm and need an efficient way to visualise and understand their data.

![DGT Pipeline](/assets/imgs/dgt-pipeline.png)
_Figure 1. Data Graphing Tool User Process_

## File Structure

The tool uses a combination of abstract classes and the factory pattern to provide modularity in its design. It starts with two base algorithms, Linear and Polynomial regression, and incorporates additional models (ML algorithms) via the plugins folder. The file structure used for the tool is outlined below.

```text
.
+-- assets
|   +-- imgs
|       +-- ...
+-- core
|   +-- logic
|       +-- data_handler.py
|       +-- data_retriever.py
|   +-- models
|       +-- _model.py
|       +-- regression.py
|   +-- factory.py
|   +-- loader.py
+-- plugins
|   +-- ...
+-- app.py
+-- map.json
+-- README.md
```

### Structure Details

The `core` folder contains the main aspects of the tool, including the base models, the model template, and other crucial functionality.

The `logic` folder contains the backend functionality of the program that interfaces with the frontend.

The `plugins` folder houses additional models that act as extensions to the application.

The `app.py` file acts as the starting point of the program.

The `map.json` file provides the main attribute logic for each model (including plugin models). Additionally, provides helper attributes for other components of the application such as missing data methods and valid CSV file delimiters.
