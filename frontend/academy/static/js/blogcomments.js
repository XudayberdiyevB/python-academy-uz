var reply = document.querySelectorAll('.reply');
// var replydisplay = document.querySelectorAll('.replydisplay');

reply.forEach(function(item){
    item.addEventListener('click',function(event){
        var ss = item.nextElementSibling
        console.log('ok')
//        ss.classList.toggle('show')
        if(ss.classList.contains('show')){
            ss.classList.remove('show')
        }
        else {
            ss.classList.add('show')
        }
    })
})
