from abc import ABC, abstractmethod
from typing import Iterator, Union
from pyoxigraph import Store, Triple, Quad, BlankNode, NamedNode
from model.impl import DatasetStoreImpl

class Resource(ABC):

    @abstractmethod
    def add_property(self, property: 'Property', value: Union[NamedNode, BlankNode]) -> 'Resource':
        pass

    @abstractmethod
    def remove_all(self, property: 'Property') -> 'Resource':
        pass

    @abstractmethod
    def list_properties(self, property: 'Property') -> Iterator[Triple]:
        pass

class Property(Resource):

    pass

class GraphFactory:

    #@staticmethod
    #def create_graph() -> Dataset:
    #    return GraphImpl()

    pass

class Graph(ABC):

    @abstractmethod
    def create_resource(self) -> Resource:
        pass

    @abstractmethod
    def create_resource(self, uri: str) -> Resource:
        pass

    @abstractmethod
    def create_property(self, uri: str) -> Property:
        pass

    @abstractmethod
    def list_triples(self) -> Iterator[Triple]:
        pass

class Dataset(ABC):

    @abstractmethod
    def graph_names(self) -> Iterator[Resource]:
        pass

    @abstractmethod
    def get_named_graph(self, name: str) -> Graph:
        pass

    @abstractmethod
    def get_named_graph(self, name: Resource) -> Graph:
        pass

    @abstractmethod
    def add_named_graph(self, name: Resource, graph: Graph) -> 'Dataset':
        pass

    @abstractmethod
    def list_quads(self) -> Iterator[Quad]:
        pass

class DatasetFactory:

    @staticmethod
    def create_dataset(store: Store) -> Dataset:
        return DatasetStoreImpl(store)