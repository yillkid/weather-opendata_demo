from datetime import date
import json
from opendata import get_weather

def get_today():
  # 今日日期
  today = date.today()
  
  return today

output = get_weather("南投縣")
print("今日:" +  str(get_today()))
print("地點: 南投縣")
print(json.dumps(output, ensure_ascii = False))
