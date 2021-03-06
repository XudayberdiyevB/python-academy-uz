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

