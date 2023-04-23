from owlready2 import *
from rdflib import Graph, Namespace

go = get_ontology("mynew.owl").load()

print(list(default_world.sparql("""
           SELECT (COUNT(?x) AS ?nb)
           { ?x a rdfs:domain . }
    """)))