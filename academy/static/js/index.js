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

// #### FAQs
const items = document.querySelectorAll(".accordion button");

function toggleAccordion() {
  const itemToggle = this.getAttribute('aria-expanded');

  for (i = 0; i < items.length; i++) {
    items[i].setAttribute('aria-expanded', 'false');
  }

  if (itemToggle == 'false') {
    this.setAttribute('aria-expanded', 'true');
    console.log('ok')
  }
}

items.forEach(item => item.addEventListener('click', toggleAccordion));
// #### FAQs