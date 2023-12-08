var startX=0
var startXTimestamp=0
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
    startXTimestamp=event.timeStamp;
}
function handleTouchEnd(event){
    console.log(event.timeStamp-startXTimestamp);
    if(event.timeStamp-startXTimestamp>210)
        return
    let move=event.changedTouches[0].clientX-startX
    if(startX<=0+50)
        if ((move>=-10&&move!=0) && chapterListOpen==false){
            chapterlist.style.left = '0px';
            chapterListOpen=true
        }
    if(startX>=viewportWidth-50)
        if((move<=10&&move!=0) && headingListOpen==false){
        headingList.style.right = '0px';
        headingListOpen=true;
    }
}