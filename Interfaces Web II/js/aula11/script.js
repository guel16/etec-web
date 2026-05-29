const formulario = document.getElementById('form-recruta');
const inputName = document.getElementById('input-nome');
const inputCodigo = document.getElementById('input-codigo');

formulario.addEventListener('submit', (event) => {
    event.preventDefault();

    const nomeDigitado = inputName.value.trim();
    const codigoDigitado = inputCodigo.value.trim();

    let temErro = false;
    // Validacao de Nome
    if (nomeDigitado === "") {
        document.getElementById('erro-nome').classList.remove('hidden');
        inputName.classList.add('input-error');
        temErro = true;
    }
    else {
        document.getElementById('erro-nome').classList.add('hidden');
        inputName.classList.remove('input-error');
    }
    // Validacao de codigo
    if (codigoDigitado.lengh < 6) {
        document.getElementById('erro-codigo').classList.remove('hidden');
        inputCodigo.classList.add('input-error');
        temErro = true;
    }
    else {
        document.getElementById('erro-codigo').classList.add('hidden');
        inputCodigo.classList.remove('input-error')
    }

    if (temErro === false) {
        document.getElementById('msg-sucesso').classList.add('hidden');

        inputName.value = "";
        inputCodigo.value = "";
    }
    else {
        document.getElementById('msg-sucesso').classList.add('hidden')
    }
})

