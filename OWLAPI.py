from owlready2 import *
import pandas as pd

df = pd.read_json("dataset.json")
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

class FirstSemGrade(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]

class SecSemGrade(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]

j = 1

for i in range(0, 50):
    individual = Student("individual_"+ str(j))
    individual.Marital_status.append(arr[0][i])
    individual.Course.append(arr[1][i])
    individual.Nacionality.append(arr[2][i])
    individual.Mother_qualification.append(arr[3][i])
    individual.Father_qualification.append(arr[4][i])
    individual.Mother_occupation.append(arr[5][i])
    individual.Father_occupation.append(arr[6][i])
    individual.Displaced.append(arr[7][i])
    individual.Gender.append(arr[9][i])
    individual.Scholarship_holder.append(arr[10][i])
    individual.International.append(arr[12][i])
    individual.Target.append(arr[15][i])
    individual.SecSemGrade.append(arr[14][i])
    individual.FirstSemGrade.append(arr[13][i])
    j = j+1


onto.save(file="mynew.owl")