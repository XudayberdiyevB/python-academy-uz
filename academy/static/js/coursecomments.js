var reply = document.querySelectorAll('.reply');
//var replydisplay = document.querySelectorAll('.replydisplay');

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

//document.querySelector("#cpa-form").submit(function(e){
//     if(!valid) {
//      e.preventDefault();
//    }
//})



//var a = reply.length;
//console.log(a);
//for(i=0; i<a; i++){
//    var replydisplay = document.getElementById('replydisplay');
//    reply.addEventListener('click', function(){
//        console.log('ok');
//        console.log(i);
//        if(replydisplay.style.display == 'none'){
//            replydisplay.style.display = 'block';
//        }
//        else{
//            replydisplay.style.display = 'none';
//        }
//    })
//}