var reply = document.querySelectorAll('.reply');
var a = reply.length;
console.log(a);
for(i=0; i<a; i++){
    var replydisplay = document.getElementById('replydisplay');
    reply.addEventListener('click', function(){
        console.log('ok');
        console.log(i);
        if(replydisplay.style.display == 'none'){
            replydisplay.style.display = 'block';
        }
        else{
            replydisplay.style.display = 'none';
        }
    })
}