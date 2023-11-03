from oxijen.impl import ResourceImpl
from pyoxigraph import Triple, BlankNode, NamedNode, Quad
from typing import Union
from oxijen import Graph

class PropertyImpl(ResourceImpl):
    
    def __init__(self, node: Union[BlankNode, NamedNode], graph: Graph):
        self.node = node
        self.graph = graph