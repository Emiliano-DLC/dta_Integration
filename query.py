from flask import Flask, render_template, redirect, Blueprint, url_for, request
from flask_cors import CORS
from owlready2 import *
import pandas as pd

query = Blueprint('query', __name__)

CORS(query)

@query.route('/emiliano_query', methods=["POST"])
def emiQuery():

  query = request.form.get("queryInput")
  ontologyName = request.form.get("ontologyName")

  onto = get_ontology(ontologyName).load()

  results = onto.world.sparql(query)
  arr = []
  
  for i in results:
    for r in i:
      arr.append(r)
  return render_template("./emiQuery.html", qResult=arr)
