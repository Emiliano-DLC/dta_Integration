from flask import Flask, render_template, redirect, Blueprint, url_for, request
from flask_cors import CORS
from owlready2 import *
import pandas as pd

alexQuery = Blueprint('alexQuery', __name__)

CORS(alexQuery)

onto = get_ontology("finaldataset.owl").load()

@alexQuery.route("/alexQuery")
def alexquery():
    return render_template("./alexQuery.html")

@alexQuery.route('/alex_query', methods=['GET', 'POST'])
def alex_query():

    # Get the value for occupation (X)
    x = request.form.get('occupation')

    query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX onto: <http://topicsindatascience.org/team3_ontology#>

        SELECT ?student ?gender ?fjob ?mjob ?grade
        WHERE {curl1}
            ?student rdf:type onto:Student .
            ?student onto:GENDER ?gender .
            ?student onto:FATHER_JOB ?fjob .
            ?student onto:MOTHER_JOB ?mjob .
            ?student onto:GRADE ?grade .
            FILTER(?mjob = {var1} || ?fjob = {var2})
        {curl2}
        """.format(var1 = x, var2 = float(x), curl1 = "{", curl2 = "}")

    results = onto.world.sparql(query)
    
    result_list = []
    #print(results)
    for row in results:
        row = [str(cell).replace("finaldataset.", '') for cell in row]

        # Gender
        if(row[1] == '1'): row[1] = "Female"
        else: row[1] = "Male"
        
        # Father Occupation
        if (row[2] == "1.0"): row[2] = "Retired"
        elif(row[2] == '2.0'): row[2] = "Government Job"
        elif(row[2] == '3.0'): row[2] = "Private Sector Employee"
        elif(row[2] == '4.0'): row[2] = "Self-employed"
        else: row[2] = "Other"

        # Mother Occupation
        if (row[3] == "1"): row[3] = "Retired"
        elif(row[3] == '2'): row[3] = "Government Job"
        elif(row[3] == '3'): row[3] = "Private Sector Employee"
        elif(row[3] == '4'): row[3] = "Self-employed"
        else: row[3] = "Other"

        # Grade
        if (row[4] == "0"): row[4] = "Grade: F"
        elif(row[4] == '1'): row[4] = "Grade: F"
        elif(row[4] == '2'): row[4] = "Grade: D"
        elif(row[4] == '3'): row[4] = "Grade: C"
        elif(row[4] == '4'): row[4] = "Grade: B"
        else: row[4] = "Grade: A"

        result_list.append(row)

    return render_template('./alex-results.html', results=result_list)
