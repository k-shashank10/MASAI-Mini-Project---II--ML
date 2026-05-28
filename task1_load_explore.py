#Importing libraries
import pandas as pd

#1. Reading data provided for Task
df=pd.read_csv("/content/churnguard_data.csv")

#2. Print the shape (rows, columns)
print("Shape:", df.shape)

#3. Print the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

#4. Print column names and data types
print("\nColumn info:")
print(df.info())

#5. Print count of missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())

#6. Print number of duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

#7. Print value counts of the Churn column
print("\nChurn value counts:")
print(df['Churn'].value_counts())

#8. Print unique values in the Contract column
print("\nUnique Contract values:")
print(df['Contract'].unique())
