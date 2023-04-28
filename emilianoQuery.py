from flask import Flask, render_template, redirect, Blueprint, url_for, request
from flask_cors import CORS
from owlready2 import *
import pandas as pd
import matplotlib.pyplot as plt

emilianoQuery = Blueprint('emilianoQuery', __name__)

CORS(emilianoQuery)

onto = get_ontology("finaldataset.owl").load()

@emilianoQuery.route("/EmiQue")
def emi():
    return render_template("./emiQuery.html")

@emilianoQuery.route('/EmiQueRes', methods=['GET', 'POST'])
def emiQuery():
    gender_map = {"Male": "2", "Female": "1"}
    gpa_map = {"F": "1", "D": "2", "C": "3", "B": "4", "A": "5"}

    # Get the values of X and Y from the form
    x = gender_map.get(request.form.get('gender'))
    y = gpa_map.get(request.form.get('GPA'))

    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX onto: <http://topicsindatascience.org/team3_ontology#>

    SELECT ?student ?fjob ?mjob ?gender ?grade 
    WHERE {curl1}
        ?student rdf:type onto:Student .
        ?student onto:FATHER_JOB ?fjob .
        ?student onto:MOTHER_JOB ?mjob .
        ?student onto:GENDER ?gender .
        ?student onto:GRADE ?grade .
        FILTER(?gender = {var1} && ?grade = {var2})
    {curl2}
    """.format(var1 = x, var2 = y, curl1 = "{", curl2 = "}")

    results = onto.world.sparql(query)

    result_list, fjob, mjob, frecurence, mrecurence = [], [], [], [], []

    for row in results:
        result_list.append([str(cell).replace("finaldataset.", '') for cell in row])

    
    for individual in result_list:
        fjob.append(int(float(individual[1])))
        mjob.append(int(individual[2]))
    
    for req in range(1, 6):
        frecurence.append(fjob.count(req))
        mrecurence.append(mjob.count(req))

    #Data vizualisation
    subjects = ["Retired", "Government Officers", "Private Sector", "Self-Employee", "Other"]
    df = pd.DataFrame({"Father Job":frecurence, "Mother Job":mrecurence}, index=subjects)

    ax = df.plot(kind='bar', figsize=(10, 6), rot=0, title='Query Result', ylabel='Students')
    plt.savefig('static/emilianoQuestion.png')



    return render_template("./emiQueryResult.html", gender = request.form.get('gender'), gpa = request.form.get('GPA'))
