from oxijen.rdf_model import DatasetFactory
from pyoxigraph import Store, Literal, serialize
import io

dataset = DatasetFactory.create_dataset(Store())

graph1 = dataset.default_graph
resource1 = graph1.create_resource("http://example.org/subject1")
resource1.add_property(graph1.create_property("http://example.org/property1"), graph1.create_literal("Object1"))
resource1.add_property(graph1.create_property("http://example.org/property2"), graph1.create_resource("http://example.org/object"))
resource1.add_property(graph1.create_property("http://example.org/property2"), graph1.create_typed_literal(42))

graph2 = dataset.get_named_graph("http://example.org/graph2")
resource2 = graph2.create_resource()
resource2.add_property(graph2.create_property("http://example.org/property3"), graph2.create_literal("Object2", language="da"))
resource3 = graph2.create_resource("http://example.org/subject3")
resource3.add_property(graph2.create_property("http://example.org/property4"), graph2.create_literal("Object3"))
resource3.add_property(graph2.create_property("http://example.org/property5"), graph2.create_literal("Object4"))

graph3 = dataset.get_named_graph("http://example.org/graph3")
graph3.add(graph1)

print("dataset.list_quads():\n")
output = io.BytesIO()
serialize(list(dataset.list_quads()), output, "application/n-quads")
print(output.getvalue())

print("\ndataset.graph_names():\n")
print(list(dataset.graph_names()))

print("\ndataset.contains_named_graph(\"http://example.org/graph2\"):\n")
print(dataset.contains_named_graph("http://example.org/graph2"))

print("\ndataset.contains_named_graph(\"http://example.org/non-existing\"):\n")
print(dataset.contains_named_graph("http://example.org/non-existing"))

print("\ngraph1.list_triples():\n")
output = io.BytesIO()
serialize(list(graph1.list_triples()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())

print("\nlen(graph1):\n")
print(len(graph1))

print("\nresource1.uri:\n")
print(resource1.uri)

print("\nresource1.id:\n")
print(resource1.id)

print("\nresource1.list_properties():\n")
output = io.BytesIO()
serialize(list(resource1.list_properties()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())

print("\ngraph2.list_subjects():\n")
print(list(graph2.list_subjects()))

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

print("\ngraph3.list_triples():\n")
output = io.BytesIO()
serialize(list(graph3.list_triples()), output, "application/n-triples") # "application/n-quads" should work
print(output.getvalue())