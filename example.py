from oxijen.rdf_model import DatasetFactory
from pyoxigraph import Store, Literal, serialize
import io

dataset = DatasetFactory.create_dataset(Store())

graph1 = dataset.default_graph
resource1 = graph1.create_resource("http://example.org/subject1")
resource1.add_property(graph1.create_property("http://example.org/property1"), Literal("Object1"))
resource1.add_property(graph1.create_property("http://example.org/property2"), graph1.create_resource("http://example.org/object"))

graph2 = dataset.get_named_graph("http://example.org/graph2")
resource2 = graph2.create_resource()
resource2.add_property(graph2.create_property("http://example.org/property3"), Literal("Object2"))
resource3 = graph2.create_resource("http://example.org/subject3")
resource3.add_property(graph2.create_property("http://example.org/property4"), Literal("Object3"))

print("dataset.list_quads():\n")
output = io.BytesIO()
serialize(list(dataset.list_quads()), output, "application/n-quads")
print(output.getvalue())

print("\ngraph1.list_triples():\n")
output = io.BytesIO()
serialize(list(graph1.list_triples()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())

print("\nresource1.uri:\n")
print(resource1.uri)

print("\nresource1.id:\n")
print(resource1.id)

print("\nresource1.list_properties():\n")
output = io.BytesIO()
serialize(list(resource1.list_properties()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())

print("\ngraph2.list_triples():\n")
output = io.BytesIO()
serialize(list(graph2.list_triples()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())

print("\nresource2.uri:\n")
print(resource2.uri)

print("\nresource2.id:\n")
print(resource2.id)

print("\nresource2.list_properties():\n")
output = io.BytesIO()
serialize(list(resource2.list_properties()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())

print("\nresource3.list_properties():\n")
output = io.BytesIO()
serialize(list(resource3.list_properties()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())