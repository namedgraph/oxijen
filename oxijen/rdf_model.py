from abc import ABC, abstractmethod
from typing import Iterator, Union, Optional, Any
from pyoxigraph import Store, Triple, Quad, Literal, NamedNode, BlankNode

class Resource(ABC):

    @property
    def node(self):
        return self._node

    @property
    def graph(self):
        return self._graph

    @property
    def is_anon(self):
        if isinstance(self.node, NamedNode):
            return False
        else:
            return True
        
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
    def __len__(self) -> int:
        pass

    @abstractmethod
    def create_resource(self, uri: Optional[str] = None) -> Resource:
        pass

    @abstractmethod
    def create_property(self, uri: str) -> Property:
        pass

    @abstractmethod
    def create_literal(self, value: str, language: Optional[str] = None) -> Literal:
        pass

    @abstractmethod
    def create_typed_literal(self, value: Any, datatype: Optional[Union[str, NamedNode]] = None) -> Literal:
        pass

    @abstractmethod
    def list_subjects(self) -> Iterator[Resource]:
        pass

    @abstractmethod
    def list_triples(self) -> Iterator[Triple]:
        pass

    @abstractmethod
    def add(self, triples: Union[Iterator[Triple], 'Graph']) -> 'Graph':
        pass

    @abstractmethod
    def remove_all(self ) -> 'Graph':
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
    def contains_named_graph(self, name: Union[str, Resource]) -> bool:
        pass

    @abstractmethod
    def get_named_graph(self, name: Union[str, Resource]) -> Graph:
        pass

    @abstractmethod
    def add_named_graph(self, name: Union[str, Resource], graph: Graph) -> 'Dataset':
        pass

    @abstractmethod
    def remove_named_graph(self, name: Union[str, Resource], graph: Graph) -> 'Dataset':
        pass

    @abstractmethod
    def list_quads(self) -> Iterator[Quad]:
        pass


class DatasetFactory:

    @staticmethod
    def create_dataset(store: Store) -> Dataset:
        from oxijen.model_impl.impl import DatasetStoreImpl

        return DatasetStoreImpl(store)