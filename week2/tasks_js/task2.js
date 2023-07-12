function salaryEnhance(data) {
  let items = data.employees

  for(let item of items){
    // 統一型別為 string
    if(typeof(item.salary) == "number"){
      item.salary = item.salary + ""
    }
    if (item.salary.includes("USD")) {
      item.salary = parseInt(item["salary"].replace("USD", "")) * 30
    } else if (item.salary.includes(",")) {
      item.salary = parseInt(item["salary"].replace(",", ""))
    } else {
      item.salary = parseInt(item["salary"])
    }
  }
  
  return data;
}

function calculateSumOfBonus(data) {
  let items = salaryEnhance(data).employees
  let sum = 0;

  // 處理職位
  for (let item of items) {
    let { role, salary } = item
    item.bonus = 0

    if (role == "Engineer") {
      item.bonus = salary * 0.05
    } else if (role == "CEO") {
      item.bonus = salary * 0.1
    } else if (role == "Sales") {
      item.bonus = salary * 0.03
    } else {
      item.bonus = salary * 0.01
    }
  }

  // 處理表現
  for (let item of items) {
    let { performance, bonus } = item

    if (performance.includes("above")) {
      bonus *= 1.1;
    } else if (performance.includes("below")) {
      bonus *= 0.9;
    } else {
      bonus *= 1;
    }

    item.bonus = bonus;
  }

  for (let item of items) {
    sum += item.bonus;
  }

  return sum;
}



const result = calculateSumOfBonus({
  "employees":[ {
    "name":"John",
    "salary":"1000USD",
    "performance":"above average",
    "role":"Engineer"
  },
  {
    "name":"Bob",
    "salary": 60000,
    "performance":"average",
    "role":"CEO"
  },
  {
    "name":"Jenny",
    "salary":"50,000",
    "performance":"below average",
    "role":"Sales"
  } ]
}); // call calculateSumOfBonus function

// test in node
// module.exports = result

export default result
  
  