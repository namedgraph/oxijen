from abc import ABC, abstractmethod
from typing import Iterator, Union, Optional
from pyoxigraph import Store, Triple, Quad, Literal, NamedNode, BlankNode

class Resource(ABC):

    @property
    def node(self):
        return self._node

    @property
    def graph(self):
        return self._graph

    @property
    def uri(self):
        if isinstance(self.node, NamedNode):
            return self.node.value
        else:
            return None

    @property
    def id(self):
        if isinstance(self.node, BlankNode):
            return self.node.value
        else:
            return None
    
    @abstractmethod
    def add_property(self, property: 'Property', value: Union['Resource', Literal]) -> 'Resource':
        pass

    @abstractmethod
    def remove_all(self, property: 'Property') -> 'Resource':
        pass

    @abstractmethod
    def list_properties(self, property: 'Property') -> Iterator[Triple]:
        pass


class Property(Resource):

    pass


class Graph(ABC):

    @abstractmethod
    def create_resource(self, uri: Optional[str] = None) -> Resource:
        pass

    @abstractmethod
    def create_property(self, uri: str) -> Property:
        pass

    @abstractmethod
    def list_triples(self) -> Iterator[Triple]:
        pass


class GraphFactory:

    #@staticmethod
    #def create_graph() -> Dataset:
    #    return GraphImpl()

    pass


class Dataset(ABC):

    @property
    def default_graph(self):
        pass
    
    @abstractmethod
    def graph_names(self) -> Iterator[Resource]:
        pass

    @abstractmethod
    def get_named_graph(self, name: Union[str, Resource]) -> Graph:
        pass

    @abstractmethod
    def add_named_graph(self, name: Union[str, Resource], graph: Graph) -> 'Dataset':
        pass

    @abstractmethod
    def list_quads(self) -> Iterator[Quad]:
        pass


class DatasetFactory:

    @staticmethod
    def create_dataset(store: Store) -> Dataset:
        from oxijen.model_impl.impl import DatasetStoreImpl

        return DatasetStoreImpl(store)