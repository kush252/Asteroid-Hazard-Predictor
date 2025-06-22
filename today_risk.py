import requests as re
import pandas as pd
from datetime import datetime
import sys

def fetch_risky_neo(option):
    key="wmyQlQFlKKfzqLx6LVP5rP1iHuLpNMfvMgEQCvXa"
    if option == 1:
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        date = input("Enter date in yyyy-mm-dd format: ")

    try:
        url=f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={key}"
        response=re.get(url)
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)
    

    data=response.json()
    neos=data['near_earth_objects']


    final_data = []

    for obj in neos[date]:
        name = obj.get('name', 'Unknown')
        est_diam = obj.get('estimated_diameter', {}).get('kilometers', {})
        diameter_max = est_diam.get('estimated_diameter_max', -1)
        diameter_min = est_diam.get('estimated_diameter_min', -1)
        abs_mag = obj.get('absolute_magnitude_h', -1)

        for approach in obj.get('close_approach_data', []):
            row = [
                approach.get('close_approach_date', 'N/A'),
                name,
                diameter_max,
                diameter_min,
                approach.get('relative_velocity', {}).get('kilometers_per_hour', -1),
                approach.get('miss_distance', {}).get('kilometers', -1),
                abs_mag
            ]
            final_data.append(row)



    df = pd.DataFrame(final_data) 
    
    today_data=[]
    for idx, row in df.iterrows():
        if row[0] == date:
            temp=[]
            for el in row:
                temp.append(el)
            today_data.append(temp)
    return today_data
   
    


   
   
