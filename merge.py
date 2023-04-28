from owlready2 import *
import pandas as pd

onto = get_ontology("http://utepdataintegration.org/team3_test")

dfone = pd.read_csv("dataset.csv")
dftwo = pd.read_csv("student.csv")
dfthree = pd.read_csv("student_prediction_DS.csv")

#-----------


#Modify dataset one

#This dataset transforms 
def df_ocupations_to_fit(value):
    if int(value) > 5:
        return int(5)   
    else: return value

#Modyfi 
dfone["FATHER_JOB"]=dfone["FATHER_JOB"].apply(df_ocupations_to_fit)
dfone["MOTHER_JOB"]=dfone["MOTHER_JOB"].apply(df_ocupations_to_fit)

#For alex dataset
def modify_value(value):
    if value == "teacher":
        return 1
    if value == "at_home":
        return 4
    if value == "health":
        return 3
    if value == "services":
        return 2
    else:
        return 5
    
def modify_GENDER(value):
    if value == "F":
        return 2
    else:
        return 1
    

dftwo = pd.read_csv("student.csv")
dftwo['FATHER_JOB']=dftwo['FATHER_JOB'].apply(modify_value)
dftwo['MOTHER_JOB']=dftwo['MOTHER_JOB'].apply(modify_value)
dftwo['GENDER']=dftwo['GENDER'].apply(modify_GENDER)


dftwo.merge(dfthree)
print(dfone)
dfone.merge(dftwo)
dfone.to_csv("finalCSV.csv")
print(dfone)

j = 0
for i in dfone:
    print(i)
    print(j)
    j = j+1

arr = dfone.values.T.tolist()
#_---_______________________________________________

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
    


for i in range(0, 20):
    individual = Student("individual_"+ str(j))
    individual.MOTHER_JOB.append(arr[i][0])
    individual.FATHER_JOB.append(arr[i][1])
    individual.GENDER.append(arr[i][2])
    individual.GRADE.append(arr[i][5])
    j = j+1
    print("----")


onto.save(file="finaldataset.owl")

#Custom URI
onto = get_ontology("http://utepdataintegration.org/team3_dataset")
