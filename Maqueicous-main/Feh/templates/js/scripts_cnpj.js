var cnpj = "77.180.345/0001-07"
function validaCnpj(cnpj) {
    let numeros = cnpj.split("-")[0].replace(/[.|\/]/g, "");
    console.log(numeros);
    let digitos = cnpj.split("-")[1];
    console.log(digitos);
    if (primeiroDigito(numeros) != digitos[0]) {
        return "CNPJ1("+cnpj+") - Invalido"; 
    }
    if (segundoDigito(numeros+""+digitos[0]) != digitos[1]) {
        return "CNPJ2("+cnpj+") - Invalido"; 
    }
    return "CNPJ("+cnpj+") - Valido"; 
}

function primeiroDigito(numeros) {
    let peso = 2;
    let resultado=0;
    for (let i = numeros.length-1; i >= 0; i--) {
        resultado += numeros[i] * peso;
        peso = (peso == 9 ? 2: peso+1);
    }
    modulo = resultado % 11;
    console.log(modulo)
    resultado = (modulo < 2 ? 0 : 11 - modulo)
    return resultado;
}

function segundoDigito(numeros) {
    let peso = 2;
    let resultado=0;
    for (let i = numeros.length-1; i >= 0; i--) {
        resultado += numeros[i] * peso;
        peso = (peso == 9 ? 2: peso+1);
    }
    modulo = resultado % 11;
    resultado = (modulo < 2 ? 0 : 11 - modulo)
    return resultado
}