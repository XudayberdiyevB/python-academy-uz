var kurish = document.querySelector('.kurish')
var password = document.getElementById('password')
var show = document.querySelector('.fa-eye')

var hide = document.querySelector('.fa-eye-slash')
    kurish.addEventListener('click',function(){
        
        if(password.type === 'text') {
            password.type = 'password'
            show.style.display = 'block'
            hide.style.display = 'none'
        }
        else {
            password.type = 'text'
            show.style.display = 'none'
            hide.style.display = 'block'
        }
    })

     