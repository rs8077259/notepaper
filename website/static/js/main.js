if ('serviceWorker' in navigator){
    window.addEventListener('load',function(){
        this.navigator.serviceWorker.register('/sw.js')
        .then(reg=>{
            console.log('Registered',reg);
        }).catch(err=>{
            console.log("registration failed",err);
        })
    })
}
//raj