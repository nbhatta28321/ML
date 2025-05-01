import pandas as pd

dataSet = pd.read_csv('Walmart.csv')

columns = ["Weekly_Sales","Holiday_Flag","Temperature","Fuel_Price","CPI","Unemployment"]

for column in columns:
    print(f"Mean: {dataSet[column].mean()}")
    print(f"Median: {dataSet[column].median()}")
    print(f"Mode: {dataSet[column].mode()}")


print("hw")