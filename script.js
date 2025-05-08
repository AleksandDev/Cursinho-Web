const inputName = document.querySelector("input#nome");
const inputEmail = document.querySelector("input#email");
const botao = document.querySelector("button#submit");
const linguagens = document.querySelectorAll("input#[checkbox-linguagens]");
const conheceu = document.querySelector("input#[radio-conheceu]");

function validarCampos() {

    const nomeValido = inputName.value.trim() !== "";
    const emailValido = inputEmail.value.trim() !== "";

    if (!nomeValido && !emailValido) {
        alert("O nome e o email não podem ser vazios!");
    } else if (!nomeValido) {
        alert("O nome não pode ser vazio!");
    } else if (!emailValido) {
        alert("O email não pode ser vazio!");
    } else {
        alert("Todos os campos foram preenchidos com sucesso!");
    }
}

botao.addEventListener("click", validarCampos);