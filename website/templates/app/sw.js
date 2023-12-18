let cacheName= 'cache-v2';
let resourcesToPreCache=[
    '/',
    '/static/css/home.css',
    '/static/css/poster.css',
    '/static/images/logo.jpg',
    '/static/images/logo.png',
    '/sw.js',
    '/static/js/main.js',
    '/error/offline/',
    '/static/css/offline.css',
    '/static/images/offline.svg',
];
self.addEventListener('install',function(event){
    self.skipWaiting();
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
self.addEventListener('activate',event=>{
    console.log("updated service worker is now activated");
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
})//rj
