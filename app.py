from flask import Flask, render_template, request, redirect, Blueprint
from flask_cors import CORS
from owlready2 import *
import pandas as pd

from emilianoQuery import emilianoQuery
from alexQuery import alexQuery


app = Flask(__name__)
app.register_blueprint(emilianoQuery)
app.register_blueprint(alexQuery)


# Load the ontology into an rdflib Graph object


# Define a namespace for your ontology
#MY_ONTOLOGY_NS = Namespace("http://topicsindatascience.org/team3_ontology")

onto = get_ontology("finaldataset.owl").load()

CORS(app)

@app.route("/")
def home():
    return render_template("./home.html")

@app.route("/querySH")
def qs():
    return render_template("./queryPage.html")

@app.route("/ConQue")
def con():
    return render_template("./ConQuery.html")

@app.route("/SergQue")
def serg():
    return render_template("./SergioQuery.html")

@app.route('/query', methods=['GET', 'POST'])
def query():
    gender_map = {"Male": "2", "Female": "1"}
    gpa_map = {"F": ["0", "1"], "D": "2", "C": "3", "B": "4", "A": "5"}

    # Get the values of X and Y from the form
    x = gender_map.get(request.form.get('x'))
    y = gpa_map.get(request.form.get('y'))

    


    print(x)
    

    query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX onto: <http://topicsindatascience.org/team3_ontology#>

        SELECT ?student ?gender ?gpa
        WHERE {
        ?student rdf:type onto:Student .
        ?student onto:GENDER ?gender .
        ?student onto:GRADE ?gpa .
        FILTER(?gender = """ + x + """ && ?gpa >= """ + y + """)
        }
        """ 
    
    print(query)
    #ontologyName = request.form.get("ontologyName")

    

    results = onto.world.sparql(query)
    
    result_list = []
    #print(results)
    for row in results:
        row = [str(cell).replace("finaldataset.", '') for cell in row]
         
        if(row[1] == '1'): row[1] = "Female"
        else: row[1] = "Male"
        if (row[2] == "0"): row[2] = "Grade AVG: F"
        elif(row[2] == '1'): row[2] = "Grade AVG: F"
        elif(row[2] == '2'): row[2] = "Grade AVG: D"
        elif(row[2] == '3'): row[2] = "Grade AVG: C"
        elif(row[2] == '4'): row[2] = "Grade AVG: B"
        else: row[2] = "Grade AVG: A"
        result_list.append(row)
        
    
 
    
    # Render the results in a template using Jinja2
    return render_template('results.html', results=result_list)
