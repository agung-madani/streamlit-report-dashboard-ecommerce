import streamlit as st

# --- Exploratory Data Analysis ---
st.header("📊 Exploratory Data Analysis")
st.markdown("This page focuses on uncovering patterns and insights from the datasets to address the business questions.")

# Business Question 1
st.subheader("🚚 Business Question 1: How does product delivery performance impact customer satisfaction?")
st.markdown("""
To answer this question, we explored the relationship between delivery time, order status, and customer review scores. For this analysis, the **Orders** and **Order Reviews** datasets were utilized.

### Process:
1. **Calculated Delivery Time**: 
   - The delivery time for each order was computed as the difference between the `order_delivered_customer_date` and `order_purchase_timestamp`.
   - This gives the delivery duration in days.

2. **Merged Datasets**: 
   - The `Orders` and `Order Reviews` datasets were merged using `order_id` to combine review scores with delivery times and order statuses.

3. **Grouped Analysis**:
   - Delivery time statistics were calculated by grouping data by `order_status` and `review_score` to identify patterns.

### Insights:
The table below summarizes the delivery time statistics by order status and review score:

| Order Status | Review Score | Count  | Mean   | Std Dev | Min  | 25%  | Median | 75%  | Max   |
|--------------|--------------|--------|--------|---------|------|------|--------|------|-------|
| Delivered    | 1            | 9,405  | 20.85  | 16.06   | 0    | 9    | 16     | 30   | 195   |
| Delivered    | 2            | 2,940  | 16.19  | 12.49   | 1    | 8    | 13     | 22   | 208   |
| Delivered    | 3            | 7,960  | 13.79  | 9.94    | 0    | 7    | 12     | 18   | 188   |
| Delivered    | 4            | 18,983 | 11.85  | 8.29    | 0    | 7    | 10     | 15   | 194   |
| Delivered    | 5            | 57,050 | 10.22  | 6.82    | 0    | 6    | 9      | 13   | 187   |

### Key Observations:
- **Impact of Delivery Time on Customer Satisfaction**:
   - As the review score decreases, the mean delivery time increases, suggesting that customers who receive their products later tend to leave lower ratings.
   - Conversely, faster deliveries are associated with higher review scores.
   
- **Delivery Time Range**:
   - The minimum delivery time is 0 days (indicating some orders are delivered on the same day or very quickly).
   - The maximum delivery time is surprisingly high, with some orders taking more than 150 days to deliver, which may indicate outliers or exceptional cases.

This analysis reinforces the idea that improving product delivery times could significantly boost customer satisfaction.
""")

# Business Question 2
st.subheader("📈 Business Question 2: What are the regional sales patterns and product preferences?")
st.markdown("""
To address this question, we analyzed sales patterns and product preferences across different states using multiple datasets: **Orders**, **Customers**, **Geolocation**, **Order Items**, and **Products**.

### Process:
1. **Merging Datasets**:
   - The datasets were merged sequentially to combine information about orders, customers' geolocations, purchased items, and product details.
   - This created a comprehensive dataset containing 16,838,631 entries across 32 columns.
            
      | Column                          | Data Type        |
      |---------------------------------|------------------|
      | order_id                        | object           |
      | customer_id                     | object           |
      | order_status                    | object           |
      | order_purchase_timestamp        | datetime64[ns]   |
      | order_approved_at               | datetime64[ns]   |
      | order_delivered_carrier_date    | datetime64[ns]   |
      | order_delivered_customer_date   | datetime64[ns]   |
      | order_estimated_delivery_date   | datetime64[ns]   |
      | delivery_time                   | int64            |
      | customer_unique_id              | object           |
      | customer_zip_code_prefix        | int64            |
      | customer_city                   | object           |
      | customer_state                  | object           |
      | geolocation_zip_code_prefix     | float64          |
      | geolocation_lat                 | float64          |
      | geolocation_lng                 | float64          |
      | geolocation_city                | object           |
      | geolocation_state               | object           |
      | order_item_id                   | int64            |
      | product_id                      | object           |
      | seller_id                       | object           |
      | shipping_limit_date             | object           |
      | price                           | float64          |
      | freight_value                   | float64          |
      | product_category_name           | object           |
      | product_name_lenght             | float64          |
      | product_description_lenght      | float64          |
      | product_photos_qty              | float64          |
      | product_weight_g                | float64          |
      | product_length_cm               | float64          |
      | product_height_cm               | float64          |
      | product_width_cm                | float64          |

2. **Calculating Total Sales**:
   - The total sales for each order were calculated by summing the product price and freight value.
   - Regional sales were grouped by `customer_state` and `product_category_name`.

3. **Analysis of Regional Sales**:
   - **Top States by Total Sales**: 
     Sales by state were aggregated, sorted, and analyzed to identify the leading regions for total revenue generation.
   - **Top Product Categories by Total Sales**:
     Product category sales were aggregated to highlight the most popular categories across all regions.
   - **State-Specific Top Product Categories**:
     The product category contributing the most sales within each state was identified.

### Insights:

#### Top States by Total Sales:
| **State** | **Total Sales**  |
|-----------|------------------|
| São Paulo (SP) | 789,463,100.00 |
| Rio de Janeiro (RJ) | 496,243,000.00 |
| Minas Gerais (MG) | 455,701,800.00 |

- São Paulo leads in total sales, followed by Rio de Janeiro and Minas Gerais, showcasing significant regional disparities. Smaller states like Roraima (RR) and Acre (AC) contribute much less, indicating varying consumer demand levels.

#### Top Product Categories by Total Sales:
| **Category**         | **Total Sales**      |
|-----------------------|----------------------|
| Beleza_saude          | 206,442,500.00      |
| Cama_mesa_banho       | 199,513,300.00      |
| Relogios_presentes    | 181,759,400.00      |

- Products in personal care (`beleza_saude`), home goods (`cama_mesa_banho`), and accessories (`relogios_presentes`) generate the highest sales, reflecting strong consumer interest in these categories.

#### State-Specific Top Product Categories:
| Customer State | Product Category      | Total Sales     |
|----------------|-----------------------|-----------------|
| PI             | automotivo           | 594,122.27      |
| PA             | beleza_saude         | 2,681,628.48    |
| SE             | beleza_saude         | 718,023.18      |
| RN             | beleza_saude         | 704,261.75      |
| PE             | beleza_saude         | 3,176,895.58    |
| MS             | beleza_saude         | 1,045,073.50    |
| MG             | beleza_saude         | 46,702,099.26   |
| TO             | beleza_saude         | 457,131.92      |
| DF             | beleza_saude         | 1,650,661.70    |
| CE             | beleza_saude         | 1,936,407.31    |
| BA             | beleza_saude         | 6,415,536.29    |
| RO             | brinquedos           | 398,513.77      |
| SP             | cama_mesa_banho      | 77,048,732.15   |
| RS             | cama_mesa_banho      | 11,100,743.78   |
| RR             | eletrodomesticos     | 54,809.30       |
| PR             | esporte_lazer        | 8,422,806.00    |
| SC             | esporte_lazer        | 8,043,614.65    |
| AM             | ferramentas_jardim   | 103,453.26      |
| MA             | informatica_acessorios | 1,361,708.38  |
| AP             | informatica_acessorios | 213,809.91    |
| PB             | pcs                  | 1,065,182.99    |
| AL             | relogios_presentes   | 1,302,386.41    |
| GO             | relogios_presentes   | 2,194,149.68    |
| ES             | relogios_presentes   | 4,538,792.77    |
| MT             | relogios_presentes   | 3,119,980.81    |
| RJ             | relogios_presentes   | 43,616,746.18   |
| AC             | relogios_presentes   | 216,478.07      |

- **Beleza_saude** is a dominant product category across many states, suggesting broad appeal for personal care items.
- Categories like `brinquedos` and `ferramentas_jardim` are localized to specific regions, highlighting regional preferences.

This analysis uncovers regional trends in consumer demand and product popularity, providing valuable insights for targeted marketing and inventory planning.
""")
