import pandas as pd
import streamlit as st
from plotly.graph_objects import Figure, Scatter, Bar

st.set_page_config(layout="wide")


@st.cache(persist=True)
def load_data():
    table = pd.read_excel('src/data.xlsx', sheet_name='data')
    for year in range(2017, 2021):
        table[year] = table[year].replace(',', '')
        table[year] = table[year].astype('float32')
    return table


data = load_data()

row1_1, row1_2 = st.columns((3, 1))
with row1_2:
    st.subheader(' ')
    st.subheader(' ')
    st.subheader(' ')
    options = st.multiselect(
        label='Выберете показатель',
        options=set(data[data['Вид'] == 'Доходы']['Наименование']),
        default=['Доходы, всего']
    )

with row1_1:
    fig = Figure()
    for option in options:
        fig.add_trace(Scatter(
            name='Москва',
            x=[2017, 2018, 2019, 2020],
            y=data[
                  (data['Вид'] == 'Доходы') &
                  (data['Регион'] == 'Москва') &
                  (data['Наименование'] == option)
              ].iloc[:, 2:].values[0],
            stackgroup='one',
        ))
        fig.add_trace(Scatter(
            name='Россия',
            x=[2017, 2018, 2019, 2020],
            y=data[
                  (data['Вид'] == 'Доходы') &
                  (data['Регион'] == 'Россия') &
                  (data['Наименование'] == option)
              ].iloc[:, 2:].values[0],
            stackgroup='one',
        ))
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        fig.update_xaxes(tickvals=[2017, 2018, 2019, 2020])
    st.plotly_chart(fig, use_container_width=True)

row2_1, row2_2 = st.columns((3, 1))
with row2_2:
    st.subheader(' ')
    st.subheader(' ')
    st.subheader(' ')
    options = st.multiselect(
        label='Выберете показатель',
        options=set(data[data['Вид'] == 'Расходы']['Наименование']),
        default=['Расходы, всего']
    )

with row2_1:
    fig = Figure()
    for option in options:
        fig.add_trace(Scatter(
            name='Москва',
            x=[2017, 2018, 2019, 2020],
            y=data[
                  (data['Вид'] == 'Расходы') &
                  (data['Регион'] == 'Москва') &
                  (data['Наименование'] == option)
              ].iloc[:, 2:].values[0],
            stackgroup='one',
        ))
        fig.add_trace(Scatter(
            name='Россия',
            x=[2017, 2018, 2019, 2020],
            y=data[
                  (data['Вид'] == 'Расходы') &
                  (data['Регион'] == 'Россия') &
                  (data['Наименование'] == option)
              ].iloc[:, 2:].values[0],
            stackgroup='one',
        ))
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        fig.update_xaxes(tickvals=[2017, 2018, 2019, 2020])
    st.plotly_chart(fig, use_container_width=True)
