function findIndexOfCar(seats, status, number) {
  // 先把資訊整合進一個物件陣列中
  const seatInfos = []
  for (let [i, seat] of seats.entries()) {
    let info = {}
    info.seats = seat
    info.available = status[i] === 1 ? true : false
    seatInfos.push(info)
  }

  // 開始遍歷
  let r = null
  for (let [i, info] of seatInfos.entries()) {
    if (info.available === true && info.seats >= number) {
      r = i + 1
      return `已為您訂到第 ${r} 號車廂的 ${number} 個位子`
    }
  }

  return -1
}

const result = findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) // print 4
// const result = findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) // print -1
// const result = findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4) // print 2


// node test
// module.exports = result

export default result
