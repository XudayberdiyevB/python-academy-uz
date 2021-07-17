// dropdown click
var dropx = document.querySelector('.dropx')

var boxX = document.querySelector('.boxX')

dropx.addEventListener('click',function(){
    if(boxX.classList.contains('active')){
        boxX.classList.remove('active')
    }
    else {
        boxX.classList.add('active')
    }
})

var suppchatopen = document.querySelector('.comment')
var suppchatclose = document.querySelector('.close')
var wr = document.querySelector('.wrapper')
suppchatopen.addEventListener('click', function(){
    wr.style.visibility='visible'
})
suppchatclose.addEventListener('click', function(){
    wr.style.visibility='hidden'
})