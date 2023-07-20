import './script/hamberEffect.js'

const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
let dataPool
let showNum = 12

// 載入（抓取資料） → 根據資料的前 3+12 筆做出 block → append 這些 block → 前三個加上 .rect 的 class
// 
fetch(url)
  .then( res => res.json() )
  .then( data => {
    let r = data.result.results
    dataPool = r
    render(15)
    const blocks = document.querySelectorAll(".block")
    for(let i=0; i<3; i++){
      blocks[i].classList.add("rect")
    }
  })


  
  // 根據傳進來的資料物件來製作對應的 block
  function makeBlock(dataObj) {
    let { stitle: title, file: urls } = dataObj
    const regex = /https?:\/\/\S+?\.(?:jpg|jpeg|png|gif)/i;
    let url = urls.match(regex)
    
  const block = document.createElement("div")
  const img = document.createElement("img") // 1
  const wrapper = document.createElement("div") // 2
  const text = document.createElement("div")
  let textContent = document.createTextNode(title)

  block.classList.add("block")
  wrapper.classList.add("text_wrapper")
  text.classList.add("text")
  img.setAttribute("src", url)
  text.appendChild(textContent)
  wrapper.appendChild(text)
  block.appendChild(img)
  block.appendChild(wrapper)

  return block
}

// 渲染 block 出來
function render(num){
  const container = document.querySelector("#content .container")
  
  for(let i=0; i<num; i++){
    let dataObj = dataPool[i]
    let block = makeBlock(dataObj)
    
    container.appendChild(block)
  }
}