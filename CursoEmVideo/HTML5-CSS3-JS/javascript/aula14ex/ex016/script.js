function contar(){
    var inicio = document.querySelector('input#inicio')
    var fim = document.querySelector('input#fim')
    var passo = document.querySelector('input#passo')
    var res = document.querySelector('div#res')
    if(inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        res.innerHTML = 'ERRO: Não foi possível contar, verifique os dados'
    }else{
        res.innerHTML = `Contando: <br>`
        var i = Number(inicio.value)
        var f = Number(fim.value)
        var p = Number(passo.value)
        if(p <= 0){
            alert('ERRO: Passo inválido. OK para passo 1')
            p = 1
        }
        if(i < f){
            for(let c = i; c <= f; c += p){
                res.innerHTML += `${c} `
            }
        }else{
            for(let c = i; c >= f; c -= p ){
                res.innerHTML += `${c} `
            }
        }    
    }
}