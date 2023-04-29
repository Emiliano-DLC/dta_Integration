from flask import Flask, render_template, redirect, Blueprint, url_for, request
from flask_cors import CORS
from owlready2 import *
import pandas as pd
import matplotlib.pyplot as plt

sergQuery = Blueprint('sergQuery', __name__)

CORS(sergQuery)

onto = get_ontology("finaldataset.owl").load()

@sergQuery.route("/sergQuery")
def sergQuerys():
    return render_template("./SergQuery.html")

@sergQuery.route('/sergioQuery', methods=['GET', 'POST']) 
def sergioQuery():

    occupations = {"Retired": "1", "Government Job": "2", "Private Sector Employee": "3", "Self-employed": "4", "Other": "5"}
    gpa_map = {"F": "1", "D": "2", "C": "3", "B": "4", "A": "5"}

    # Get the values of X and Y from the form
    x = gpa_map.get(request.form.get('x'))
    y = occupations.get(request.form.get('y'))

    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX onto: <http://topicsindatascience.org/team3_ontology#>
    SELECT ?student ?fjob ?mjob ?gender ?grade 
    WHERE {curl1}
        ?student rdf:type onto:Student .
        ?student onto:GENDER ?gender .
        ?student onto:FATHER_JOB ?fjob .
        ?student onto:MOTHER_JOB ?mjob .
        ?student onto:GRADE ?grade .
        FILTER(?grade >= {var1} && ((?mjob = {var2} || ?fjob = {var2})))
    {curl2}
    """.format(var1 = x, var2 = y, curl1 = "{", curl2 = "}")

    results = onto.world.sparql(query)

    result_list = []

    for row in results:
        row = [str(cell).replace("finaldataset.",'') for cell in row]

        if (row[2] == "1.0"): row[2] = "Retired"
        elif(row[2] == '2.0'): row[2] = "Government Job"
        elif(row[2] == '3.0'): row[2] = "Private Sector Employee"
        elif(row[2] == '4.0'): row[2] = "Self-employed"
        else: row[2] = "Other"

        if (row[3] == "1"): row[3] = "Retired"
        elif(row[3] == '2'): row[3] = "Government Job"
        elif(row[3] == '3'): row[3] = "Private Sector Employee"
        elif(row[3] == '4'): row[3] = "Self-employed"
        else: row[3] = "Other"

        if (row[4] == "0"): row[4] = "Grade: F"
        elif(row[4] == '1'): row[4] = "Grade: F"
        elif(row[4] == '2'): row[4] = "Grade: D"
        elif(row[4] == '3'): row[4] = "Grade: C"
        elif(row[4] == '4'): row[4] = "Grade: B"
        else: row[4] = "Grade: A"

        result_list.append(row)

    return render_template("./sergResults.html", results=result_list)