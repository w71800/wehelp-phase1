import './script/hamberEffect.js'

const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
const loadBtn = document.querySelector("#btn_load")
let dataPool
let renderStart = 0

/**
 * 載入（抓取資料） → 
 * 根據資料的前 3+12 筆做出 block → 
 * append 這些 block → 
 * 前三個加上 .rect 的 class
 * */ 
fetch(url)
  .then( res => res.json() )
  .then( data => {
    let r = data.result.results
    dataPool = r
    initialize()
  })

  function initialize() {
    render(15)
    const blocks = document.querySelectorAll(".block")
    for(let i=0; i<3; i++){
      blocks[i].classList.add("rect")
    }
    setInterval(()=>{
      loadBtn.classList.remove("hide")
    },500)
  }
  
  // 根據傳進來的資料物件來製作對應的 block
  function makeBlock(dataObj) {
    let { stitle: title, file: urls } = dataObj
    const regex = /https?:\/\/\S+?\.(?:jpg|jpeg|png)/i;
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
function render(num, start = 0) {
  const container = document.querySelector("#content .container")
  // 根據起點和渲染數決定終點
  let end = start + num
  // 如果終點超過的話，自動抓到最後
  if(end > dataPool.length) {
    end = dataPool.length
  } 
  
  // 根據範圍區間來渲染出對應的數據
  for(let i=start; i<end; i++){
    let dataObj = dataPool[i]
    let block = makeBlock(dataObj)
    
    container.appendChild(block)
  }
  renderStart = end
  console.log(renderStart);
}

loadBtn.addEventListener("click", ()=>{
  // 點擊時檢查起點是否已經超過
  if(renderStart >= dataPool.length) {
    alert("已經沒有可顯示資料囉！")
    loadBtn.classList.add("inactive")
    loadBtn.textContent = "全下載完囉"
    return
  }

  render(12, renderStart)
})