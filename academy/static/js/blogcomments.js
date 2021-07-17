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

// star-rating
var rating = document.querySelector(".rating");
var ratingDisplayEle = document.querySelector(".rating-display");
//add event listener
function clickStar(ele){
  var clickedStar = ele;
  //value of the star
  var ratingValue = parseInt(clickedStar.getAttribute("value"));
  //change the color of the star
  for(var i=0; i<ratingValue; i++){
    rating.children[i].classList.add("clicked");
    for(var j=ratingValue; j<=4; j++){
      if(rating.children[j].classList.contains("clicked")){
        rating.children[j].classList.remove("clicked");
      }
    }
  }
}

//function to calculate rating
function calculateRating(ele){
  //check how many elements are having clicked class
  var ratingCount = 0;
  for(var i=0; i<ele.children.length; i++){
    if(ele.children[i].classList.contains("clicked")){
      ratingCount++;
    }
  }
  ratingDisplayEle.textContent = `Siz 5 dan ${ratingCount} ni tanladingiz`;
}