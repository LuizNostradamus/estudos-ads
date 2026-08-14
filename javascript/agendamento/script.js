let sala = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

function reservar(linha, coluna, cadeira){
    if (sala[linha][coluna] == 0){
        sala[linha][coluna] = 1
        cadeira.style.background="red"

        document.getElementById("mensagem").innerText=
        "Cadeira reservada"

        
    }
    else if(sala[linha][coluna] == 1){
        sala[linha][coluna] = 1
        cadeira.style.background="red"
        document.getElementById("mensagem").innerText=
        "Cadeira já está reservada"
    }
    else{
        (sala[linha][coluna] = 0)
        cadeira.style.background="green"
        document.getElementById("mensagem").innerText=
        "Cadeira já está reservada"
    }
}