from oxijen.rdf_model import DatasetFactory
from pyoxigraph import Store, Literal

dataset = DatasetFactory.create_dataset(Store())

graph1 = dataset.get_named_graph("http://example.org/graph1")
resource1 = graph1.create_resource("http://example.org/subject1")
resource1.add_property(graph1.create_property("http://example.org/property1"), Literal("Object1"))
resource1.add_property(graph1.create_property("http://example.org/property2"), graph1.create_resource("http://example.org/object"))

graph2 = dataset.get_named_graph("http://example.org/graph2")
resource2 = graph1.create_resource("http://example.org/subject2")
resource2.add_property(graph1.create_property("http://example.org/property3"), Literal("Object2"))
resource3 = graph1.create_resource("http://example.org/subject3")
resource3.add_property(graph1.create_property("http://example.org/property4"), Literal("Object3"))

print("dataset.list_quads():\n")
print(list(dataset.list_quads()))

print("\ngraph1.list_triples():\n")
print(list(graph1.list_triples()))

print("\nresource1.list_properties():\n")
print(list(resource1.list_properties()))

print("\ngraph1.list_triples():\n")
print(list(graph1.list_triples()))

print("\nresource2.list_properties():\n")
print(list(resource2.list_properties()))

print("\nresource3.list_properties():\n")
print(list(resource3.list_properties()))