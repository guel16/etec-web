const salaPrecisa = document.getElementById('sala-precisa');
const btnLumos = document.getElementById('btn-lumos');

const pomoDeOuro = document.getElementById('pomo-de-ouro');

const diarioInpurt = document.getElementById('diario-input');
const diarioResposta = document.getElementById('diario-resposta');

btnLumos.addEventListener('click', () => {
    salaPrecisa.classList.toggle('lumos-active');

    if (salaPrecisa.classList.contains('lumos-active')) {
        btnLumos.innerHTML = 'NOX!';
    }
    else {
        btnLumos.innerText = 'LUMOS!'
    }
})

pomoDeOuro.addEventListener('mouseenter', () => {

    const novaPosicaoX = Math.random() * 80;
    const novaPosicaoY = Math.random() * 80;

    pomoDeOuro.style.left = `${novaPosicaoX}%`;
    pomoDeOuro.style.top = `${novaPosicaoY}%`;
})

diarioInpurt.addEventListener('input', (Event) => {
    const textoDigitado = event.target.value;

    if (textoDigitado === "") {
        diarioResposta.innerText = '...';
    }
    else {
        diarioResposta.innerText = `O diario absorveu ${textoDigitado}`;
    }

});
    const paragrafoPena = document.getElementById ('paragrafoPena');
    const btnPena = document.getElementById ('btn-pena');

    btnPena.addEventListener ('click', () => {
        if (paragrafoPena.classList.toggle ('cliqueBotao')) {
            paragrafoPena.innerText = 'A pena está voando'  
        }
        else {
            paragrafoPena.innerText = ""
        }
    })
const espelho = document.getElementById ('espelho-reflete')
 
espelho.addEventListener('mouseenter', () => {
    alert("Você ve o seu maior desejo!")
});
 
const imagemPoter = document.getElementById ('personagem');

imagemPoter.addEventListener ('mouseenter', () => {
    imagemPoter.src = ('https://static.wikia.nocookie.net/harrypotter/images/2/20/1480e49ef96ad1e935ae09bafc1fa152.jpg/revision/latest/scale-to-width-down/2000?cb=20210314195418&path-prefix=pt-br ') 
})
imagemPoter.addEventListener ('mouseleave' , () => {
    imagemPoter.src = ('"https://www.hola.com/horizon/original_aspect_ratio/5c68fd9cf9c5-harry-potter-daniel-radcliffe-dominic-mclaughlin-hbo-warner-bros-1.jpg">')
})