import streamlit as st

# Title for the page
st.title("Conclusion")

# Introduction
st.markdown(
    """
    ## Overview
    This page summarizes the key insights derived from the analysis of the data. The focus was on understanding 
    the impact of delivery performance on customer satisfaction and regional sales trends.
    """
)

# Business Question 1
st.header("Business Question 1")
st.subheader("How does product delivery performance impact customer satisfaction?")
st.markdown(
    """
    ### Conclusion:
    - Delivery time impacts review scores, with faster deliveries generally receiving higher ratings. 
    - However, even early deliveries receive low scores, suggesting additional factors need further analysis. 
    """
)

# Business Question 2
st.header("Business Question 2")
st.subheader("What are the regional sales trends, and how do they vary by product category?")
st.markdown(
    """
    ### Conclusion:
    - Sales are concentrated in larger states, led by São Paulo, with smaller states showing much lower demand. 
    - Key categories include Beleza_saude, cama_mesa_banho, and relogios_presentes, with localized demand for categories like brinquedos and ferramentas_jardim.
    """
)

# Summary
st.markdown(
    """
    ## Final Thoughts
    The analysis provides actionable insights into delivery performance and regional sales distribution:
    - Businesses could explore factors beyond delivery time to enhance customer satisfaction.
    - Regional disparities in sales highlight opportunities to target underperforming regions with tailored marketing strategies and category-specific promotions.
    """
)
