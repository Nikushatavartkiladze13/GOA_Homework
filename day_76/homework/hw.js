let decrease = document.getElementById("dicrease")
let increase = document.getElementById("increase")
let number = document.getElementById("number")
let reset = document.getElementById("reset")
function incr(){
    number.innerHTML = Number(number.innerHTML)+1
}
function decr(){
    number.innerHTML = Number(number.innerHTML)-1
}
function res(){
    number.innerHTML = Number(0)
}
increase.addEventListener('click', incr)
decrease.addEventListener('click', decr)
reset.addEventListener('click', res)