from pyoxigraph import Store, Triple, BlankNode, NamedNode
from typing import Union, Iterator
import GraphImpl

class GraphStoreImpl(GraphImpl):

    def __init__(self, store: Store, name: Union[BlankNode, NamedNode]):
        self.store = store
        self.name = name

    def list_triples(self) -> Iterator[Triple]:
        quads = self.graph.store.quads_for_pattern(None, None, None, self.name)

        return map(lambda quad: quad.triple, quads)