from oxijen import Resource, Graph, Dataset
from pyoxigraph import Quad, Store, NamedNode
from typing import Iterator
import ResourceImpl, GraphStoreImpl

class DatasetStoreImpl(Dataset):

    def __init__(self, store: Store):
        self.store = store

    def graph_names(self) -> Iterator[Resource]:
        graph_names = self.store.named_graphs()
        
        return map(lambda name: ResourceImpl(name, None), graph_names)

    def get_named_graph(self, name: str) -> Graph:
        return self.get_named_graph(ResourceImpl(NamedNode(name)))
    
    def get_named_graph(self, name: Resource) -> Graph:
        return GraphStoreImpl(self.store, name)

    def add_named_graph(self, name: Resource, graph: Graph) -> Dataset:
        quads = map(lambda triple: Quad(triple.subject, triple.predicate, triple.object, name), graph.triples())
        self.store.extend(graph)

        return self

    def list_quads(self) -> Iterator[Quad]:
        return self.graph.store.quads_for_pattern(None, None, None, None)