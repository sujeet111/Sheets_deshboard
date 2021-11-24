from os import name
from main import driver_code
import streamlit as st
import json
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

st.title('ACTIVITIES REPORT')
d1 = str(st.date_input('start date'))
d2 = str(st.date_input('End date'))

d1 = str(datetime.strptime(d1, '%Y-%m-%d').strftime('%d/%m/%Y'))
d2 = str(datetime.strptime(d2, '%Y-%m-%d').strftime('%d/%m/%Y'))
st.write(type(d1))
d1
st.write(type(d2))
d2

with open('data.json') as json_file:
    json_output = json.load(json_file)

def total_contrubution(email,df):
    time_zero = datetime.strptime('00:00:00', '%H:%M:%S')
    time = datetime.strptime('00:00:00', '%H:%M:%S')
    for i in df[email].keys():
        if i != 'name':
            s1 = datetime.strptime(df[email][i],'%H:%M:%S')
            time = time - time_zero + s1
    return time.time()

def interval_contrubution(email,df,d1,d2):
    time_zero = datetime.strptime('00:00:00', '%H:%M:%S')
    time = datetime.strptime('00:00:00', '%H:%M:%S')
    for i in df[email].keys():
        if i == 'name':
            continue
        
        if datetime.strptime(d1, "%d/%m/%Y") <= datetime.strptime(i, "%d/%m/%Y") <= datetime.strptime(d2, "%d/%m/%Y"):
            s1 = datetime.strptime(df[email][i],'%H:%M:%S')
            time = time - time_zero + s1
    return time.time()

with open('data.json') as json_file:
    json_output = json.load(json_file)

for i in json_output.keys():
    if EMAIL_REGEX.match(i):
        st.subheader(json_output[i]['name'])
        user_time = total_contrubution(i,json_output)
        st.write('Total hours devoted by ',json_output[i]['name'],' : ',str(user_time.hour),"hours and ",str(user_time.minute)," minutes")
        interval_time = interval_contrubution(i,json_output,d1,d2)
        st.write('Total hours in the mentioned period :',json_output[i]['name'],' : ',str(interval_time.hour),"hours and ",str(interval_time.minute)," minutes")
    
st.button('Update This Report')
driver_code()