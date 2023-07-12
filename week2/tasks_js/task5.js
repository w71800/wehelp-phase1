function findIndexOfCar(seats, status, number) {
  // 先把資訊整合進一個物件陣列中
  const seatInfos = []
  for (let [i, seat] of seats.entries()) {
    let info = {}
    info.seats = seat
    info.available = status[i] === 1 ? true : false
    info.index = i
    seatInfos.push(info)
  }

  // 開始處理合乎資格的車廂資訊（找 seats 最少的）
  let candidates = []
  candidates = seatInfos.filter( info => info.available && info.seats >= number )
  candidates.sort( (c1, c2) => c1.seats - c2.seats )
  if(candidates.length > 0){
    return `您訂到了 ${candidates[0].index} 號車廂的 ${number} 個座位`
  }else{
    return `${-1}（很遺憾，目前無符合您需求的車廂）`
  }
}

const result = findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) // print 4
// const result = findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) // print -1
// const result = findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4) // print 2


// node test
// module.exports = result

export default result
