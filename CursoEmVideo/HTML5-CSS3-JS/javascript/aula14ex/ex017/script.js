function geratab(){
    var num = document.querySelector('input#num')
    var res = document.querySelector('select#tab')
    if(num.value.length == 0){
        alert('ERRO: Digite um numero')
    }else{
        n = Number(num.value)
        res.innerHTML = ''
        for(var c = 1; c <= 10; c++){
            let item = document.createElement('option')
            item.text = `${n} X ${c} = ${n * c}`
            item.value = `res${c}`
            res.appendChild(item)
        }
    }
}