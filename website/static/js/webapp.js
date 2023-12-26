let activeMenuButton = document.getElementById("home-button")//current menu that is open
const loaderContainer = document.getElementById('buffer-animation-container')
const mainContainer = document.getElementById('main-content')
let page=1;
let currentMenu='';
function changeMenuColor(menuButtonToActivate) {
    //change the color of menu when activation stage changes
    activeMenuButton.getElementsByClassName('menu-icon')[0].style.color = 'black';
    activeMenuButton.getElementsByClassName('icon-button-text')[0].style.color = 'black';
    activeMenuButton.getElementsByClassName('icon-button-text')[0].style.backgroundColor = 'inherit';
    activeMenuButton = menuButtonToActivate;
    activeMenuButton.getElementsByClassName('menu-icon')[0].style.color = 'rgb(77, 201, 250)';
    activeMenuButton.getElementsByClassName('icon-button-text')[0].style.backgroundColor = 'rgb(77, 201, 250)';
    activeMenuButton.getElementsByClassName('icon-button-text')[0].style.color = 'whitesmoke'
}
function requestAsset(domElement) {
    let dataurl=`http://127.0.0.1:8000/api/note?page=${page}&perpage=5`
    if (navigator.onLine) {
        loaderContainer.innerHTML = '<span class="loader" id="loader"></span>';
        fetch(dataurl, { 'method': 'get' })
            .then(response => response.json())
            .then(data => {
                loaderContainer.innerHTML = ''//removig loader annimiation
                data.forEach(element => {
                    mainContainer.insertAdjacentHTML('beforeend',`<a href="${element.url}"><div class="poster">\
                    <img src="${element.imgUrl}" class="poster-img">\
                    <div class="poster-tags">\
                        root\
                    </div>\
                    <h2 class="poster-heading">${element.title}</h2>\
                    <p class="poster-content">${'hello'}</p>
                    </div><\a>`);
                });

            })
            .catch(err => {
                loaderContainer.innerHTML = "<p>some error happened when requesting content please try again</p><button id='retry-button'>retry</button>"
                document.getElementById('retry-button').addEventListener('click', event => {
                    requestAsset(domElement);
                })
            })
    }
    else {
        loaderContainer.innerHTML = "<p>you are offline please try again</p><button id='retry-button'>retry</button>"
        document.getElementById('retry-button').addEventListener('click', event => {
            requestAsset(domElement);
        })
    }
}

document.getElementById("home-button").addEventListener('click', changeMenu)

document.getElementById("downloads-button").addEventListener('click', changeMenu)

document.getElementById("write-button").addEventListener('click', changeMenu)

document.getElementById("menu-button").addEventListener('click', changeMenu)


function changeMenu(event) {
    currentMenu=this;
    changeMenuColor(this)
    requestAsset(this);
}
changeMenuColor(document.getElementById("home-button"))
requestAsset(document.getElementById("home-button"));




//scrollbar

let element=document.querySelector('html')
document.addEventListener('scroll',event=>{
    if(element.scrollTop-500==((element.scrollHeight -element.clientHeight)-500)){
    page++;
    requestAsset(currentMenu);
    }
})