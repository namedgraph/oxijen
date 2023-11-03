from oxijen.model import Resource, Property, Graph, Dataset
from pyoxigraph import Store, Triple, BlankNode, NamedNode, Quad
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

class PropertyImpl(ResourceImpl, Property):
    
    # def __init__(self, node: Union[BlankNode, NamedNode], graph: Graph):
    #     self.node = node
    #     self.graph = graph
    pass

class GraphImpl(Graph):

    def create_resource(self) -> Resource:
        return ResourceImpl(BlankNode(), self)

    def create_resource(self, uri: str) -> Resource:
        return ResourceImpl(NamedNode(uri), self)

    def create_property(self, uri: str) -> Property:
        return ResourceImpl(NamedNode(uri), self)
    
class GraphStoreImpl(GraphImpl):

    def __init__(self, store: Store, name: Union[BlankNode, NamedNode]):
        self.store = store
        self.name = name

    def list_triples(self) -> Iterator[Triple]:
        quads = self.graph.store.quads_for_pattern(None, None, None, self.name)

        return map(lambda quad: quad.triple, quads)
    
class DatasetStoreImpl(Dataset):

    def __init__(self, store: Store):
        self.store = store

    def graph_names(self) -> Iterator[Resource]:
        graph_names = self.store.named_graphs()
        
        return map(lambda name: Resource(name, None), graph_names)

    def get_named_graph(self, name: str) -> Graph:
        return self.get_named_graph(Resource(NamedNode(name)))
    
    def get_named_graph(self, name: Resource) -> Graph:
        return GraphStoreImpl(self.store, name)

    def add_named_graph(self, name: Resource, graph: Graph) -> Dataset:
        quads = map(lambda triple: Quad(triple.subject, triple.predicate, triple.object, name), graph.triples())
        self.store.extend(quads)

        return self

    def list_quads(self) -> Iterator[Quad]:
        return self.graph.store.quads_for_pattern(None, None, None, None)