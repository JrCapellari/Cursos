var num = [5, 8, 4]
num[3] = 6 // add o valor 6 no indice 3
num.push(7) // add o valor 7 na ultima posição
console.log(num)
num.sort() // organiza os valores
console.log(`Vetor em ordem fica ${num} e possui ${num.length} elementos`)
console.log('---------------------------------------------------')
/*for(var pos = 0; pos < num.length; pos++){
    console.log(`Posição ${pos} tem valor ${num[pos]}`)
}
console.log('---------------------------------------------------')
*/
// Busca otimizada (somente) para arrays e objetos
for(var pos in num){
    console.log(`Posição ${pos} tem valor ${num[pos]}`)
}
console.log('---------------------------------------------------')
var valor = 8
var posicao = num.indexOf(valor)
if(posicao == -1){
    console.log('Valor não encontrado')
}else{
    console.log(`A posição do valor ${valor} é ${posicao}`)
}