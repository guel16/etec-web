const mensagem = document.getElementById ('mensagem-joyce');
// MANIPULA O TEXTO DO HTML (PRIORIDADE\)
mensagem.innerText = 'ESTOU AQUI';
// MANIPULA A COR DO ELEMENTO DO HTML
mensagem.style.color = '#eab308';
// QUERY PEGA APENAS O PRIMEIRO ELEMENTO
const laboratorio = document.querySelector ('#laboratorio-halkins');
laboratorio.style.backgroundcolor = 'rgba(20 , 0, 0, 0.5)';
// o ALL pega todos os elementos e retorna dentro da lista
const membrosClube = document.querySelectorAll('.membro');
// O LAÇO DO FOREACH
membrosClube.forEach ((membro) => {
    membro.innerText += '(Presente)';
    membro.style.color = '#818cf8';
    console.log (membrosClube)
})

// pratica
const titulo = document.getElementById ('titulo');
titulo.innerText = 'Portal Aberto'

// 02
const quantidade = document.getElementsByClassName ('membro')
console.log (quantidade.length)

// 03
const monstro = document.querySelector ('.monstro');
 alert (monstro.textContent)

console.log (laboratorio)
console.log (monstro)

// 04
const selecionarLista =  document.querySelectorAll ('.membro');
selecionarLista.forEach ((lista) => {
    console.log ('Bem-Vindo');
})