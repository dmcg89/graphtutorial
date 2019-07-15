#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        #  check if vertex is already a neighbor
        if vertex in self.neighbors:
            raise ValueError('Item exists in neighbor: {}'.format(vertex))
        #  if not, add vertex to neighbors and assign weight.
        else:
            self.neighbors[vertex] = weight
            # return self.neighbors


    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        #  return the neighbors
        return self.neighbors.keys()

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        #  return the weight of the edge from this vertex to the given vertex.
        return self.neighbors.values()


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_dict = {}
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        #  increment the number of vertices
        self.numVertices += 1
        #  create a new vertex
        new_vertex = Vertex(key)
        #  add the new vertex to the vertex list
        self.vert_dict[key] = new_vertex
        #  return the new vertex
        return self

    def getVertex(self, n):
        """return the vertex if it exists"""
        #  return the vertex if it is in the graph
        if n in self.vert_dict:
            return n
        raise ValueError('Vertex not found: {}'.format(n))

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if f not in self.vert_dict or t not in self.vert_dict:
            raise ValueError('One of the vertices not in graph')
            # if both vertices in the graph, add the
            # edge by making t a neighbor of f
        else:
            # and using the addNeighbor method of the Vertex class.
            # Hint: the vertex f is stored in self.vertList[f].
            self.vert_dict[f].addNeighbor(self.vert_dict[t])


    def getVertices(self):
        """return all the vertices in the graph"""
        # return self.vertList.keys()
        return self.vert_dict.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")
    g.addVertex("Friend 4")
    g.addVertex("Friend 5")
    g.addVertex("Friend 6")
    g.addVertex("Friend 7")
    g.addVertex("Friend 8")
    g.addVertex("Friend 9")
    g.addVertex("Friend 10")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")
    g.addEdge("Friend 3", "Friend 4")
    g.addEdge("Friend 4", "Friend 5")
    g.addEdge("Friend 5", "Friend 6")
    g.addEdge("Friend 7", "Friend 8")
    g.addEdge("Friend 8", "Friend 9")
    g.addEdge("Friend 9", "Friend 10")
    
    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
