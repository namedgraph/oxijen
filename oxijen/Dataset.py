from abc import ABC, abstractmethod
from pyoxigraph import Quad
from typing import Iterator
from oxijen import Resource, Graph

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