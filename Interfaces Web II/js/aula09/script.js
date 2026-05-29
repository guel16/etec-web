const titulo = document.getElementById('titulo');
// Alterando texto
titulo.innerText = 'Você está na Matrix.'

titulo.style.color = '#fff'

const areaAgentes = document.getElementById ('agentes');

const dadosAgentes = [
    {nome: 'Agentes Smith' ,  fotos: 'https://upload.wikimedia.org/wikipedia/pt/thumb/1/1f/Agent_Smith_%28The_Matrix_series_character%29.jpg/250px-Agent_Smith_%28The_Matrix_series_character%29.jpg'},
    {nome: 'Agentes Jones' ,  fotos: 'https://i.pinimg.com/474x/78/9d/dc/789ddc773ce8ce58ce6d77f8e2e1cc57.jpg'}
];

dadosAgentes.forEach ((agente) => {
    // Cria uma div vazia
    const novoCard = document.createElement ('div');
    // classe aplica dentro do css
    novoCard.className = 'card';

    // InnerHtml preenche o card com diferentes tags
    novoCard.innerHTML = `
    <img src= "${agente.fotos}" alt="${agente.nome}">
    <p>${agente.nome}</p>
    `

    areaAgentes.appendChild (novoCard);
});

// Exercicios
titulo.innerText = 'Ola, Neo'

// 02
const body = document.querySelector('body');

body.style.backgroundColor = '#0a0a0a'

// 03
const paragrafo = document.createElement ('p');
paragrafo.innerText = 'Eu já estive aqui...';

paragrafo.appendChild ('p')