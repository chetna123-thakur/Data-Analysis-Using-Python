import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006,
                 1007, 1008, 1009, 1010, 1011, 1011],
    "Order_Date": [
        "2026-01-05", "2026-01-08", "2026-01-12",
        "2026-01-18", "2026-02-02", "2026-02-10",
        "2026-02-14", "2026-02-20", "2026-03-03",
        "2026-03-12", "2026-03-18", "2026-03-18"
    ],
    "City": [
        "Delhi", "Mumbai", "Delhi", "Chandigarh",
        "Mumbai", "Delhi", "Chandigarh", "Mumbai",
        "Delhi", "Mumbai", None, "Mumbai"
    ],
    "Product": [
        "Laptop", "Phone", "Tablet", "Laptop",
        "Phone", "Tablet", "Laptop", "Phone",
        "Monitor", "Laptop", "Phone", "Phone"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics"
    ],
    "Quantity": [2, 3, 1, 2, 4, 2, 3, 3, 2, 1, 5, 5],
    "Unit_Price": [
        50000, 20000, 15000, 50000, 20000, 15000,
        50000, 20000, 25000, 50000, 20000, 20000
    ]
}

df = pd.DataFrame(data)
#print(df)


#Inspect the dataset ===>

#print(df.shape)
#print(df.info())
#print(df.isnull().sum())
#print("Duplicate rows:", df.duplicated().sum())

#Remove exact duplicate rows ===>

#df = df.drop_duplicates()
#print("Rows after removing duplicates:", len(df))

#Handle the missing city ===>

#df["City"] = df["City"].fillna("Unknown")

#Create a revenue column ==>

df["Revenue"] = df["Quantity"] * df["Unit_Price"]
(df.head())

#Find the best-selling products by revenue

product_revenue = (
    df.groupby("Product")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(product_revenue)

#Create visualizations ===>
#1. Revenue by product

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

