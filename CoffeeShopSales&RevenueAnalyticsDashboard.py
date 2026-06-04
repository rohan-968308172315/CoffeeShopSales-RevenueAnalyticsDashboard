import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Coffe_sales.csv")

# Basic Information
print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Records:")
print(df.head())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Total Revenue
total_revenue = df["money"].sum()
print("\nTotal Revenue:", round(total_revenue,2))

# Average Sale Value
avg_sale = df["money"].mean()
print("Average Sale Value:", round(avg_sale,2))

# Top Selling Coffee Products
top_products = df.groupby("coffee_name")["money"].sum()
top_products = top_products.sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_products)

# Sales by Time of Day
time_sales = df.groupby("Time_of_Day")["money"].sum()

print("\nTime of Day Revenue:")
print(time_sales)

# Weekday Revenue
weekday_sales = df.groupby("Weekday")["money"].sum()

print("\nWeekday Revenue:")
print(weekday_sales)

# Monthly Revenue
monthly_sales = df.groupby("Month_name")["money"].sum()

print("\nMonthly Revenue:")
print(monthly_sales)

# Payment Method Analysis
payment_method = df["cash_type"].value_counts()

print("\nPayment Method Usage:")
print(payment_method)

# Peak Sales Hours
hourly_sales = df.groupby("hour_of_day")["money"].sum()

print("\nHourly Revenue:")
print(hourly_sales)

# ===============================
# VISUALIZATION SECTION
# ===============================

# Top Products Chart
top_products.plot(
    kind='bar',
    figsize=(10,5)
)

plt.title("Top Selling Coffee Products")
plt.xlabel("Coffee")
plt.ylabel("Revenue")
plt.show()

# Time Of Day Sales
time_sales.plot(
    kind='pie',
    autopct='%1.1f%%',
    figsize=(6,6)
)

plt.title("Revenue by Time of Day")
plt.ylabel("")
plt.show()

# Payment Methods
payment_method.plot(
    kind='bar',
    figsize=(6,4)
)

plt.title("Payment Method Usage")
plt.xlabel("Payment Type")
plt.ylabel("Transactions")
plt.show()

# Hourly Revenue
hourly_sales.plot(
    figsize=(10,5)
)

plt.title("Revenue by Hour")
plt.xlabel("Hour")
plt.ylabel("Revenue")
plt.show()

# Monthly Revenue
monthly_sales.plot(
    kind='bar',
    figsize=(8,4)
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

print("\nAnalysis Completed Successfully.")