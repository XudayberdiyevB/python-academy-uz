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

// back to top btn
var btn = document.querySelector('#back-top-button');

document.querySelector(window).scroll(function() {
  if (document.querySelector(window).scrollTop > 300) {
    btn.classList.add('show');
  } else {
    btn.removeClass('show');
  }
});

btn.addEventListener('click', function(e) {
  e.preventDefault();
  document.querySelector('html, body').animate({scrollTop:0}, '300');
});