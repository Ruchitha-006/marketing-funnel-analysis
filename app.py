import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Marketing Funnel Analysis Dashboard")

st.write("Analyze Visitors → Leads → Customers conversion funnel")

# Sample Data
data = {
    'Channel': ['Facebook', 'Google Ads', 'Instagram', 'LinkedIn'],
    'Visitors': [1200, 2000, 1000, 800],
    'Leads': [240, 350, 150, 220],
    'Customers': [50, 120, 40, 90]
}

df = pd.DataFrame(data)

# Calculate Conversion Rates
df['Visitor_to_Lead_%'] = (df['Leads'] / df['Visitors']) * 100
df['Lead_to_Customer_%'] = (df['Customers'] / df['Leads']) * 100
df['Overall_Conversion_%'] = (df['Customers'] / df['Visitors']) * 100

st.subheader("📄 Funnel Data")
st.dataframe(df)

# Overall Conversion Chart
st.subheader("📈 Overall Conversion by Channel")

fig1, ax1 = plt.subplots()
ax1.bar(df['Channel'], df['Overall_Conversion_%'])
ax1.set_ylabel("Conversion %")
ax1.set_xlabel("Channel")
plt.xticks(rotation=45)

st.pyplot(fig1)

# Lead Quality Chart
st.subheader("🎯 Lead to Customer Conversion")

fig2, ax2 = plt.subplots()
ax2.bar(df['Channel'], df['Lead_to_Customer_%'])
ax2.set_ylabel("Lead to Customer %")
ax2.set_xlabel("Channel")
plt.xticks(rotation=45)

st.pyplot(fig2)

# Funnel Drop Off
st.subheader("📉 Overall Funnel Drop-Off")

total_visitors = df['Visitors'].sum()
total_leads = df['Leads'].sum()
total_customers = df['Customers'].sum()

st.write(f"Visitors: {total_visitors}")
st.write(f"Leads: {total_leads}")
st.write(f"Customers: {total_customers}")

fig3, ax3 = plt.subplots()
ax3.bar(['Visitors', 'Leads', 'Customers'], 
        [total_visitors, total_leads, total_customers])
ax3.set_ylabel("Users")

st.pyplot(fig3)

st.success("✅ Funnel Analysis Complete")
