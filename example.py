from oxijen.model import DatasetFactory
from pyoxigraph import Store, Literal

dataset = DatasetFactory.create_dataset(Store())
graph = dataset.get_named_graph("http://example.org/graph")
resource = graph.create_resource("http://example.org/subject")
resource.add_property(graph.create_property("http://example.org/property"), Literal("literal"))
print(list(graph.list_triples()))