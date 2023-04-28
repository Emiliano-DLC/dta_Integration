from owlready2 import *
import pandas as pd

df = pd.read_csv("finalCSV.csv")
df["GRADE"] = df["GRADE"].astype(int)

arr = df.values.T.tolist()
print(df)

#Custom URI
onto = get_ontology("http://utepdataintegration.org/team3_test")

#Entities
class Student(Thing):
    namespace = onto


#What valued does the user has
class MOTHER_JOB(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class FATHER_JOB(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class GENDER(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class GRADE(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class Pstatus(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class STUDENTID(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    
class CUML_GPA(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]

class school(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]

    
class Medu(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]

class Fedu(DataProperty):
    namespace = onto
    domain = [Student]
    range = [int]
    

j = 1

for i in range(0, 20):
    individual = Student("individual_"+ str(j))
    individual.MOTHER_JOB.append(arr[1][i])
    individual.FATHER_JOB.append(arr[2][i])
    individual.GENDER.append(arr[3][i])
    individual.GRADE.append(arr[6][i])
    j = j+1
    print("----")


onto.save(file="finaldataset.owl")


"""
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
"""