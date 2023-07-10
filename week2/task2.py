def salaryEnhance(data):
  items = data["employees"]
  # 處理薪水
  for item in items:
    if "USD" in item["salary"]:
      item["salary"] = int(item["salary"].replace("USD", "")) * 30
    elif "," in item["salary"]:
      item["salary"] = int(item["salary"].replace(",", ""))
    else:
      item["salary"] = int(item["salary"])
  return data


def calculate_sum_of_bonus(data):
  # 目標：根據大家的狀態與角色來計算對應的獎金量，基礎薪水的部分要處理過
  items = salaryEnhance(data)["employees"]
  sum = 0
  # 處理職位
  for item in items:
    role = item["role"]
    item["bonus"] = 0
    salary = item["salary"]

    if role == "Engineer":
      item["bonus"] = salary*0.05
    elif role == "CEO":
      item["bonus"] = salary*0.1
    elif role == "Sales":
      item["bonus"] = salary*0.03
    else:
      item["bonus"] = salary*0.01

  # 處理表現
  for item in items:
    performance = item["performance"]
    bonus = item["bonus"]
    if "above" in performance:
      bonus *= 1.1
    elif "below" in performance:
      bonus *= 0.9
    else:
      bonus *= 1
  
  for item in items:
    sum += item["bonus"]
  return sum


result = calculate_sum_of_bonus({
  "employees": [
    {
      "name": "John",
      "salary": "1000USD",
      "performance": "above average",
      "role": "Engineer"
    },
    {
      "name": "Bob",
      "salary": "60000",
      "performance": "average",
      "role": "CEO"
    },
    {
      "name": "Jenny",
      "salary": "50,000",
      "performance": "below average",
      "role": "Sales"
    },
  ]
}) # call calculate_sum_of_bonus function
