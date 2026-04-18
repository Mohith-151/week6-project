#==============================================================================
#           A Dashboard using Streamlit for the sales anaylsis
#==============================================================================


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="Sales Executive Dashboard", layout="wide")
st.title("Interactive Sales Dashboard")

# Data Loading
df = pd.read_csv('sales_data.csv') 


# --- GLOBAL METRICS SECTION  ---
total_revenue = df['Total Sales'].sum()
total_qty = df['Quantity Sold'].sum()
avg_spent = df['Total Sales'].mean()

m_col1, m_col2, m_col3 = st.columns(3)
m_col1.metric("Total Revenue", f"${total_revenue:,.2f}")
m_col2.metric("Total Quantity Sold", f"{total_qty:,}")
m_col3.metric("Average Transaction Value", f"${avg_spent:,.2f}")

st.markdown("---")

# --- GLOBAL VISUALS ---
g_col1, g_col2 = st.columns(2)

with g_col1:
    st.subheader("Revenue by Product Category")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df, x='Product Category', y='Total Sales', estimator=sum, palette='flare', ax=ax1, hue='Product Category', legend=False)
    # plt.xticks(rotation=45)
    st.pyplot(fig1)

with g_col2:
    st.subheader("Revenue by Shops")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df, x='Shop Name', y='Total Sales', estimator=sum, palette='crest', ax=ax2, hue='Shop Name', legend=False)
    # plt.xticks(rotation=45)
    st.pyplot(fig2)

st.markdown("---")

# --- PRODUCT CATEGORY- FILTER BUTTONS ---
st.subheader("Filter the Anaylsis by Product Category")
categories = list(df['Product Category'].unique())

# Initialize session state for the selected category if it doesn't exist
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = categories[0]

# Create a row of buttons
btn_cols = st.columns(len(categories))
for i, category in enumerate(categories):
    if btn_cols[i].button(category, use_container_width=True):
        st.session_state.selected_category = category

# Filter the dataframe for the deep-dive section ONLY
filtered_df = df[df['Product Category'] == st.session_state.selected_category]

st.info(f"Currently viewing details for: **{st.session_state.selected_category}**")

# --- 6. FILTERED VISUALS SECTION ---
# Row 1: KPI Cards for selected category
kpi_col1, kpi_col2 = st.columns(2)
cat_rev = filtered_df['Total Sales'].sum()
cat_qty = filtered_df['Quantity Sold'].sum()

kpi_col1.metric(f"Revenue: {st.session_state.selected_category}", f"${cat_rev:,.2f}")
kpi_col2.metric(f"Units Sold: {st.session_state.selected_category}", f"{cat_qty:,}")

# Row 2: Charts
chart_col1, chart_col2 = st.columns([2, 1]) # Scatter is wider (ratio 2:1)

with chart_col1:
    st.subheader("Product Detail Analysis")
    fig_scatter = px.scatter(
        filtered_df, 
        x="Price Per Unit", 
        y="Total Sales", 
        size="Quantity Sold", 
        color="Shop Name",
        hover_name="Product Name",
        title=f"Price vs Sales in {st.session_state.selected_category}"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with chart_col2:
    st.subheader("Top 3 Products")
    # Get top 3 by total sales
    top_3_df = filtered_df.groupby('Product Name')['Total Sales'].sum().nlargest(3).reset_index()
    
    fig_top3, ax_top3 = plt.subplots(figsize=(5, 7.5)) # Taller plot
    sns.barplot(data=top_3_df, y='Product Name', x='Total Sales', palette='viridis', ax=ax_top3, hue='Product Name', legend=False)
    st.pyplot(fig_top3)