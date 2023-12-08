let luna = document.getElementById('luna');
let nubes = document.getElementById('nubes');
let tocayos = document.getElementById('tocayos');
let btn = document.getElementById('btn');
let boat = document.getElementById('boat');
let agua = document.getElementById('agua');

window.addEventListener('scroll', function(){
    let value = window.scrollY;
    luna.style.top = value + 1.05 + 'px';
    nubes.style.top = value + 0.5 + 'px';
    tocayos.style.marginRight = value + 100 + 'px';
    boat.style.marginLeft = value + 100 + 'px';
    btn.style.marginTop = value + 1.5 + 'px';
})