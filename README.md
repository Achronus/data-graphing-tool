# Data Graphing Tool

_In development!_

The Data Graphing Tool is a web application that providers users with a Graphical User Interface (GUI) to perform typical Machine Learning (ML) tasks. Once the user uploads a CSV file of data into the app, they are taken through a standard ML process, highlighted in figure 1.

It is designed for users with no prior programming knowledge but understand ML concepts or do not have time to write an algorithm and need an efficient way to visualise and understand their data.

![DGT Pipeline](/assets/imgs/dgt-pipeline.png)

<center style="font-style: italic;">Figure 1. Data Graphing Tool User Process</center>

## File Structure

The tool uses a combination of protocols and the factory pattern to provide modularity in its design. It starts with two base algorithms, Linear and Polynomial regression, and incorporates additional models (ML algorithms) via the plugins folder. The file structure used for the tool is outlined below.

```text
.
+-- assets
|   +-- imgs
|       +-- ...
+-- core
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

### Aspects Of Note

The `core` folder contains the main aspects of the tool, including the base models, the model protocol template, and other crucial functionality.

The `plugins` folder houses additional models that act as extensions to the application.

The `app.py` file acts as the starting point of the program.

The `map.json` file provides the main attribute logic for each model (including plugin models).
