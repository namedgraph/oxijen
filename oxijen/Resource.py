from abc import ABC, abstractmethod
from pyoxigraph import NamedNode, BlankNode, Triple
from typing import Iterator, Union
from oxijen import Property

#class Property:
#    pass

class Resource(ABC):

    @abstractmethod
    def add_property(self, property: Property, value: Union[NamedNode, BlankNode]) -> 'Resource':
        pass

    @abstractmethod
    def remove_all(self, property: Property) -> 'Resource':
        pass

    @abstractmethod
    def list_properties(self, property: Property) -> Iterator[Triple]:
        pass