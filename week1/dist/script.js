const hamberger = document.querySelector(".hamberger")
const sidebar = document.querySelector("#sidebar")

hamberger.addEventListener('click', ()=>{
  hamberger.classList.toggle("active")
  sidebar.classList.toggle("in")
})