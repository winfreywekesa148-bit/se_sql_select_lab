# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("Employee Data:")
print(employee_data)

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn).head()
print("Employees:")
print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn).head()
print("Employees in Order:")
print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT employeeNumber AS ID, lastName FROM employees""", conn).head()
print(df_alias)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
                           SELECT first_name, last_name, jobTitle, 
                           CASE WHEN jobTitle LIKE '%President%' THEN 'Executive'
                           WHEN jobTitle LIKE '%VP Sales%' THEN 'Executive'
                           WHEN jobTitle LIKE '%VP Marketing%' THEN 'Executive'
                           ELSE 'Not Executive' END AS role
                            FROM employees
                           '""", conn)
print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT last_name, LENGTH(last_name) AS name_length FROM employees""", conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT substr(jobTitle, 1, 2) AS short_title FROM employees """, conn)

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""SELECT SUM(priceEach * quantityOrdered) AS total_price FROM orderDetails""", conn).sum()

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""SELECT orderNumber, orderDate, strftime('%d', orderDate) AS day, strftime('%m', orderDate) AS month, strftime('%Y', orderDate) AS year FROM orders""", conn)

conn.close()