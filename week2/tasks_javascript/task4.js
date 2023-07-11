/** 
 * 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, ...
 * 策略：
 * 偶數項 4, 7, 10....(3(n/2)+1)
 * 奇數項 3, 6, 9，先抓到其對應的偶數項 n-1 的值，再扣 1 起來
*/ 

function getNumber(index) {
  let n = index + 1
  if (n === 1) {
    return 0
  } else if (n % 2 === 0) {
    return parseInt(3 * (n / 2) + 1)
  } else {
    var oddGuy = 3 * ((n - 1) / 2) + 1
    return parseInt(oddGuy - 1)
  }
}

const resultOf_1 = getNumber(1) // 印出 4
const resultOf_5 = getNumber(5) // 印出 10
const resultOf_10 = getNumber(10) // 印出 15

// node test
// module.exports = { resultOf_1, resultOf_5, resultOf_10}

export default { resultOf_1, resultOf_5, resultOf_10 } 