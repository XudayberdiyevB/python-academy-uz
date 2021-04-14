var reply = document.querySelector('.reply')
var replydisplay = document.getElementById('replydisplay')
    reply.addEventListener('click', function(){
        if(replydisplay.style.display == 'none')
            replydisplay.style.display = 'block';
        else
            replydisplay.style.display = 'none';
    })