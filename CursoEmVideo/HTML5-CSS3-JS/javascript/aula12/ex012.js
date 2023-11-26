var idade = 14
console.log(`Você tem tem ${idade} anos`)
if(idade < 16){
    console.log('NÃO Vota')
}else if((idade >= 16 && idade < 18) || (idade >= 65)){
        console.log('Voto OPCIONAL')
    }else{
        console.log('Voto OBRIGATÓRIO')
    }