import pandas as pd

# Load only the relevant columns from customer_details.xlsx
cols_to_use = [
    "Customer Name",
    "ORG_ID",
    "Industry",
    "Product Status",
    "Sum of Annual Revenue",
    "Revenue Range",
    "Total Retailer Connections"
]

# Read only these columns
customer_data = pd.read_excel("customer_details.xlsx", usecols=cols_to_use)

# Show just the first 5 rows for inspection
print(customer_data.head())

# Optional: show summary stats for quick insights
print(customer_data.describe(include="all"))
