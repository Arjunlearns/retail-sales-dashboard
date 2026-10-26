
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# 1. Page configuration
# -------------------------------
st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Analytics Dashboard")
st.caption("Online Retail Dataset | December 2010 – December 2011")

# -------------------------------
# 2. Load the exported dataset
# -------------------------------
@st.cache_data
def load_data():
    data = pd.read_csv("retail_sales_cleaned.csv")

    data["InvoiceDate"] = pd.to_datetime(
    data["InvoiceDate"],
    dayfirst=True
)
    data["Revenue"] = data["Quantity"] * data["UnitPrice"]
    data["Month"] = data["InvoiceDate"].dt.to_period("M").astype(str)

    return data


df = load_data()

# -------------------------------
# 3. Sidebar filters
# -------------------------------
st.sidebar.header("Dashboard Filters")

countries = sorted(df["Country"].dropna().unique())

selected_countries = st.sidebar.multiselect(
    "Select countries",
    countries,
    default=countries
)

filtered_df = df[df["Country"].isin(selected_countries)].copy()

# -------------------------------
# 4. Key performance indicators
# -------------------------------
total_revenue = filtered_df["Revenue"].sum()
total_units = filtered_df["Quantity"].sum()
total_invoices = filtered_df["InvoiceNo"].nunique()
total_customers = filtered_df["CustomerID"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Positive Sales Revenue", f"£{total_revenue:,.2f}")
col2.metric("Units Sold", f"{total_units:,.0f}")
col3.metric("Unique Invoices", f"{total_invoices:,}")
col4.metric("Identified Customers", f"{total_customers:,}")

st.divider()

# -------------------------------
# 5. Monthly sales trend
# -------------------------------
st.subheader("Monthly Sales Revenue")

monthly_sales = (
    filtered_df.groupby("Month", as_index=False)["Revenue"]
    .sum()
    .sort_values("Month")
)

fig_monthly = px.line(
    monthly_sales,
    x="Month",
    y="Revenue",
    markers=True,
    title="Revenue by Month"
)

fig_monthly.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue (£)"
)

st.plotly_chart(fig_monthly, use_container_width=True)

# -------------------------------
# 6. Top products
# -------------------------------
st.subheader("Top 10 Products by Revenue")

top_products = (
    filtered_df.groupby("Description")["Revenue"]
    .sum()
    .nlargest(10)
    .sort_values()
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="Revenue",
    y="Description",
    orientation="h",
    title="Highest-Revenue Product Descriptions"
)

st.plotly_chart(fig_products, use_container_width=True)

# -------------------------------
# 7. Country performance
# -------------------------------
st.subheader("Top 10 Countries by Revenue")

country_sales = (
    filtered_df.groupby("Country")["Revenue"]
    .sum()
    .nlargest(10)
    .sort_values()
    .reset_index()
)

fig_countries = px.bar(
    country_sales,
    x="Revenue",
    y="Country",
    orientation="h",
    title="Revenue by Country"
)

st.plotly_chart(fig_countries, use_container_width=True)

# -------------------------------
# 8. Top customers
# -------------------------------
st.subheader("Top 10 Customers by Revenue")

customer_sales = (
    filtered_df.dropna(subset=["CustomerID"])
    .groupby("CustomerID")["Revenue"]
    .sum()
    .nlargest(10)
    .sort_values()
    .reset_index()
)

customer_sales["CustomerID"] = (
    customer_sales["CustomerID"].astype(int).astype(str)
)

fig_customers = px.bar(
    customer_sales,
    x="Revenue",
    y="CustomerID",
    orientation="h",
    title="Highest-Spending Identified Customers"
)

st.plotly_chart(fig_customers, use_container_width=True)

# -------------------------------
# 9. Preview the data
# -------------------------------
with st.expander("View transaction data"):
    st.dataframe(filtered_df, use_container_width=True)

st.caption(
    "Revenue represents positive-sales records only. "
    "Returns, cancellations, and non-positive-price records "
    "were excluded during the original analysis."
)
