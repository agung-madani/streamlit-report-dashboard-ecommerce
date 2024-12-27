import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Data Wrangling",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Data Wrangling")
st.markdown("This section covers the steps taken to prepare the data for analysis.")

# --- Gathering Data ---
st.header("📂 Gathering Data")
st.markdown("Data was collected from multiple CSV files provided as part of the dataset. Below are samples from each dataset:")

# Orders Dataset
st.subheader("📦 Orders Dataset")
orders_data = {
    "order_id": ["e481f51cbdc54678b7cc49136f2d6af7", "53cdb2fc8bc7dce0b6741e2150273451", "47770eb9100c2d0c44946d9cf07ec65d"],
    "customer_id": ["9ef432eb6251297304e76186b10a928d", "b0830fb4747a6c6d20dea0b8c802d7ef", "41ce2a54c0b03bf3443c3d931a367089"],
    "order_status": ["delivered", "delivered", "delivered"],
    "order_purchase_timestamp": ["2017-10-02 10:56:33", "2018-07-24 20:41:37", "2018-08-08 08:38:49"],
    "order_approved_at": ["2017-10-02 11:07:15", "2018-07-26 03:24:27", "2018-08-08 08:55:23"],
    "order_delivered_carrier_date": ["2017-10-04 19:55:00", "2018-07-26 14:31:00", "2018-08-08 13:50:00"],
    "order_delivered_customer_date": ["2017-10-10 21:25:13", "2018-08-07 15:27:45", "2018-08-17 18:06:29"],
    "order_estimated_delivery_date": ["2017-10-18 00:00:00", "2018-08-13 00:00:00", "2018-09-04 00:00:00"]
}
st.dataframe(pd.DataFrame(orders_data))

# Order Reviews Dataset
st.subheader("⭐ Order Reviews Dataset")
reviews_data = {
    "review_id": ["7bc2406110b926393aa56f80a40eba40", "80e641a11e56f04c1ad469d5645fdfde", "228ce5500dc1d8e020d8d1322874b6f0"],
    "order_id": ["73fc7af87114b39712e6da79b0a377eb", "a548910a1c6147796b98fdf73dbeba33", "f9e4b658b201a9f2ecdecbb34bed034b"],
    "review_score": [4, 5, 5],
    "review_comment_title": [None, None, None],
    "review_comment_message": [None, None, None],
    "review_creation_date": ["2018-01-18 00:00:00", "2018-03-10 00:00:00", "2018-02-17 00:00:00"],
    "review_answer_timestamp": ["2018-01-18 21:46:59", "2018-03-11 03:05:13", "2018-02-18 14:36:24"]
}
st.dataframe(pd.DataFrame(reviews_data))

# Geolocation Dataset
st.subheader("🌍 Geolocation Dataset")
geo_data = {
    "geolocation_zip_code_prefix": [1037, 1046, 1046],
    "geolocation_lat": [-23.545621, -23.546081, -23.546129],
    "geolocation_lng": [-46.639292, -46.644820, -46.642951],
    "geolocation_city": ["sao paulo", "sao paulo", "sao paulo"],
    "geolocation_state": ["SP", "SP", "SP"]
}
st.dataframe(pd.DataFrame(geo_data))

# Customers Dataset
st.subheader("👥 Customers Dataset")
customers_data = {
    "customer_id": ["06b8999e2fba1a1fbc88172c00ba8bc7", "18955e83d337fd6b2def6b18a428ac77", "4e7b3e00288586ebd08712fdd0374a03"],
    "customer_unique_id": ["861eff4711a542e4b93843c6dd7febb0", "290c77bc529b7ac935b93aa66c333dc3", "060e732b5b29e8181a18229c7b0b2b5e"],
    "customer_zip_code_prefix": [14409, 9790, 1151],
    "customer_city": ["franca", "sao bernardo do campo", "sao paulo"],
    "customer_state": ["SP", "SP", "SP"]
}
st.dataframe(pd.DataFrame(customers_data))

# Order Items Dataset
st.subheader("🛒 Order Items Dataset")
order_items_data = {
    "order_id": ["00010242fe8c5a6d1ba2dd792cb16214", "00018f77f2f0320c557190d7a144bdd3", "000229ec398224ef6ca0657da4fc703e"],
    "order_item_id": [1, 1, 1],
    "product_id": ["4244733e06e7ecb4970a6e2683c13e61", "e5f2d52b802189ee658865ca93d83a8f", "c777355d18b72b67abbeef9df44fd0fd"],
    "seller_id": ["48436dade18ac8b2bce089ec2a041202", "dd7ddc04e1b6c2c614352b383efe2d36", "5b51032eddd242adc84c38acab88f23d"],
    "shipping_limit_date": ["2017-09-19 09:45:35", "2017-05-03 11:05:13", "2018-01-18 14:48:30"],
    "price": [58.90, 239.90, 199.00],
    "freight_value": [13.29, 19.93, 17.87]
}
st.dataframe(pd.DataFrame(order_items_data))

# Products Dataset
st.subheader("📦 Products Dataset")
products_data = {
    "product_id": ["1e9e8ef04dbcff4541ed26657ea517e5", "3aa071139cb16b67ca9e5dea641aaa2f", "96bd76ec8810374ed1b65e291975717f"],
    "product_category_name": ["perfumaria", "artes", "esporte_lazer"],
    "product_name_lenght": [40.0, 44.0, 46.0],
    "product_description_lenght": [287.0, 276.0, 250.0],
    "product_photos_qty": [1.0, 1.0, 1.0],
    "product_weight_g": [225.0, 1000.0, 154.0],
    "product_length_cm": [16.0, 30.0, 18.0],
    "product_height_cm": [10.0, 18.0, 9.0],
    "product_width_cm": [14.0, 20.0, 15.0]
}
st.dataframe(pd.DataFrame(products_data))

# Insight
st.subheader("🔍 Insight")
st.markdown("""
- At first glance, several features in the datasets appear to contain NaN values. 
  This indicates that not all orders have associated review comments or complete product category details.
""")

# --- Assessing Data ---
st.header("🔍 Assessing Data")
st.markdown("This section highlights the assessment of each dataset to identify issues, anomalies, and missing values.")

# Assessing Orders Dataset
st.subheader("📦 Assessing Orders Dataset")
st.image("images/image_asses_orders.jpg", caption="Assessment of Orders Dataset")
st.markdown("""
**Insights:**
- Missing values in several fields.
- The `order_status` field shows that most orders are successfully delivered, with "delivered" being the most common status.
""")

# Assessing Order Reviews Dataset
st.subheader("⭐ Assessing Order Reviews Dataset")
st.image("images/image_asses_order_reviews.jpg", caption="Assessment of Order Reviews Dataset")
st.markdown("""
**Insights:**
- The average review score is 4.08, with a median of 5, reflecting generally high customer satisfaction.
- Many customers leave ratings without written feedback.
""")

# Assessing Geolocation Dataset
st.subheader("🌍 Assessing Geolocation Dataset")
st.image("images/image_asses_geolocation.jpg", caption="Assessment of Geolocation Dataset")
st.markdown("""
**Insights:**
- No missing values.
- Latitude and longitude have a broad range of values, indicating the dataset covers a large geographic area.
""")

# Assessing Customers Dataset
st.subheader("👥 Assessing Customers Dataset")
st.image("images/image_asses_customers.jpg", caption="Assessment of Customers Dataset")
st.markdown("""
**Insights:**
- No missing values.
""")

# Assessing Order Items Dataset
st.subheader("🛒 Assessing Order Items Dataset")
st.image("images/image_asses_order_items.jpg", caption="Assessment of Order Items Dataset")
st.markdown("""
**Insights:**
- No missing values.
- The `order_item_id` column indicates that the most common value for this field is 1, meaning that most orders consist of a single item.
""")

# Assessing Products Dataset
st.subheader("📦 Assessing Products Dataset")
st.image("images/image_asses_products.jpg", caption="Assessment of Products Dataset")
st.markdown("""
**Insights:**
- Some missing values in a few columns.
""")


# --- Cleaning Data ---
st.header("🧹 Cleaning Data")
st.markdown("In this section, we describe the cleaning steps applied to ensure the datasets are consistent, accurate, and ready for analysis.")

# Cleaning Orders Dataset
st.subheader("📦 Cleaning Orders Dataset")
st.markdown("""
- Converted several timestamp columns, such as `order_approved_at`, `order_delivered_carrier_date`, and others, to proper datetime objects for accurate temporal analysis.
- Removed rows with missing values in critical columns like `order_approved_at`, `order_delivered_carrier_date`, and `order_delivered_customer_date` to ensure the dataset contains only complete records.
- Filtered out orders with a status of "canceled" to focus on successfully processed orders.
""")
st.image("images/cleaned_orders_image.jpg", caption="Cleaned Orders Dataset")
st.markdown("""
**Insights:**
- The dataset now has 96,455 entries, reduced from 99,441.
- All timestamp columns are properly formatted as datetime objects.
""")

# Cleaning Order Reviews Dataset
st.subheader("⭐ Cleaning Order Reviews Dataset")
st.markdown("""
- Filled missing values in `review_comment_title` and `review_comment_message` columns with placeholders: "No Title" and "No Message".
""")
st.image("images/cleaned_order_reviews_image.jpg", caption="Cleaned Order Reviews Dataset")
st.markdown("""
**Insights:**
- Reviews without titles and messages are now filled with appropriate placeholders.
- The dataset retains its original size of 99,224 entries.
""")

# Cleaning Products Dataset
st.subheader("📦 Cleaning Products Dataset")
st.markdown("""
- Replaced missing values in `product_category_name` with "Unknown".
- Imputed missing numerical values like `product_name_lenght`, `product_description_lenght`, and `product_photos_qty` with their respective median values for a balanced and representative dataset.
""")
st.image("images/cleaned_products_image.jpg", caption="Cleaned Products Dataset")
st.markdown("""
**Insights:**
- Missing values in categorical and numerical columns have been handled effectively. Except, the length, weight, height, and width are still have missing values. I won't be using these so it doesn't matter.  
""")


st.success("The data is now clean and ready for further analysis!")
