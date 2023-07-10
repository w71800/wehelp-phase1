def func(*data):
  # 目標：生出 [{"name": ..., "middle": ...}]，策略是把每個 middle 都拿去 loop，遇到同樣的就停（先改成數個數）
  items = []
  results = []
  
  # 加工資料生成 items，方便做處理
  for name in data:
    dict = {}
    dict["name"] = name
    dict["middle"] = name[1]
    items.append(dict)
  
  # 開始每個要來做比對
  for item in items:
    # 當下要進行 loop 比較的 middle
    currentMiddle = item["middle"]
    count = 0
    # 進行比對
    for target in items:
      targetMiddle = target["middle"]
      # 數到跟自己一樣的就 +1
      if currentMiddle == targetMiddle:
        count += 1
    # 當下這個字比較完一輪後，個數為 1 的就推進該結果
    else:
      if count == 1:
        results.append(item["name"])
  else:
    if len(results) != 0:
      return results
    else:
      return "沒有對應的結果"



# your code here
result1 = func("彭大牆", "王明雅", "吳明") 
result2 = func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花", "中小小")