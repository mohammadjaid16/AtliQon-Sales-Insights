

# AtliQon Sales Insights

An interactive BI dashboard built on Databricks AI/BI that delivers a 360-degree view of AtliQon's sales performance across customers, products, markets, and time. The dashboard transforms raw transactional data into actionable insights through KPI counters, trend analysis, top-N rankings, and cross-dimensional breakdowns.

## What's Inside

The dashboard is organized into four focused pages, each addressing a different business question:

### 1. Sales Overview
The command center for sales performance. It opens with four KPI counters — total revenue, customer count, product count, and total quantity sold — followed by a full breakdown of sales by market, division, channel, and platform. A monthly trend line reveals how revenue moves over time, while two bar charts highlight the top 10 customers and top 10 products by revenue. A detailed data table at the bottom provides row-level drill-down for any of these dimensions.

### 2. Product Performance
Dedicated to understanding what's selling. KPI counters show total SKUs, average product price, and category count. A bar chart ranks the top 15 products by revenue, and a pivot matrix compares division performance across quarters. A category mix pie chart shows the revenue split across all product categories, while two tables provide product-level and market-level detail.

### 3. Customer Analytics
Focused on who's buying and where. KPI counters cover total customers, average revenue per customer, top market revenue, and active market count. A bar chart ranks the top 20 customers by revenue, and a distribution chart shows how many customers operate in each market. A pivot matrix breaks down revenue by channel and market, and a detail table provides full customer-level analysis.

### 4. Time & Trends
Built for temporal analysis. KPI counters summarize total revenue, average monthly revenue, peak quarter revenue, and active months. The page features monthly and quarterly trend lines, year-over-year bar comparisons, and a monthly quantity trend for volume analysis. A pivot matrix compares division performance across quarters, and two detail tables provide month-level granularity. A multi-category growth trajectory chart tracks the top 5 product categories over time.

## Global Filters

Ten dashboard-wide filters are available on every page, allowing users to slice data by:

- Year
- Market
- Division
- Channel
- Date Range
- Category
- Product
- Customer
- Quarter
- Platform

## Data Architecture

### Source

All data is sourced from `fmcg.gold.vw_fact_orders_enriched`, a Unity Catalog view stored in Delta Lake format on Databricks. The view contains enriched sales transaction data with the following schema:

| Column | Type | Description |
| --- | --- | --- |
| `date` | date | Transaction date |
| `product_code` | string | Unique product identifier |
| `customer_code` | string | Unique customer identifier |
| `date_key` | integer | Numeric date key |
| `year` | integer | Year extracted from date |
| `month_name` | string | Full month name |
| `month_short_name` | string | Abbreviated month name |
| `quarter` | string | Quarter (Q1–Q4) |
| `year_quarter` | string | Year + quarter combined |
| `customer` | string | Customer name |
| `market` | string | Geographic market |
| `platform` | string | Sales platform |
| `channel` | string | Sales channel |
| `division` | string | Business division |
| `category` | string | Product category |
| `product` | string | Product name |
| `variant` | string | Product variant |
| `sold_quantity` | integer | Units sold |
| `price_inr` | integer | Unit price in INR |
| `total_amount_inr` | integer | Total revenue in INR |

### Datasets

The dashboard uses a combination of a local metric view and pre-aggregated SQL datasets:

* **Main Dataset** — Local metric view on the source table, exposing all columns as dimensions with a `COUNT(*)` measure
* **Top 10 / 20 Customers** — Pre-ranked SQL datasets for customer bar charts
* **Top 10 / 15 Products** — Pre-ranked SQL datasets for product bar charts
* **Top 5 Categories** — Pre-ranked SQL dataset for the category bar chart
* **Top 5 Categories Monthly Trends** — CTE-based SQL dataset joining top categories to monthly aggregations for the growth trajectory line chart
* **Top 10 Divisions Monthly Revenue** — CTE-based SQL dataset joining top divisions to monthly aggregations for the pivot matrix
* **Sales Trend with Moving Average** — Window-function SQL dataset computing monthly revenue with a 3-month moving average for trend analysis

### Semantic Model

All datasets are registered as entities in a Databricks semantic model, enabling entity-qualified queries across the dashboard without manual joins.

## Technology Stack

* **Platform:** Databricks AI/BI Dashboards
* **Data Storage:** Delta Lake (Unity Catalog)
* **Query Engine:** Databricks SQL Warehouse
* **Data Modeling:** Local metric views + SQL datasets with semantic model
* **Visualization:** Bar, line, pie, pivot, counter, table, and filter widgets

## Key Design Decisions

* **Top-N Pattern:** Pre-aggregated SQL datasets with `ORDER BY ... LIMIT N` power ranking visuals, avoiding unreliable widget-level sorting
* **Null Exclusion:** All chart queries include `IS NOT NULL` filters on key dimensions and measures to ensure clean, consistent visualizations
* **Global Filters:** Ten multi-select and date-range filters apply across all pages, enabling cross-dimensional exploration without page-by-page configuration
* **Moving Average Trend:** A window-function-based dataset provides a smoothed 3-month moving average alongside actual sales for trend identification
