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

// let a = document.querySelector('.a')

// a.addEventListener('click',function(event){
//     if(this.hash !== ""){
//         event.preventDefault();
//         var hash = this.hash

//         function(){
//             window.location.hash = hash
//         }
//     }
// })

// -------------------------
// jquiry smooth scroll
// Add smooth scrolling to all links
