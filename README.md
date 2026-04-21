# ADAY Data Analysis Internship Portfolio Project

## Project Overview

This project is a portfolio-style **e-commerce data analysis case study** built to match the kind of work described in the **ADAY Data Analysis Intern** posting. The analysis focuses on sales, inventory, and customer behavior and turns raw business data into clear insights and recommendations.

The project uses a **synthetic dataset** that was created for demonstration purposes. It is not company data, but it is structured to reflect realistic business questions a direct-to-consumer brand might ask.

## Business Objective

Use sales, inventory, and customer-level data to answer practical business questions such as:

- Which product categories drive the most revenue?
- Which channels perform best?
- How does revenue change over time?
- How much of the business comes from repeat customers?
- Which areas show signs of low-stock risk?

## Tools Used

- Python
- pandas
- matplotlib
- Excel
- Jupyter Notebook

## Project Structure

```text
aday_data_analysis_project/
│
├── README.md
├── requirements.txt
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── notebooks/
│   └── ecommerce_analysis.ipynb
├── scripts/
│   └── analysis.py
├── visuals/
│   ├── monthly_revenue_trend.png
│   ├── revenue_by_category.png
│   ├── revenue_by_channel.png
│   ├── repeat_customer_rate.png
│   └── inventory_status_by_category.png
└── dashboard/
    └── excel_dashboard.xlsx
```

## Dataset Description

The dataset includes the following business fields:

- order_id
- order_date
- customer_id
- customer_segment
- sales_channel
- region
- product_id
- category
- product_name
- unit_price
- quantity
- discount_pct
- revenue
- inventory_on_hand
- reorder_level

The cleaned dataset also includes:

- inventory_status
- month
- first_purchase_date
- customer_tenure_days
- is_repeat_customer
- avg_unit_revenue

## Cleaning Steps

The raw file intentionally includes a few realistic data quality issues, including:

- inconsistent text formatting
- missing values
- mixed revenue formatting
- inconsistent channel/category capitalization

Cleaning steps performed in the notebook and script:

1. standardize column names
2. convert dates into datetime format
3. clean revenue values into numeric format
4. fill missing discount values with 0
5. fill missing region values with `"Unknown"`
6. create inventory and repeat-customer features for analysis

## Key Findings

- **Total revenue:** $342,950.85
- **Total orders:** 1,250
- **Units sold:** 2,966
- **Average order value:** $274.36
- **Repeat-customer revenue share:** 68.0%

### Main insights

1. **Outerwear generated the most revenue**, followed by Dresses.
2. **Web was the highest-revenue channel**, with Mobile App as the second strongest contributor.
3. **Repeat-customer contribution increased over time**, showing that retention became more important as the year progressed.
4. **Some products and categories showed low-stock risk**, suggesting that inventory planning should be reviewed for higher-demand items.
5. **Category performance was not evenly distributed**, which means marketing and inventory decisions should be more targeted by product group.

## Business Recommendations

- Increase visibility and inventory planning for high-performing categories like Outerwear and Dresses.
- Review retention campaigns for repeat customers because they contribute a large share of revenue.
- Use channel-specific analysis to allocate marketing budget more efficiently.
- Monitor low-stock-risk items earlier to prevent lost sales.
- Build a lightweight dashboard that sales, operations, and marketing teams can use weekly.

## Visuals

### Monthly Revenue Trend
![Monthly Revenue Trend](visuals/monthly_revenue_trend.png)

### Revenue by Category
![Revenue by Category](visuals/revenue_by_category.png)

### Revenue by Channel
![Revenue by Channel](visuals/revenue_by_channel.png)

### Repeat Customer Rate
![Repeat Customer Rate](visuals/repeat_customer_rate.png)

### Inventory Status by Category
![Inventory Status by Category](visuals/inventory_status_by_category.png)

## How to Run

1. Clone the repository
2. Install dependencies
3. Open the notebook or run the script

```bash
pip install -r requirements.txt
python scripts/analysis.py
```

## Resume-Ready Project Description

Analyzed synthetic e-commerce sales, inventory, and customer data using Python, pandas, matplotlib, and Excel. Cleaned messy business data, built visual reports, identified revenue and retention trends, and developed recommendations to support data-driven decisions across operations, marketing, and inventory planning.

## Notes

This is a portfolio project created to demonstrate business analysis skills relevant to a remote data analysis internship.
