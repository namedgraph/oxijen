from oxijen import Graph, Property, Resource
from pyoxigraph import BlankNode, NamedNode
import PropertyImpl, ResourceImpl

class GraphImpl(Graph):

    def create_resource(self) -> Resource:
        return ResourceImpl(BlankNode(), self)

    def create_resource(self, uri: str) -> Resource:
        return ResourceImpl(NamedNode(uri), self)

    def create_property(self, uri: str) -> Property:
        return PropertyImpl(NamedNode(uri), self)