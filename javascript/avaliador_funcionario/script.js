function avaliarfuncionario(){
    let nome = document.getElementById("nome").value
    let anos = Number(document.getElementById("anos").value)
    let slario = Number(document.getElementById("salario").value)
    let nivel;
    let bonus;
    let pagamentos;
    if (anos < 2){
        nivel = "Junior"
    }
    else if (anos <= 5){
        nivel = "Plenor"
    }
    else{
        nivel = "Senior"
    }
    if (salario > 2500){
        bonus = 300
        pagamentos = slario + bonus
    }
    else{
        bonus = 0
        pagamentos = slario + bonus
    }
    document.getElementById("resultado").innerHTML = `
    <h2> Resultado </h2>
     <p>Funcionário ${nome}</p>
      <p>Nivel: ${nivel}</p>
       <p>Salário: ${slario.toFixed(2)}</p>
        <p>Bonus: ${bonus.toFixed(2)}</p>
         <p>Pagamentos: ${pagamentos.toFixed(2)}</p>
    `
}