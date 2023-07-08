const hamberger = document.querySelector(".hamberger")
const sidebar = document.querySelector("#sidebar")
let appear = false

hamberger.addEventListener('click', ()=>{
  appear = !appear
  hamberger.classList.toggle("active")
  if(appear){
    sidebar.classList.toggle("appear")
    setTimeout(() => {
      sidebar.classList.toggle("in")
    }, 100)
  }else{
    sidebar.classList.toggle("in")
    setTimeout(() => {
      sidebar.classList.toggle("appear")
    }, 500)
  }
})