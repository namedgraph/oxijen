from oxijen import Resource, Graph, Property
from pyoxigraph import Triple, BlankNode, NamedNode, Quad
from typing import Iterator, Union

class ResourceImpl(Resource):

    def __init__(self, node: Union[BlankNode, NamedNode], graph: Graph):
        self.node = node
        self.graph = graph

    def add_property(self, property: Property, value: Union[NamedNode, BlankNode]) -> Resource:
        self.graph.store.add(Quad(self, property, value, None))

        return self

    def remove_all(self, property: Property) -> Resource:
        quad_iter = self.graph.store.quads_for_pattern(self, property, None, None)
        
        for quad in quad_iter:
            self.graph.store.remove(quad)

        return self

    def list_properties(self, property: Property) -> Iterator[Triple]:
        quads = self.graph.store.quads_for_pattern(self, property, None, None)
        
        return map(lambda quad: quad.triple, quads)