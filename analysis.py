import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("tips.csv")

print("First rows:")
print(df.head())

print("\nAverage total bill:")
print(df["total_bill"].mean())

print("\nAverage tip per day:")
print(df.groupby("day")["tip"].mean())

# Graph
df.groupby("day")["tip"].mean().plot(kind="bar")
plt.title("Average Tip per Day")
plt.ylabel("Tip Amount")
plt.xlabel("Day")
plt.show()