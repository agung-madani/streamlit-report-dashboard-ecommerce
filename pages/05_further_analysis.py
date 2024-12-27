import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Title for the page
st.title("Further Analysis")

# Section: Load Dataframe
st.header("Dataframe")

# Load merged_df
try:
    merged_df = pd.read_csv("merged_df.csv", parse_dates=['order_delivered_customer_date', 'order_estimated_delivery_date'])
    st.success("merged_df loaded successfully!")
except FileNotFoundError:
    st.error("Error: merged_df.csv not found in the current folder!")

# Proceed only if the dataframe is loaded
if 'merged_df' in locals():
    st.write("Dataframe is ready for further analysis.")

    # Filter low-score reviews (<= 3)
    low_score_delays = merged_df[merged_df['review_score'] <= 3].copy()

    # Calculate delivery delay
    low_score_delays['delivery_delay'] = (low_score_delays['order_delivered_customer_date'] - 
                                          low_score_delays['order_estimated_delivery_date']).dt.days

    # Analysis of delays for low-scoring deliveries
    st.subheader("Analysis of Delays for Low-Scoring Deliveries")
    delay_stats = low_score_delays.groupby('order_status')['delivery_delay'].describe()
    st.write("**Statistics for Delivery Delays:**")
    st.table(delay_stats)

    # Insights
    st.markdown("### Insights:")
    st.markdown(
        "- The mean delivery delay is approximately **-7.35 days**, indicating that deliveries are often completed earlier than expected.\n"
        "- **75% of deliveries** are made **1 day earlier** or more."
    )

    # Interactive Histogram for Delivery Delays
    st.subheader("Distribution of Delivery Delays for Low-Scoring Deliveries")
    delay_range = st.slider(
        "Select Range of Delivery Delays (days):",
        int(low_score_delays['delivery_delay'].min()),
        int(low_score_delays['delivery_delay'].max()),
        (-20, 20)
    )
    filtered_delays = low_score_delays[
        (low_score_delays['delivery_delay'] >= delay_range[0]) &
        (low_score_delays['delivery_delay'] <= delay_range[1])
    ]

    if not filtered_delays.empty:
        fig = px.histogram(
            filtered_delays,
            x='delivery_delay',
            nbins=30,
            title='Distribution of Delivery Delays for Low-Scoring Deliveries',
            labels={'delivery_delay': 'Delivery Delay (days)'},
            marginal="box",
            template="plotly_white"
        )
        st.plotly_chart(fig)
    else:
        st.warning("No data available for the selected range of delivery delays.")
