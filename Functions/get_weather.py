import requests
import pandas as pd
import json

def get_weather(start_dates,end_dates,code):
  '''
  Returns a csv file with weather data for a specified city code and a given list of start and end dates

        Parameters:
            start_dates (list) : A list of start dates one month apart (API FUNCTIONALITY)
            end_dates   (list) : A list of end dates one month apart (API FUNCTIONALITY)
            code        (str)  : Airport city

        Returns: 
            A saved csv file with weather data

        Example:
          start_dates = ['2018-03-01','2018-04-02','2018-05-02','2018-06-02','2018-07-02']  # N0TE: OFFSET BY 1 DAY EACH START DATE AS QUERY IS INCLUSIVE
          end_dates = ['2018-04-01','2018-05-01','2018-06-01','2018-07-01','2018-08-01']
          code = 'ATL'
          get_weather(start_dates,end_dates,code) # For the period ranging between 2018-03-01 & 2018-08-01

  '''
  df_final = pd.DataFrame(columns=['date','astronomy','maxtempF','mintempC','mintempF','avgtempC','avgtempF','totalSnow_cm','sunHour','uvIndex','hourly','airport_code'])

  for i , j in zip(end_dates,start_dates):

    url = f"http://api.worldweatheronline.com/premium/v1/past-weather.ashx?q= 41.9803, 87.9090&date={j}&enddate={i}&tp=24&key=b04c3773879a49d3a5f170136212706&format=json"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    df = pd.json_normalize(data['data']['weather'])

    df_final = df_final.append(df)


  df_final = df_final.drop(['hourly'],axis =1)
  df_final = df_final.drop(['astronomy'],axis =1)
  df_final['airport_code'] = code



  df_final.to_csv(f'{code}_final.csv',index=False)