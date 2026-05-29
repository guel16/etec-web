const pokedexPreview= document.getElementById('live-pokedex-preview');
const cintoPreview= document.getElementById('live-cinto-preview');
const arenaPreview = document.getElementById('live-arena-preview');
const btnFugir = document.getElementById('btn-fugir');
console.log (pokedexPreview);
console.log (cintoPreview);
console.log (arenaPreview);
console.log (btnFugir);

// forEach Laço
const pokemonData = [
    {nome:'Bubasauro' , tipo:'Planta/Veneno', imagem:'1', cor:'bg-green-100 border-green-300'},
    {nome:'Charmander' , tipo:'Fogo ', imagem:'4', cor:'bg-red-100 border-red-300'},
    {nome:'Squardle' , tipo:'Agua', imagem:"7", cor:'bg-blue-100 border-blue-300'},
    {nome:'Blastoise' , tipo:'Agua', imagem:"9", cor:'bg-blue-100 border-blue-300 '},
    {nome:'Fearow' , tipo:'Normal/Voador', imagem:"22", cor:'bg-grey-80 border-white-330 '},
    {nome:'Weedle' , tipo:'Inseto/Venenoso', imagem:"13", cor:'bg-purple-100 border-purple-300 '},
    {nome:'Electrode' , tipo:'Eletrico', imagem:"101", cor:'bg-yellow-100 border-yellow-300 '},
    {nome:'Lapras' , tipo:'Agua/Gelo', imagem:"131", cor:'bg-blue-100 border-blue-300 '},
    {nome:'Starmie' , tipo:'Agua', imagem:"121", cor:'bg-blue-100 border-blue-300 '},
];

pokemonData.forEach ((pkmn) => {
    console.log(pkmn);
    const card = document.createElement ('div');
    card.className = `flex cursor-pointer flex-col items-center rounded-x1 border p-4 shadow-sm transition-transform hover:-translate-y-1 ${pkmn.cor}`;
    card.innerHTML = `
    <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pkmn.imagem}.png"
    alt="${pkmn.nome}" class="h-24 w-24 drop-shadow-md">
    <h3 class="mt-2 text-lg font-bold text-slate-800>${pkmn.nome}</h3>
    <span class="text-xs font-bold uppercase tracking-wider text-slate-600
    opacity-80">${pkmn.tipo}</span>
    `;



    pokedexPreview.appendChild(card);
});
