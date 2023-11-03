from abc import ABC, abstractmethod
from pyoxigraph import Triple
from typing import Iterator
from oxijen import Property, Resource

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