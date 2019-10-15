#Implementation for paper 1:Efficient Identification of Overlapping Communities

#Project Team Members:
#1. Amal Sony (asony)
#2. Prayani Singh (psingh)
#3. Tanmaya Nanda (tnanda)

import os
import sys
import networkx as nx
import numpy as np

def weight(graph):
    #Input: A networkx graph
    #Output: Density of the graph
    if nx.number_of_nodes(graph) == 0:
        return 0
    else:
        return float(2*nx.number_of_edges(graph)/nx.number_of_nodes(graph))

def rank(vertex):
    #Input: A tuple containing vertex and its rank
    #Output: Rank of the node
    return vertex[1]

def orderVertices(graph):
    #Input: A networkx graph
    #Output: A list of tuples(vertex,rank) ordered according to the decreasing order of their ranks.
    vertices = nx.pagerank(graph).items()
    vertices = sorted(vertices, reverse=True, key=rank)
    return vertices

def LA(graph):
    #Input: A networkx graph
    #Output: Seed clusters to be fed into the Improved Iterative Scan Algorithm)

    #Order vertices using page rank
    vertices = orderVertices(graph)
    clusters = []
    for vertex in vertices:
        added = False
        for cluster in clusters:
            #Add the vertex to the cluster to check whether the density increases.
            before_adding_vertex = graph.subgraph(cluster)
            updated_cluster = list(cluster)
            updated_cluster.append(vertex[0])
            after_adding_vertex = graph.subgraph(updated_cluster)
            #If wieght increases, add the vertex to the cluster
            if weight(after_adding_vertex) > weight(before_adding_vertex):
                added = True
                cluster.append(vertex[0])
        if added == False:
            clusters.append([vertex[0]])
    return clusters

def IS2(cluster, graph):
    #Input: Cluster to be improved and the networkx graph
    #Output: Improved cluster
    w = weight(graph.subgraph(cluster))
    increased = True
    while increased:
        combined_cluster = list(cluster)
        #Get adjacent vertices of each vertex and add it to the cluster
        for vertex in cluster:
            adjacent_vertices = graph.neighbors(vertex)
            combined_cluster = list(set(combined_cluster).union(set(adjacent_vertices)))
        
        #Remove or add vertex to check the change in the density of the cluster
        for vertex in combined_cluster:
            new_cluster = list(cluster)
            if vertex in cluster:
                new_cluster.remove(vertex)
            else:
                new_cluster.append(vertex)
            original_subgraph = graph.subgraph(cluster)
            new_subgraph = graph.subgraph(new_cluster)
            if weight(new_subgraph) > weight(original_subgraph):
                cluster = list(new_cluster)
        
        w_new = weight(graph.subgraph(cluster))
        if w_new == w:
            increased = False
        else:
            w = w_new
    return cluster

if __name__ == "__main__":
    #Read input file
    graph_file_path = sys.argv[1]
    graph_file = open(graph_file_path, 'r')
    #Moving to the second row since the first row contains the number of nodes and edges
    next(graph_file)

    #Create a graph
    g = nx.Graph()
    #Add vertices and edges to the graph.
    for line in graph_file:
        line = line.split()
        g.add_edge(int(line[0]),int(line[1]))
    
    #Generate initial clusters using Link Aggregate Algorithm
    initial_clusters = LA(g)
    unique_initial_clusters = []
    #Get final clusters using Improved Iterative Scan Algorithm
    final_clusters = []
    for cluster in initial_clusters:
        updated_cluster = IS2(cluster,g)
        final_clusters.append(updated_cluster)
            
    
    #Removing duplicate clusters and printing the output to a file
    output_file_path = os.path.basename(graph_file_path) + ".clusters.txt"
    output_file = open(output_file_path, 'w')
    unique_final_clusters = []

    for cluster in final_clusters:
        cluster = sorted(cluster)
        if cluster not in unique_final_clusters:
            unique_final_clusters.append(cluster)
            print(*cluster, sep=' ', end='\n', file=output_file)
