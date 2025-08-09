// parte para validar os campos do formulário
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

// Função para alternar o menu
function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('show');
}

// parte para o carrossel dos cursos
let slideAtual = 0;
    const slides = document.querySelectorAll('.carrossel-slide');
    const indicadores = document.querySelectorAll('.indicador');

    function mostrarSlide(index) {
        if (index >= slides.length) {
            slideAtual = 0;
        } else if (index < 0) {
            slideAtual = slides.length - 1;
        } else {
            slideAtual = index;
        }

        slides.forEach(slide => slide.classList.remove('ativo'));
        indicadores.forEach(indicador => indicador.classList.remove('ativo'));

        slides[slideAtual].classList.add('ativo');
        indicadores[slideAtual].classList.add('ativo');
    }

    function moverCarrossel(direcao) {
        mostrarSlide(slideAtual + direcao);
    }

    function irParaSlide(index) {
        mostrarSlide(index);
    }

    mostrarSlide(slideAtual);