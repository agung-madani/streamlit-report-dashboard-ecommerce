import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="E-Commerce Data Analysis",
    page_icon="🛒",
    layout="wide"
)

# --- Introduction Section ---
st.title("🛍️ E-Commerce Public Dataset Analysis")
st.markdown("""
Welcome to the **E-Commerce Data Analysis Project**! This dashboard is built to explore, analyze, and visualize insights 
from a comprehensive e-commerce dataset. Dive in to uncover patterns and trends in customer behavior, product performance, 
order logistics, and more.
""")

# --- Project Information Section ---
st.header("📌 Project Information")
st.markdown("""
- **Project Name**: E-Commerce Data Analysis
- **Analyst**: Agung Rashif Madani  
- **Email**: [agungrashif009@gmail.com](mailto:agungrashif009@gmail.com)  
- **Dicoding ID**: armada
""")

# --- Business Questions Section ---
st.header("📋 Business Questions")
st.markdown("""
This project aims to address critical business questions to guide strategic decisions. Here are the key questions:
1. **How does product delivery performance impact customer satisfaction?**
2. **How does the geographic location of customers influence the popularity of product categories and sales performance in different regions?**
""")

st.info("These questions will be explored in detail through the data visualizations and analyses provided in this dashboard.")

# --- Call to Action ---
st.markdown("### 🚀 Get Started")
st.markdown("Use the navigation sidebar to explore different sections of the dashboard.")



