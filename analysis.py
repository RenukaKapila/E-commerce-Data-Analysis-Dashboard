from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw_data.csv"
CLEAN_PATH = ROOT / "data" / "cleaned_data.csv"
VISUALS = ROOT / "visuals"

# Load raw data
df = pd.read_csv(DATA_PATH)

# Clean column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Standardize data types and formats
df["order_date"] = pd.to_datetime(df["order_date"])
df["sales_channel"] = df["sales_channel"].str.title()
df["category"] = df["category"].str.title()
df["revenue"] = (
    df["revenue"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)
df["discount_pct"] = df["discount_pct"].fillna(0)
df["region"] = df["region"].fillna("Unknown")
df["inventory_on_hand"] = df["inventory_on_hand"].fillna(df["reorder_level"])

# Feature engineering
df["inventory_status"] = df.apply(
    lambda row: "Low Stock Risk"
    if row["inventory_on_hand"] <= row["reorder_level"] * 1.2
    else "Healthy",
    axis=1,
)
df["month"] = df["order_date"].dt.to_period("M").astype(str)
df["first_purchase_date"] = df.groupby("customer_id")["order_date"].transform("min")
df["customer_tenure_days"] = (df["order_date"] - df["first_purchase_date"]).dt.days
df["is_repeat_customer"] = df["customer_tenure_days"] > 0
df["avg_unit_revenue"] = (df["revenue"] / df["quantity"]).round(2)

# Save cleaned data
df.to_csv(CLEAN_PATH, index=False)

# KPI calculations
total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
total_units = df["quantity"].sum()
average_order_value = df.groupby("order_id")["revenue"].sum().mean()

print("Total revenue:", round(total_revenue, 2))
print("Total orders:", total_orders)
print("Units sold:", total_units)
print("Average order value:", round(average_order_value, 2))

# Aggregations
monthly = df.groupby("month", as_index=False).agg(
    revenue=("revenue", "sum"),
    orders=("order_id", "nunique"),
    units=("quantity", "sum"),
)

category_revenue = (
    df.groupby("category", as_index=False)
    .agg(revenue=("revenue", "sum"))
    .sort_values("revenue", ascending=False)
)

channel_revenue = (
    df.groupby("sales_channel", as_index=False)
    .agg(revenue=("revenue", "sum"))
    .sort_values("revenue", ascending=False)
)

repeat_rate = (
    df.groupby("month")["is_repeat_customer"]
    .mean()
    .reset_index(name="repeat_rate")
)

inventory_status = (
    df.groupby(["category", "inventory_status"])
    .size()
    .unstack(fill_value=0)
)

# Create visuals
VISUALS.mkdir(exist_ok=True)

plt.figure(figsize=(10, 5))
plt.plot(pd.to_datetime(monthly["month"]), monthly["revenue"], marker="o", linewidth=2)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.grid(True, alpha=0.25)
plt.tight_layout()
plt.savefig(VISUALS / "monthly_revenue_trend.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(category_revenue["category"], category_revenue["revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=20)
plt.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig(VISUALS / "revenue_by_category.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(channel_revenue["sales_channel"], channel_revenue["revenue"])
plt.title("Revenue by Sales Channel")
plt.xlabel("Channel")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=20)
plt.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig(VISUALS / "revenue_by_channel.png", dpi=160)
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(pd.to_datetime(repeat_rate["month"]), repeat_rate["repeat_rate"] * 100, marker="o", linewidth=2)
plt.title("Monthly Repeat Customer Rate")
plt.xlabel("Month")
plt.ylabel("Repeat Rate (%)")
plt.grid(True, alpha=0.25)
plt.tight_layout()
plt.savefig(VISUALS / "repeat_customer_rate.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
inventory_status.plot(kind="bar", stacked=True)
plt.title("Inventory Status by Category")
plt.xlabel("Category")
plt.ylabel("Order Lines")
plt.xticks(rotation=20)
plt.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig(VISUALS / "inventory_status_by_category.png", dpi=160)
plt.close()

print("\nTop categories by revenue:")
print(category_revenue)

print("\nRevenue by channel:")
print(channel_revenue)