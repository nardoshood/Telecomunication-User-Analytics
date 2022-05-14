import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly as plt
import re
import plotly.express as px
import seaborn as sns

st.title(' User Analytics in the Telecommunication Industry ')

DATA_URL = ('data/cleaned_data.csv')
CLUSTER_URL = ('data/cluster_data.csv')
App_URL = ('data/application_data.csv')
Users_dur = ('data/top_users_dur.csv')
Users_freq = ('data/top_users_freq.csv')
Users_traffic = ('data/top_users_traffic.csv')

def loadData(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data



def cluster_data():
    cluster = pd.read_csv(CLUSTER_URL)
    return cluster


def app_data():
    app=pd.read_csv(App_URL)
    return app


def users_dur():
    dur = pd.read_csv(Users_dur)
    return dur


def users_freq():
    freq = pd.read_csv(Users_freq)
    return freq 


def users_traffic():
    traffic = pd.read_csv(Users_traffic)
    return traffic 
    


data_load_state = st.text('Loading data...')
data = loadData(10000)
cluster = cluster_data()
app = app_data()
dur = users_dur()
freq = users_freq()
traffic = users_traffic() 

data_load_state.text('Loading data...done!')


def barChart(data, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(data).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)



def stBarChart():
    app = app_data()
    title = "Application with their traffic volume"
    barChart(app,title, "app", "traffic_volume")

######### Top users using session freq

def barChart_freq(freq, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(freq).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)



def stBarChart_freq():
    freq = users_freq()
    # st.write(freq) 
    title = "Top Users engagement using sessions frequency as an engagement metrics"
    barChart(freq,title, "MSISDN/Number", "session_freq")


######### Top users using session duration


def barChart_dur(dur, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(dur).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)


def stBarChart_dur():
    dur = users_dur()
    # st.write(dur)
    title = "Top Users engagement using sessions duration as an engagement metrics"
    barChart(dur,title, "MSISDN/Number", "session_dur")


######### Top users using session traffic



def barChart_traffic(traffic, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(traffic).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)


def stBarChart_traffic():
    traffic = users_traffic()
    title = "Top Users engagement using sessions traffic as an engagement metrics"
    barChart(traffic,title, "MSISDN/Number", "session_traffic")



st.subheader('Cleaned Data')
st.write(data)
st.subheader('App Data')
st.write(app)

# st.subheader('3D cluster data')
# st.pyplot(fig)

# st.title("Data Display")
# selectHashTag()
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
# selectLocAndAuth()
st.title("Data Visualizations")
with st.expander("Engagement metricx plots"):
    stBarChart()
    stBarChart_freq()
    stBarChart_dur()
    stBarChart_traffic()



