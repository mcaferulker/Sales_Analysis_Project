import pandas as pd
import matplotlib.pyplot as plt

# Data
sales_df = pd.read_csv("sales_data.csv")

# Convert to DayTime
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# 1. Groupby Category
category_summary = sales_df.groupby("Category").agg(
    Total_Units_Sold=("Units_Sold", "sum"),
    Total_Revenue=("Revenue", "sum")
).sort_values(by="Total_Revenue", ascending=False)

# 2. Monthly Sale and Revenue Trend
sales_df['Month'] = sales_df['Date'].dt.to_period('M')
monthly_trends = sales_df.groupby("Month").agg(
    Total_Units_Sold=("Units_Sold", "sum"),
    Total_Revenue=("Revenue", "sum")
)

# 3. Visualizing
# Revenue by categories (Bar Chart)
category_summary.plot(kind="bar", y="Total_Revenue", legend=False, figsize=(10, 6))
plt.title("Total Revenue by Category")
plt.ylabel("Revenue")
plt.xlabel("Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/category_revenue.png")
plt.show()

# Units by Categories (Bar Chart)
category_summary.plot(kind="bar", y="Total_Units_Sold", legend=False, figsize=(10, 6), color='orange')
plt.title("Total Units Sold by Category")
plt.ylabel("Units")
plt.xlabel("Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/category_units_sold.png")
plt.show()

# Monthly Sale Trend (Line Chart)
monthly_trends.plot(y="Total_Units_Sold", kind="line", marker='o', figsize=(10, 6))
plt.title("Monthly Total Units Sold")
plt.ylabel("Units Sold")
plt.xlabel("Month")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("images/monthly_units_sold.png")
plt.show()

# Monthly Revenue Trend (Line Chart)
monthly_trends.plot(y="Total_Revenue", kind="line", color="orange", marker='o', figsize=(10, 6))
plt.title("Monthly Total Revenue")
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.savefig("images/monthly_revenue.png")
plt.show()