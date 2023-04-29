from owlready2 import *
import pandas as pd
import random

onto = get_ontology("http://topicsindatascience.org/team3_ontology")

emi = pd.read_csv("dataset.csv")
alex = pd.read_csv("student_data.csv")
connor = pd.read_csv("student_prediction_DS.csv")




#Modify dataset one

#This dataset transforms 
def df_ocupations_to_fit(value):
    if int(value) > 5:
        return int(5)   
    else: return value
'''

#Modyfi 
dfone["FATHER_JOB"]=dfone["FATHER_JOB"].apply(df_ocupations_to_fit)
dfone["MOTHER_JOB"]=dfone["MOTHER_JOB"].apply(df_ocupations_to_fit)
'''
#For alex dataset


def modify_occ_Alex(value):
    if value == "teacher":
        return 3
    if value == "at_home":
        return 6
    if value == "health":
        return random.randint(3, 5)
    if value == "services":
        return 2
    else:
        return random.randint(3, 5)


def modify_Mocc_Con(value):
    if value == 2:
        return 5

def modify_occ_Emi(value):
    if value == 1:
        return 5
    elif value == 2:
        return 2
    elif value == 3:
        return 3
    elif value == 4:
        return 4
    elif value == 5:
        return 5
    elif value == 6:
        return 3
    elif value == 7:
        return 4
    elif value == 8:
        return 4
    elif value == 9:
        return 3
    elif value == 10:
        return 3
    elif value == 11:
        return 2
    elif value == 12:
        return 5
    elif value == 13:
        return 5
    elif value == 14:
        return 2
    elif value == 15:
        return 2
    elif value == 16:
        return 2
    elif value == 17:
        return 3
    elif value == 18:
        return 3
    elif value == 19:
        return 3
    elif value == 20:
        return 2
    elif value == 21:
        return 2
    elif value == 22:
        return 3
    elif value == 23:
        return 3
    elif value == 24:
        return 2
    elif value == 25:
        return 3
    elif value == 26:
        return 3
    elif value == 27:
        return 3
    elif value == 28:
        return 3
    elif value == 29:
        return 3
    elif value == 30:
        return 3
    elif value == 31:
        return 3
    elif value == 32:
        return 3
    elif value == 33:
        return 2
    elif value == 34:
        return 4
    elif value == 35:
        return 4
    elif value == 36:
        return 4
    elif value == 37:
        return 4
    elif value == 38:
        return 4
    elif value == 39:
        return 4
    elif value == 40:
        return 3
    elif value == 41:
        return 3
    elif value == 42:
        return 3
    elif value == 43:
        return 3
    elif value == 44:
        return 3
    elif value == 45:
        return 3
    else:
        return 5
    

    
    
def modify_GENDER_Alex(value):
    if value == "F":
        return 1
    else:
        return 2

def modify_GENDER_Emi(value):
    if value == 1:
        return 2
    else:
        return 1


def mofdify_grade_alex(value):
    
    if value >= 17:
        return 5
    if value >= 14 and value < 17:
        return 4
    if value >= 11 and value < 14:
        return 3
    if value >= 9 and value < 11:
        return 2
    if value >= 6 and value < 9:
        return 1
    else:
        return 0

def modify_grade_emi(value):

    if value >= 14.5:
        return 5
    if value >= 13.5 and value < 14.5:
        return 4
    if value >= 12.5 and value < 13.5:
        return 3
    if value >= 11.5 and value < 12.5:
        return 2
    if value >= 10.5 and value < 11.5:
        return 1
    else:
        return 0


alex['GENDER']=alex['GENDER'].apply(modify_GENDER_Alex)
emi['GENDER']=emi['GENDER'].apply(modify_GENDER_Emi)
emi['MJOB']=emi['MJOB'].apply(modify_occ_Emi)
emi['FJOB']=emi['FJOB'].apply(modify_occ_Emi)
alex['MJOB']=alex['MJOB'].apply(modify_occ_Alex)
alex['FJOB']=alex['FJOB'].apply(modify_occ_Alex)
connor['MJOB']=connor['MJOB'].apply(modify_Mocc_Con)
emi['GRADE']=emi['GRADE'].apply(modify_grade_emi)
alex['GRADE']=alex['GRADE'].apply(mofdify_grade_alex)

#print(alex)

merged_df = pd.concat([emi, connor, alex])

# Check the merged dataset
#print(merged_df.head())
merged_df.to_csv('Final_Merged_Dataset.csv', index=False)

print(merged_df.head())


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
    
arr = merged_df.values.T.tolist()
j = 1
for i in range(0, 1000):
    individual = Student("individual_"+ str(j))
    individual.GENDER.append(arr[1][i])
    individual.MOTHER_JOB.append(arr[2][i])
    individual.FATHER_JOB.append(arr[3][i])
    individual.GRADE.append(arr[4][i])
    j = j+1
    


onto.save(file="finaldataset.owl")

