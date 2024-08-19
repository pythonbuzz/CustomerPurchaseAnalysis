import numpy as np
import csv

# Load data from 'customer_purchases.csv' into a structured NumPy array
data = np.genfromtxt('customer_purchases.csv', delimiter=',', dtype=None, encoding=None, names=True)

# Find the unique customer IDs in the data
unique_customers = np.unique(data['CustomerID'])

# Create a dictionary to store the total amount spent by each customer
total_spent_by_customers = {}

# Loop over each unique customer and calculate the total amount they spent
for customer in unique_customers:
    total_spent_by_customers[customer] = np.sum(data[data['CustomerID'] == customer]['AmountSpent'])

# Find the unique dates in the data
unique_dates = np.unique(data['Date'])

# Create an array to store the total sales for each day
daily_sales = np.zeros(unique_dates.size)

# Loop over each unique date and calculate the total sales for that day
for i, date in enumerate(unique_dates):
    daily_sales[i] = np.sum(data[data['Date'] == date]['AmountSpent'])

# Find the index of the day with the highest sales
max_sales = np.argmax(daily_sales)

# Identify the date corresponding to the highest sales
highest_sales_day = unique_dates[max_sales]

# Open a new CSV file 'purchase_analysis.csv' for writing the results
with open('purchase_analysis.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the total amount spent by each customer
    writer.writerow(['CustomerId', 'TotalAmountSpent'])
    for id, total in total_spent_by_customers.items():
        writer.writerow([id, total])
    
    # Add an empty row for separation
    writer.writerow([])
    
    # Write the total sales for each day
    writer.writerow(['Date', 'TotalSales'])
    for date, sales in zip(unique_dates, daily_sales):
        writer.writerow([date, sales])
    
    # Add an empty row for separation
    writer.writerow([])
    
    # Write the date with the highest sales and the total sales for that day
    writer.writerow(['HighestSalesDay', 'TotalSales'])
    writer.writerow([highest_sales_day, daily_sales[max_sales]])
