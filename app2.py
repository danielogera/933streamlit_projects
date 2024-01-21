import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='streamlit sales dashboard',
    layout='centered',
    initial_sidebar_state='auto',
    page_icon=':books:'
)
st.header(':blue[Importing and analysing data with pandas]')
st.divider()

# importing a csv file
data_file = 'analyze.csv'
data = pd.read_csv(data_file, index_col=False)
# creating a DataFrame FROM THE DATA SET
df = pd.DataFrame(data)

st.write(df.head())

# plotting the data

unit_price = df[['Unit_Price']]
st.metric(label=':red[Average Unit price]', value=unit_price.mean().round(2))
st.bar_chart(unit_price.head(50), color= [0.8, 0, 0.2])

profit = df[['Profit']]
st.metric(label=':red[Average profit]', value=profit.mean().round(2))
st.bar_chart(profit.head(50),  color= [0.8, 0, 0.2])

Revenue = df[['Revenue']]
st.metric(label=':red[Average Revenue]', value=Revenue.mean().round(2))
st.bar_chart(Revenue.head(50),  color= [0.8, 0, 0.2])
