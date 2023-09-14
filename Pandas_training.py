import pandas as pd


#Pandas - Transform, Clean, visualize, extract insights
#Data Stored in tabular format - Data frame in the form of rows and columns

#Data Types:
#Dictionary stores python structure in the form of key value pairs

teachers = {"Name":['Alex','Ajuna','Louis', 'farzaneh'],
          "city":['Glostrup','Gladsaxe','Amager', 'Copenhagen'],
          "Distance(km)":[20,25,30,35]
         }

print(teachers)
df_teachers = pd.DataFrame(teachers)
print(df_teachers)

#Question: Who all are living at a distance > 20 KM?

print(df_teachers[df_teachers['Distance(km)']>20]['Name'])







