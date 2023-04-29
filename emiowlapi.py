from owlready2 import *
import pandas as pd

df = pd.read_json("dataset.csv-WSP2WS7.json")
arr = df.values.T.tolist()

#Custom URI
onto = get_ontology("http://utepdataintegration.org/team3_test")

#Entities
class Student(Thing):
    namespace = onto


#What valued does the user has
class Marital_status(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Course(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Nacionality(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Mother_qualification(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Father_qualification(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Mother_occupation(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Father_occupation(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Displaced(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Gender(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Scholarship_holder(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class International(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Target(DataProperty):
    namespace = onto
    domain = [Student]
    range = [str]

j = 1
'''
for i in range(0, 50):
    individual = Student("individual_"+ str(j))
    individual.Marital_status.append(arr[0][i])
    individual.Course.append(arr[3][i])
    individual.Nacionality.append(arr[5][i])
    individual.Mother_qualification.append(arr[6][i])
    individual.Father_qualification.append(arr[7][i])
    individual.Mother_occupation.append(arr[8][i])
    individual.Father_occupation.append(arr[9][i])
    individual.Displaced.append(arr[10][i])
    individual.Gender.append(arr[12][i])
    individual.Scholarship_holder.append(arr[13][i])
    individual.International.append(arr[15][i])
    individual.Target.append(arr[16][i])
    j = j+1


onto.save(file="mynew.owl")'''