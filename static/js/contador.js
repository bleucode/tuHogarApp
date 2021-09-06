const color=document.getElementById('fondo_color')
const numero=document.getElementById('numero')

let cantidad=0
let tiempo=setInterval(() => {
    cantidad+=1
    color.style.height=`${cantidad}%`
    numero.textContent=cantidad
    if(cantidad===100){
        clearInterval(tiempo)
    }
}, 100);