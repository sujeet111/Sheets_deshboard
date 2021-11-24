import json
from datetime import datetime


with open('data.json') as json_file:
    data = json.load(json_file)

def total_contrubution(email,df):
    time_zero = datetime.strptime('00:00:00', '%H:%M:%S')
    time = datetime.strptime('00:00:00', '%H:%M:%S')
    for i in df[email].keys():
        if i != 'name':
            s1 = datetime.strptime(df[email][i],'%H:%M:%S')
            time = time - time_zero + s1
    return time


total_contrubution("SUJEETPATIL111@GMAIL.COM",data)
