function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')
    if(fano.value.length == 0 || fano.value > ano){
        alert('ERRO: Verifique os dados')
    }else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - fano.value
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if(fsex[0].checked){
            genero = 'Homem'
            if(idade >=0 && idade < 10){
                //Criança
                img.setAttribute('src', 'img/Hbebe.png')
            }else if(idade < 21){
                //Jovem
                img.setAttribute('src', 'img/Hjovem.png')
            }else if(idade < 50){
                //Adulto
                img.setAttribute('src', 'img/Hadulto.png')
            }else{
                //Idoso
                img.setAttribute('src', 'img/Hvelho.png')
            }
        }else if (fsex[1].checked){
            genero = 'Mulher'
            if(idade >= 0 && idade < 10){
                //Criança
                img.setAttribute('src', 'img/Mbebe.png')
            }else if(idade < 21){
                //Jovem
                img.setAttribute('src', 'img/Mjovem.png')
            }else if(idade < 50){
                //Adulta
                img.setAttribute('src', 'img/Madulta.png')
            }else{
                //Idosa
                img.setAttribute('src', 'img/Mvelha.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `${genero} com ${idade} anos`
        res.appendChild(img)
    }
}