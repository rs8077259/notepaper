


self.addEventListener('activate',function(event){
    console.log("active event");
})
self.addEventListener('fetch',function(event) {
    console.log(Fetch);    
})

let cacheName= 'cache-v2';
let resourcesToPreCache=[
    '/',
    '/static/css/home.css',
    '/static/css/poster.css',
    '/static/images/logo.jpg',
    '/static/images/logo.png',
    '/error/offline/',
    '/static/css/offline.css',
    '/static/images/offline.svg',
];
self.addEventListener('install',function(event){
    console.log("install event");
    event.waitUntil(
        caches.open(cacheName)
        .then(cache=>{
            console.log("added all");
            return cache.addAll(resourcesToPreCache)
        }).catch(err=>{
            console.log(err);
        })
    )
})

self.addEventListener('fetch',
event=>{
    console.log("here i am ");
    event.respondWith(caches.match(event.request)
    .then(cachedResponse=>{
        if (cachedResponse){
            console.log("here")
            return cachedResponse||fetch(event.request);
        }}
    ))
})
