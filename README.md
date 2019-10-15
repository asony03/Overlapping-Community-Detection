# Project 2: Overlapping Community Detection
Project members:
- Amal Sony (asony)
- Prayani Singh (psingh)
- Tanmaya Nanda (tnanda)

This is an implementation for the algorithm from the paper: Efficient Identification of Overlapping
Communities

Python version used: Python 3.7.3

OS used: macOS Catalina (10.15)

Python libraries needed:

1. Networkx: Install using ```pip install networkx```
2. Numpy: Install using ```pip install numpy```

Instructions to run the program:
1. Go the the directory containing main.py
2. Run ```python main.py <grpah_file_path>``` where "graph_file_path" is the path to the graph file.
ex. ```python main.py ./datasets/amazon/amazon.small.graph```
For the above input, the output file is ```amazon.graph.small.clusters.txt```

The output file contains the list of communities identified for the graph given as input.
Every line represents one community and it contains the list of nodes in that community.

ex.

1917 1918 1919 1920 4906 4980 

2099 2100 2101 2102 2104 2105 2789 3997 

This output contains 2 communities. The first community contains 6 nodes and the second community contains 8 nodes.

Datasets tested:
- amazon.small.graph
- youtube.small.graph
- dblp.small.graph
