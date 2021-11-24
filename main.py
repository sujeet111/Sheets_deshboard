import pandas as pd
import json
from datetime import datetime

#Google Sheet Data Extraction
sheet_url = "https://docs.google.com/spreadsheets/d/1-NtDj5odd6WErdRbeeAaXbiUhcZTqSQ_A_LQxiaXHf4/edit#gid=2000723695"
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
output = pd.read_csv(url_1)

def duration(s1,s2,ope):
    FMT = '%H:%M:%S'
    if ope == "sub":
        return str(datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT))
    if ope == "add":
        return str(datetime.strptime(s2, FMT) + datetime.strptime(s1, FMT))
     
    # duration(row['Duration(Start Time)'],row['Duration(End Time)'])



def driver_code(): 
    for i in range(len(output.index)):
        print("*"*5)
        with open('data.json') as json_file:
            json_output = json.load(json_file)

        row = output.iloc[i]
        data = {}
        time_spent = duration(row['Duration(Start Time, 24 hr format)'], row['Duration(End Time, 24 hr format)'], "sub")
        try:
            if row['Email address'] in json_output.keys():
                data = json_output[row['Email address']]
                data[row['Date']] = time_spent
                json_output[row['Email address']] = data

            if row['Email address'] not in json_output.keys():
                data['name'] = row['Name']
                data[row['Date']] = time_spent
                json_output[row['Email address']] = data
        except:
            pass
        
        json_output['Last updated'] = str(datetime.now())
        print('Last updated = ', json_output['Last updated'])

        with open('data.json', 'w') as outfile:
            json.dump(json_output, outfile, indent=4 )
        print('success')

driver_code()