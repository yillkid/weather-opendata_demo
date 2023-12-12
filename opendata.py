import requests

def get_weather(location):
  weather = ""
  url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=rdec-key-123-45678-011121314"
  response = requests.get(url)
  if response.status_code == 200:
      data = response.json()
      list_location = data['records']['location']
      for obj in list_location:
          if obj['locationName'] == location:
              weather = weather + "早上:" + obj['weatherElement'][0]['time'][0]['parameter']['parameterName']
              weather = weather + "氣溫:" + obj['weatherElement'][2]['time'][0]['parameter']['parameterName'] + "-" + \
                      obj['weatherElement'][1]['time'][0]['parameter']['parameterName'] + " C, " + \
                      obj['weatherElement'][3]['time'][0]['parameter']['parameterName']
              weather = weather + "下午:" + obj['weatherElement'][0]['time'][1]['parameter']['parameterName']
              weather = weather + "氣溫:" + obj['weatherElement'][2]['time'][1]['parameter']['parameterName'] + "-" + \
                      obj['weatherElement'][1]['time'][1]['parameter']['parameterName'] + " C, " + \
                      obj['weatherElement'][3]['time'][1]['parameter']['parameterName']
              weather = weather + "晚上:" + obj['weatherElement'][0]['time'][2]['parameter']['parameterName']
              weather = weather + "氣溫:" + obj['weatherElement'][2]['time'][2]['parameter']['parameterName'] + "-" + \
                      obj['weatherElement'][1]['time'][2]['parameter']['parameterName'] + " C, " + \
                      obj['weatherElement'][3]['time'][2]['parameter']['parameterName']

  return weather

