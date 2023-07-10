def func(*data):
  # 目標：生出 [{"name": ..., "middle": ...}]，策略是把每個 middle 都拿去 loop，遇到同樣的就停
  items = []

  for name in data:
    dict = {}
    dict["name"] = name
    dict["middle"] = name[1]
    items.append(dict)
  else:
    print(items)
  
  for item in items:
    # 抓到當下要進行比較的 middle
    currentMiddle = item["middle"]
    for middle in items:
      if currentMiddle == middle:
        print("遇到同樣的了")
        break
      else:
        print("沒有遇到", "這個人是："+ name.name)

# your code here
func("彭大牆", "王明雅", "吳明") 
# func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")