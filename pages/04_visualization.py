import streamlit as st
import pandas as pd
import plotly.express as px

# Title for the page
st.title("Visualization")

# Section: Load Dataframes
st.header("Dataframes")

# Load merged_df
try:
    merged_df = pd.read_csv("merged_df.csv")
    st.success("merged_df loaded successfully!")
except FileNotFoundError:
    st.error("Error: merged_df.csv not found in the current folder!")

# Load highest_sales_products_sorted
try:
    highest_sales_products_sorted = pd.read_csv("highest_sales_products_sorted.csv")
    st.success("highest_sales_products_sorted loaded successfully!")
except FileNotFoundError:
    st.error("Error: highest_sales_products_sorted.csv not found in the current folder!")

# Ensure both dataframes are loaded
if 'merged_df' in locals() and 'highest_sales_products_sorted' in locals():
    st.write("Dataframes are ready for visualization!")

    # Business Question 1: Relationship between Review Score and Delivery Time
    st.subheader("Business Question 1: How does product delivery performance impact customer satisfaction?")
    
    # Filters for Business Question 1
    st.write("Use the filters below to refine the visualization:")
    score_filter = st.multiselect(
        "Select Review Scores to Display",
        options=merged_df['review_score'].unique(),
        default=merged_df['review_score'].unique(),
        help="Select one or more review scores to include in the chart."
    )
    merged_filtered = merged_df[merged_df['review_score'].isin(score_filter)]

    # Interactive Visualization for Business Question 1
    if not merged_filtered.empty:
        fig1 = px.box(
            merged_filtered,
            x='review_score',
            y='delivery_time',
            title='Relationship between Review Score and Delivery Time',
            labels={'review_score': 'Review Score', 'delivery_time': 'Delivery Time (days)'}
        )
        st.plotly_chart(fig1)
    else:
        st.warning("No data available for the selected review scores.")

    # Business Question 2: Total Sales by State and Product Category
    st.subheader("Business Question 2: What are the most profitable regions and product categories?")
    
    # Filters for Business Question 2
    st.write("Use the filters below to refine the visualization:")
    
    # Filter by state
    state_filter = st.multiselect(
        "Select States to Display",
        options=highest_sales_products_sorted['customer_state'].unique(),
        default=highest_sales_products_sorted['customer_state'].unique(),
        help="Select one or more states to include in the chart."
    )
    # Filter by product category
    category_filter = st.multiselect(
        "Select Product Categories to Display",
        options=highest_sales_products_sorted['product_category_name'].unique(),
        default=highest_sales_products_sorted['product_category_name'].unique(),
        help="Select one or more product categories to include in the chart."
    )

    # Apply filters
    sales_filtered = highest_sales_products_sorted[
        (highest_sales_products_sorted['customer_state'].isin(state_filter)) &
        (highest_sales_products_sorted['product_category_name'].isin(category_filter))
    ]

    # Sort options
    sort_by = st.selectbox(
        "Sort by",
        options=["Total Sales (Ascending)", "Total Sales (Descending)"],
        index=1
    )
    ascending = True if sort_by == "Total Sales (Ascending)" else False
    sales_filtered = sales_filtered.sort_values(by='total_sales', ascending=ascending)

    # Interactive Visualization for Business Question 2
    if not sales_filtered.empty:
        fig2 = px.bar(
            sales_filtered,
            x='customer_state',
            y='total_sales',
            color='product_category_name',
            title='Total Sales by State and Product Category',
            labels={'customer_state': 'Customer State', 'total_sales': 'Total Sales', 'product_category_name': 'Product Category'}
        )
        st.plotly_chart(fig2)
    else:
        st.warning("No data available for the selected states and product categories.")
