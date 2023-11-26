let num = document.querySelector('input#fnum')
let lista = document.querySelector('select#flista')
let res = document.querySelector('div#res')
let valores = []

// verifica se o número esta entre 1 e 100
function isNumero(n){ 
    if(Number(n) >= 1 && Number(n) <= 100){
        return true
    }else {
        return false
    }
}

// verifica se o número já esta na lista
function inLista(n, l){
    if(l.indexOf(Number(n)) != -1){
        return true
    }else {
        return false
    }
}

/* chama as funções para verificação;
   adiciona o número a array valores;
   cria e mostra os numeros na caixa lista;
*/
function adicionar(){
    if(isNumero(num.value) && !inLista(num.value, valores)){
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `valor ${num.value} adicionado`
        lista.appendChild(item)
        
    }else {
        window.alert('Valor inválido ou já listado.')
    }
    num.value = '' // limpa os resultados
    num.focus()    // mantem o cursor na caixa de inclusão
}

// escreve os resultados apos clicar em finalizar
function finalizar(){
    if(valores.length == 0){
        window.alert('Não há valores inseridos.')
    }else {
        let tot = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let soma = 0
        let media = 0
        for(pos in valores){
            soma += valores[pos]
            if(valores[pos] > maior)
                maior = valores[pos]
            if(valores[pos] < menor)
                menor = valores[pos]
            
        }
        media = soma/tot
        res.innerHTML = ''
        res.innerHTML += `<p>Temos ${tot} valores cadastrados`
        res.innerHTML += `<p>O maior valor é ${maior}`
        res.innerHTML += `<p>O menor valor é ${menor}`
        res.innerHTML += `<p>A soma é ${soma}`
        res.innerHTML += `<p>A media é ${media}`
    }
}