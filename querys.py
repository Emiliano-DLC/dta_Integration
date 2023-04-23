from owlready2 import *

onto = get_ontology("mynew.owl").load()
print(onto.base_iri)

query = """
PREFIX my_owl: <http://utepdataintegration.org/team3_test#>
SELECT ?student
WHERE {
  ?student rdf:type my_owl:Student .
}
"""

results = onto.world.sparql(query)
for r in results:
    for i in r:
        print(i)