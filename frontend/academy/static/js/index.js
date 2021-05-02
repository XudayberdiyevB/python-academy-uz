// dropdown click
var dropx = document.querySelector('.dropx')

var boxX = document.querySelector('.boxX')

dropx.addEventListener('click',function(){
    console.log('bosildo');
    if(boxX.classList.contains('active')){
        boxX.classList.remove('active')
    }
    else {
        boxX.classList.add('active')
    }
   
})

var btnMenu = document.querySelector('.btn-menu')
var menuShow = document.querySelector('.menu-show')
console.log(menuShow);
// btnMenu.addEventListener('click',function(){
    
// })
