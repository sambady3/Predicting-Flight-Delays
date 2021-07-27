import ast

def parse_hourly(row):
    
  '''
  Used to parse the hourly column and weather desc columns returned from the weather api: http://api.worldweatheronline.com 
  '''  

  return ast.literal_eval(row)