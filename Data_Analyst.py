import pandas as pd


data_dict = {
    "Patient ID": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P003"],
    "Age": [45, 67, 34, 78, 54, 23, None, 36, 62, 41, 34],
    "Diagnosis": ["Flu", "Pneumonia", "Fracture", "COVID-19", "Heart Disease", "Flu", "Pneumonia", "Fracture", "COVID-19", "Heart Disease", "Fracture"],
    "Length of Stay": [3, 7, 2, 14, 10, 5, 8, None, 12, 6, 2],
    "Hospital Department": ["Emergency", "General Medicine", "Orthopedics", "Cardiology", "Orthopedics", "Emergency", "General Medicine", "Orthopedics", "Cardiology", "General Medicine", "Orthopedics"],
}


df = pd.DataFrame(data_dict)


df_cleaned = df.drop_duplicates()

df_cleaned["Age"] = df_cleaned["Age"].fillna(df_cleaned["Age"].mean())
df_cleaned["Length of Stay"] = df_cleaned["Length of Stay"].fillna(df_cleaned["Length of Stay"].mean())


statistics = {
    "Mean Age": df_cleaned["Age"].mean(),
    "Median Age": df_cleaned["Age"].median(),
    "Standard Deviation (Age)": df_cleaned["Age"].std(),
    "Mean Length of Stay": df_cleaned["Length of Stay"].mean(),
    "Median Length of Stay": df_cleaned["Length of Stay"].median(),
    "Standard Deviation (Length of Stay)": df_cleaned["Length of Stay"].std(),
}

stats_summary = pd.DataFrame(
    list(statistics.items()),
    columns=["Metric", "Value"]
)

print("Cleaned Dataset:")
print(df_cleaned)
print("\nStatistical Analysis Summary:")
print(stats_summary)
