import streamlit as st
from components.data import get

st.set_page_config(layout="wide")

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.header('Phonepe data Visualsation')

select, maps, sidebar = st.columns([1,3,1])

def show_data(category, year, quarter):

    datas = get.map_data(category, year, quarter)
    if datas is not None:
        map, data, agg_data = datas
        if category=="transaction":
            with maps:
                st.markdown("**:blue[Total Transactions in Millions]**")
                st.write(agg_data["transactions_M"].sum())
                st.markdown("**:blue[Total Transaction Amount in cr `\u20B9`]**")
                st.write(agg_data["amount_cr"].sum().round(3))
                st.markdown("**:blue[Avg transaction value `\u20B9`]**")
                st.write(10*(agg_data["amount_cr"].sum()/agg_data["transactions_M"].sum()).round(3))
                st.plotly_chart(map)
            with sidebar:
                st.markdown("**:blue[Transactions in Millions and Amount in cr `\u20B9` by category]**")
                for ind in agg_data.index:
                    st.subheader(agg_data["transaction_type"][ind])
                    st.write(agg_data["transactions_M"][ind], agg_data['amount_cr'][ind])

        elif category=="user":
            with maps:
                st.markdown("**:blue[Total Registered Users in millions]**")
                st.write(data["users_registered_M"].sum().round(8))
                st.markdown("**:blue[Total AppOpens in millions]**")
                st.write(data["appOpens_M"].sum().round(8))
                st.plotly_chart(map)
            with sidebar:
                st.markdown("**:blue[Transactions_M and percentage by smartphone brand]**")
                if agg_data.empty == True:
                    st.markdown("**:black[no data to show, empty dataframe]**")
                else:    
                    for ind in agg_data.index:
                        st.subheader(agg_data["brand"][ind])
                        st.write(agg_data["transactions_M"][ind], (agg_data['percentage'][ind]*100).round(2))
    else:
        with maps:
            st.markdown("**:black[no data to show, empty dataframe]**")
with select:
    category = st.selectbox(
    'Get data about',
    ('Transaction', 'User'))

    year = st.selectbox(
        'Select Year',
        ('2018','2019','2020','2021','2022'))

    quarter = st.selectbox(
        'Select Quarter',
        ('Q1','Q2','Q3','Q4'))

    if st.button('Get Results'):
        show_data(category.lower(), int(year), int(quarter[1]))