def find_index_of_car(seats, status, number):
  # 先把資訊整合進一個 List 中
  seatInfos = []
  for i, seat in enumerate(seats):
    dict = {}
    dict["seats"] = seat
    dict["available"] = True if status[i] == 1 else False

    seatInfos.append(dict)
  
  ## 開始遍歷
  r = None
  for i, info in enumerate(seatInfos):
    if info["available"] == True and info["seats"] >= number:
      r = i + 1
      return "已為您訂到第 "+ str(r) + " 號車廂的 " + str(number) + " 個位子"
  else: 
    return -1

 


result = find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
# result = find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
# result =  find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2