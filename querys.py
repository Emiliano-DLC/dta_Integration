from owlready2 import *

onto = get_ontology("mynew.owl").load()
print(onto.base_iri)

query = """
PREFIX my_owl: <http://utepdataintegration.org/team3_test#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?student
WHERE {
  ?student rdf:type my_owl:Student .
  ?student my_owl:Target ?target .
  ?student my_owl:Marital_status ?mstat .
  Filter (?target = "Dropout")
  Filter (?mstat = 1)
}
"""

results = onto.world.sparql(query)
for r in results:
    for i in r:
        print(i)


'''
  ?student my_owl:Target ?target .
  Filter (?target = "Dropout")
'''