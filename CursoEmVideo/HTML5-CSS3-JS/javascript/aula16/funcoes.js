// recebe um parametro e retorna o resultado
function parimp(n) {
    if(n % 2 == 0){
        return 'par'
    }else{
        return 'impar'
    }
}
let res = parimp(6)
console.log(`O numero digitado é ${res}`)