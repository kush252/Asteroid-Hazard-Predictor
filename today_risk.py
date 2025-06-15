import requests as re
import pandas as pd
from datetime import datetime


def fetch_risky_neo(option):
    key="wmyQlQFlKKfzqLx6LVP5rP1iHuLpNMfvMgEQCvXa"
    if option == 1:
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        date = input("Enter date in yyyy-mm-dd format")
        
    url=f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={key}"
    response=re.get(url)
    print("Status code:",response.status_code)

    data=response.json()
    neos=data['near_earth_objects']


    final_data=[]
    for obj in neos[date]:
        for approach in obj['close_approach_data']:
        
            current=[]
            if obj['close_approach_data']:
                current.append(approach['close_approach_date'])
            current.append(obj['name'])
            if obj['estimated_diameter']:
                current.append(obj['estimated_diameter']['kilometers']['estimated_diameter_max'])
            else:
                current.append(-1)

            if obj['estimated_diameter']:
                current.append(obj['estimated_diameter']['kilometers']['estimated_diameter_min'])
            else:
                current.append(-1)

            if obj['close_approach_data']:
                current.append(approach['relative_velocity']['kilometers_per_hour'])
            else:
                current.append(-1)

            if obj['close_approach_data']:
                current.append(approach['miss_distance']['kilometers'])
            else:
                current.append(-1)
            final_data.append(current)


    df = pd.DataFrame(final_data) 
    
    today_data=[]
    for idx, row in df.iterrows():
        if row[0] == date:
            temp=[]
            for el in row:
                temp.append(el)
            today_data.append(temp)
    return today_data
   
    


   
   
