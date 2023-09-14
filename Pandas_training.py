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


#Importing CSV files

iris_data = pd.read_csv('c:/Users/alext/OneDrive/Documents/CodePython/Course excercises/iris.csv')

#explore iris data
iris_data.shape
iris_data.head(5)
iris_data.tail(5)

#checking datatypes
iris_data.dtypes

#loc and iloc
iris_data.loc[2:4]   #indexing starts from zero so you see the data from the position 3,4 &5
iris_data.loc[2:4,'petal_length']  
iris_data.iloc[2:4,2:3]





