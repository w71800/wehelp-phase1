function func(...data) {
  const items = []
  const results = []

  // 加工資料生成 items，方便處理
  for (let name of data) {
    let container = {}
    container.name = name
    container.middle = name[1]
    items.push(container)
  }

  // 開始每個要來做比對
  for (let item of items) {
    // 當下要進行比對的 middle
    let currentMiddle = item.middle
    let count = 0
    // 進行比對
    for (let target of items) {
      let targetMiddle = target.middle
      // 數到跟自己一樣的就 +1
      if (currentMiddle ===targetMiddle) {
        count += 1
      }
    }
    // 當下這個字比較完一輪後，個數為 1 的就推進該結果
    if (count == 1) {
      results.push(item.name)
    }
  }

  if (results.length != 0) {
    return results
  } else {
    return "沒有對應的結果"
  }
}

var result1 = func("彭大牆", "王明雅", "吳明")
var result2 = func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花", "中小小")
// node test
module.exports = { result1, result2 }

// export default { result1, result2 }
