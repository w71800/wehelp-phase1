def find_index_of_car(seats, status, number):
  # 先把資訊整合進一個 List 中
  seatInfos = []
  for i, seat in enumerate(seats):
    dict = {}
    dict["seats"] = seat
    dict["available"] = True if status[i] == 1 else False
    dict["index"] = i

    seatInfos.append(dict)
  pass

  candidates = []
  for info in seatInfos:
    if info["available"] == True and info["seats"] >= number:
      candidates.append(info)
  else:
    # 在這邊如果沒有符合資格的車廂就跳出
    if len(candidates) == 0:
      return str(-1) + "（很遺憾，目前無符合您需求的車廂）"
  
  candidates = sorted(candidates, key=lambda x: x["seats"])
  return "您訂到了 "+ str(candidates[0]["index"]) + " 號車廂的 " + str(number) + " 個座位"


result = find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
# result = find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
# result =  find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2