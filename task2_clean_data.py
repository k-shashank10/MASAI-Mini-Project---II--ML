## Task 2: Clean the Dataset for Telecom Company

#Importing Libaraties
import pandas as pd

#1. Load dataset
df = pd.read_csv("/content/churnguard_data.csv")

#2. Drop customerID column:
df = df.drop(columns=["customerID"])

#3. Remove duplicate rows:
df = df.drop_duplicates()

#4. Strip whitespace from gender and PaymentMethod:

df["gender"] = df["gender"].str.strip()
df["PaymentMethod"] = df["PaymentMethod"].str.strip()

#5. Standardisign casing:

for col in ["Churn", "PhoneService", "PaperlessBilling"]:
    df[col] = df[col].str.strip().str.title()

#6. Fixing Contract values:
contract_map = {
    "Month-to-month": "Month-to-Month", "month-to-month": "Month-to-Month", "Monthly": "Month-to-Month", "month to month": "Month-to-Month",
    "1 year": "One Year","One Year": "One Year", "one year": "One Year", "One year": "One Year",
    "Two Year": "Two Year", "two year": "Two Year", "2 year": "Two Year", "Two year": "Two Year",

}
df["Contract"] = df["Contract"].map(contract_map)


#7. Fixing InternetService values
internet_map = {
    "DSL": "DSL", "Dsl": "DSL","DSl": "DSL", "dsl": "DSL",
    "Fiber optic": "Fiber optic","fiber optic": "Fiber optic", "FiberOptic": "Fiber optic","Fibre optic": "Fiber optic",
    "No": "No", "nan": "No", "NO": "No","no": "No", "NaN":"No"

 }
df["InternetService"] = df["InternetService"].map(internet_map)

#8. Convert TotalCharges to numeric (junk → NaN):
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

#9.  Remove rows where tenure ≤ 0:
df = df[df["tenure"] > 0]

#10.  Remove rows where MonthlyCharges < 10 or > 200
df = df[(df["MonthlyCharges"] >= 10) & (df["MonthlyCharges"] <= 200)]

#11.  Fill missing values
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(df["MonthlyCharges"].mean())
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].mean())
df["tenure"] = df["tenure"].fillna(round(df["tenure"].median())).astype(int)

# 12. Printing Data Shape
print("Cleaned shape:", df.shape)
# 13. Checking for Missing Values
print("\nMissing values:")
print(df.isnull().sum())

#14. Cleaning Missing Values in Internet Services:

# Show rows where InternetService is null
print(df[df["InternetService"].isnull()])
#Filling Missing value found in Internet Service Column with "No": 
df["InternetService"] = df["InternetService"].fillna("No")

#15. Printing  final shape:
print("Cleaned shape:", df.shape)

# 16: Confirming missing values resolved
print("\nMissing values after cleaning:")
print(df.isnull().sum())

