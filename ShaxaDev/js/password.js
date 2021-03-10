var kurish = document.querySelector('.kurish')
var password = document.getElementById('password')
    kurish.addEventListener('click',function(){
    
        if(password.type === 'text') {
            password.type = 'password'
        }
        else {
            password.type = 'text'
        }
    })