from owlready2 import *
import pandas as pd

df = pd.read_csv("student_prediction_DS.csv")
arr = df.values.T.tolist()

onto = get_ontology("http://topicsindatascience.org/team3_ontology")

class Student(Thing):
    namespace = onto



    
class Mother_occupation(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Father_occupation(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    

    
class Gender(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]


class Grade(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]

class CumGpa(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]


j = 1

for i in range(0,145):
    individual = Student("Student"+ str(j))
    individual.Gender.append(arr[1][i])
    individual.Father_occupation.append(arr[2][i])
    individual.Mother_occupation.append(arr[3][i])
    individual.Grade.append(arr[4][i])
    individual.CumGpa.append(arr[5][i])
    j += 1

print(individual.Gender)

 
onto.save(file="Connor_Onto.owl")
