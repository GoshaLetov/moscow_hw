import requests

import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from plotly.graph_objects import Figure, Scatter

st.set_page_config(layout="wide")

DATA_FED_BUDGET_URL = 'https://minfin.gov.ru'
DATA_MOSCOW_GDP_URL = 'https://budget.mos.ru/budget'
IMAGE_URL_1 = 'https://freelance.ru/img/portfolio/pics/00/2F/99/3119447.jpg'
LOTTIE_URL_1 = 'https://assets6.lottiefiles.com/private_files/lf30_rysgr4xj.json'


@st.cache(persist=True)
def load_data():
    table = pd.read_excel('src/data.xlsx', sheet_name='data')
    for year in range(2017, 2021):
        table[year] = table[year].replace(',', '')
        table[year] = table[year].astype('float32')
    return table


row1_1, row1_2 = st.columns((4, 2))

with row1_1:
    st.title(
        """
        Ключевые показатели исполнения Федерального Бюджета РФ за период с 2006 по 2020 годы
        """)
    st.subheader(
        f"""
        Источник данных:
        [Официальный сайт Министерства Финансов РФ]({DATA_FED_BUDGET_URL})

        [Портал Правительства Москвы "Открытый бюджет"]({DATA_MOSCOW_GDP_URL})
        """)
    st.subheader(
        """
        Выполнили:
        Студенты 407 группы

        Хвощев Кирилл и Черхаров Роман
        """)


image = requests.get(IMAGE_URL_1)
with row1_2:
    st.image(image.content, use_column_width=True)

st.subheader(' ')
st.subheader('Сравнение ключевых показателей бюджета Москвы и Федерального бюджета')

data = load_data()


st.title('Сравнение доходов, млрд. рублей')
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
              ].iloc[:, 3:].values[0],
            stackgroup='one',
        ))
        fig.add_trace(Scatter(
            name='Россия',
            x=[2017, 2018, 2019, 2020],
            y=data[
                  (data['Вид'] == 'Доходы') &
                  (data['Регион'] == 'Россия') &
                  (data['Наименование'] == option)
              ].iloc[:, 3:].values[0],
            stackgroup='one',
        ))
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        fig.update_xaxes(tickvals=[2017, 2018, 2019, 2020])
    st.plotly_chart(fig, use_container_width=True)

st.title('Сравнение доходов, %')
fig = Figure()
fig.add_trace(Scatter(
    x=[2017, 2018, 2019, 2020],
    y=((data[
           (data['Вид'] == 'Доходы') & (data['Регион'] == 'Россия') & (data['Наименование'] == option)
       ].iloc[:, 3:].values[0]) /
       data[
           (data['Вид'] == 'Доходы') & (data['Регион'] == 'Москва') & (data['Наименование'] == option)
       ].iloc[:, 3:].values[0])
))
fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
fig.update_xaxes(tickvals=[2017, 2018, 2019, 2020])
st.plotly_chart(fig, use_container_width=True)

lottie = requests.get(LOTTIE_URL_1)
st_lottie(lottie.json(), speed=1, height=200, key='initial')


st.title('Сравнение расходов, млрд. рублей')
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
              ].iloc[:, 3:].values[0],
            stackgroup='one',
        ))
        fig.add_trace(Scatter(
            name='Россия',
            x=[2017, 2018, 2019, 2020],
            y=data[
                  (data['Вид'] == 'Расходы') &
                  (data['Регион'] == 'Россия') &
                  (data['Наименование'] == option)
              ].iloc[:, 3:].values[0],
            stackgroup='one',
        ))
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        fig.update_xaxes(tickvals=[2017, 2018, 2019, 2020])
    st.plotly_chart(fig, use_container_width=True)


st.title('Сравнение расходов, %')
fig = Figure()
fig.add_trace(Scatter(
    x=[2017, 2018, 2019, 2020],
    y=((data[
           (data['Вид'] == 'Расходы') & (data['Регион'] == 'Россия') & (data['Наименование'] == option)
       ].iloc[:, 3:].values[0]) /
       data[
           (data['Вид'] == 'Расходы') & (data['Регион'] == 'Москва') & (data['Наименование'] == option)
       ].iloc[:, 3:].values[0])
))
fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
fig.update_xaxes(tickvals=[2017, 2018, 2019, 2020])
st.plotly_chart(fig, use_container_width=True)
