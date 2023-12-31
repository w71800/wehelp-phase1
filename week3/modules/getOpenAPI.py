# 串接公開平台的 API
import urllib.request as request
import json
import ssl
import re

context = ssl._create_unverified_context()
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src, context = context) as res:
  datas = json.load(res)["result"]["results"]
  with open("attraction.csv", mode="w", encoding="utf-8") as file:
    for data in datas:
      title = data["stitle"]
      position = re.search(r"..區", data["address"]).group(0)
      long = data["longitude"]
      lat = data["latitude"]
      imgUrl = re.search(r"https?://\S+?[jJ][pP][eE]?[gG]", data["file"]).group(0)
      file.write(f"{title}, {position}, {long}, {lat}, {imgUrl}\n")
  with open("mrt.csv", mode="w", encoding="utf-8") as file:
    # 整理資料
    rawDatas = {}
    for data in datas:
      MRT = data["MRT"]
      if MRT == None:
        continue
      elif MRT not in rawDatas:
        rawDatas[MRT] = []
        rawDatas[MRT].append(data["stitle"])
      else:
          rawDatas[MRT].append(data["stitle"])
    else:
      pass
    
    # 寫入資料
    for key, value in rawDatas.items():
      value = ', '.join(value)
      file.write(f"{key}, {value}\n" )