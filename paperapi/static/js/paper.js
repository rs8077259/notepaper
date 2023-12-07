var startX=0
var chapterListOpen=false
var headingListOpen=false;
let viewportWidth=window.innerWidth
var container = document.querySelector('.content-area');
var chapterlist = document.querySelector('.chapter-list');
var headingList = document.querySelector('.heading-list');
console.log(window)
container.addEventListener('touchstart', handleTouchStart);
container.addEventListener('touchend', handleTouchEnd);

function handleTouchStart(event) {
    startX = event.touches[0].clientX;
    currentX = startX;
}
function handleTouchEnd(event){
    console.log(viewportWidth)
    console.log(startX);
    let move=event.changedTouches[0].clientX-startX
    console.log(move)
    if(startX>=viewportWidth-50 || startX<=0+50)
    if ((move>=-10&&move!=0) && chapterListOpen==false){
        chapterlist.style.left = '0px';
        chapterListOpen=true
    }
    else if((move<=10&&move!=0) && headingListOpen==false){
        console.log(headingList)
        headingList.style.right = '0px';
        headingListOpen=true;
    }
}