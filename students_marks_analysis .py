import pandas as pd
df = pd.read_csv("students.csv")
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df=df.dropna()
df["Average"] = (df["Math"] + df["Science"] + df["English"]) / 3
print(df)
topper = df.loc[df["Average"].idxmax()]
print("Topper:\n", topper)
low = df.loc[df["Average"].idxmin()]
print("Lowest:\n", low)
print(df.groupby("Gender")["Average"].mean())
print(df[["StudyHours","Average"]])
import matplotlib.pyplot as plt
plt.scatter(df["StudyHours"], df["Average"])
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Study Hours vs Average Marks")
plt.show()
df.groupby("Gender")["Average"].mean().plot(kind="bar")
plt.title("Average Marks by Gender")
plt.show()
df[["Math","Science","English"]].mean().plot(kind="bar")
plt.title("Average Marks by Subject")
plt.show()
df.to_csv("final_output.csv", index=False)
