const hamberger = document.querySelector(".hamberger")
const items = document.querySelector(".items")

hamberger.addEventListener('click', ()=>{
  items.classList.toggle("showItems")
  hamberger.classList.toggle("active")
})