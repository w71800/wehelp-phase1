import urllib.request as request
import json
import ssl
import re

# 串接公開平台的 API
context = ssl._create_unverified_context()
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src, context = context) as res:
  datas = json.load(res)["result"]["results"]
  with open("attraction.csv", mode="w", encoding="utf-8") as file:
    for data in datas:
      title = data["stitle"]
      position = data["address"][5:8]
      long = data["longitude"]
      lat = data["latitude"]
      imgUrl = re.search(r"https?://\S+?[jJ][pP][eE]?[gG]", data["file"]).group(0)
      file.write(f"{title}, {position}, {long}, {lat}, {imgUrl}\n")
  with open("mrt.csv", mode="w", encoding="utf-8") as file:
    # 整理資料，建立一個空 Dict
    rawDatas = {
    }
    for data in datas:
      if data["MRT"] == None:
        continue
      else:
          rawDatas[data["MRT"]] = []
    else:
      print(rawDatas)

    # 開始把景點放入
    for data in datas:
      if data["MRT"] == None:
        continue
      else:
        rawDatas[data["MRT"]].append(data["stitle"])
    else:
      print(rawDatas)
    
    # 寫入資料
    for key, value in rawDatas.items():
      value = ', '.join(value)
      file.write(f"{key}, {value}\n" )




# 爬取 PTT 電影板
# url = 
# req = request.Request()