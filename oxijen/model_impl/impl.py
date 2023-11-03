from oxijen.rdf_model import Resource, Property, Graph, Dataset
from pyoxigraph import Store, Triple, BlankNode, NamedNode, Literal, Quad
from typing import Iterator, Union, Optional

class ResourceImpl(Resource):

    def __init__(self, node: Union[BlankNode, NamedNode], graph: Graph):
        self._node = node
        self._graph = graph

    def add_property(self, property: 'Property', value: Union[Resource, Literal]) -> 'Resource':
        if isinstance(value, Resource):
            value = value.node
        
        self.graph.store.add(Quad(self.node, property.node, value, self.graph.name)) # assumes GraphStoreImpl!

        return self

    def list_properties(self, property: Optional[Property] = None) -> Iterator[Triple]:
        if isinstance(property, Property):
            property_node = property.node
        else:
            property_node = None

        quads = self.graph.store.quads_for_pattern(self.node, property_node, None, None)
        
        return map(lambda quad: quad.triple, quads)

    def remove_all(self, property: Optional[Property] = None) -> Resource:
        if isinstance(property, Property):
            property_node = property.node
        else:
            property_node = None

        quad_iter = self.graph.store.quads_for_pattern(self.node, property_node, None, None)
        
        for quad in quad_iter:
            self.graph.store.remove(quad)

        return self
    

class PropertyImpl(ResourceImpl, Property):

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
        quads = self.store.quads_for_pattern(None, None, None, self.name)

        return map(lambda quad: quad.triple, quads)


class DatasetStoreImpl(Dataset):

    def __init__(self, store: Store):
        self.store = store

    def graph_names(self) -> Iterator[Resource]:
        graph_names = self.store.named_graphs()
        
        return map(lambda name: ResourceImpl(name, None), graph_names)

    def get_named_graph(self, name: Union[str, Resource]) -> Graph:
        if type(name) is str:
            name_node = NamedNode(name)
        else:
            name_node = name.node

        return GraphStoreImpl(self.store, name_node)
    
    def add_named_graph(self, name: Union[str, Resource], graph: Graph) -> Dataset:
        if type(name) is str:
            name_node = NamedNode(name)
        else:
            name_node = name.node

        quads = map(lambda triple: Quad(triple.subject, triple.predicate, triple.object, name_node), graph.triples())
        self.store.extend(quads)

        return self

    def list_quads(self) -> Iterator[Quad]:
        return self.store.quads_for_pattern(None, None, None, None)