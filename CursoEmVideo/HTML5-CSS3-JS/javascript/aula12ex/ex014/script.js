function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('img')
    var data = new Date()
    var hora = data.getHours()
    //var hora = 5
    msg.innerHTML = `Agora são ${hora} horas`
    if(hora > 0 && hora < 12){
        // Bom dia
        img.src = 'img/manha.png'
        document.body.style.background = '#f5c984'
    }else if(hora >= 12 && hora <= 18){
        // Boa tarde
        document.body.style.background = '#a0bbce'
        img.src = 'img/tarde.png'
    }else{
        // Boa noite
        img.src = 'img/noite.png'
        document.body.style.background = '#313131'
    }

}