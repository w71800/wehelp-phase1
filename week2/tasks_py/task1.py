def find_and_print(messages):
  ## 目標：做出 [{"name": "...", "message": "...} ] 這樣的結構
  keywords = ["18", "college", "legal age", "will vote"]
  msgList = []
  results = []
  
  # 加工成目標資料結構
  for item in messages.items():
    containerDict = {
      "name": None,
      "msg": None
    }
    containerDict["name"] = item[0]
    containerDict["msg"] = item[1] 
    msgList.append(containerDict)
  
  # 分析資料中是否有關鍵字，有關鍵字的話推進結果的name
  for item in msgList:
    for word in keywords:
      if word in item["msg"]:
        results.append(item["name"])

  return ", ".join(results)
    

# keywords 18, college, legal age, will vote
result = find_and_print({
  "Bob": "My name is Bob. I'm 18 years old.", 
  "Mary": "Hello, glad to meet you.",
  "Copper": "I'm a college student. Nice to meet you.",
  "Leslie": "I am of legal age in Taiwan.",
  "Vivian": "I will vote for Donald Trump next week",
  "Jenny": "Good morning."
})