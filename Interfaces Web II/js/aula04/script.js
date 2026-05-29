const recompensaLuffy = 3000000000;
const recompensaZoro = 1111000000;

const recompensaTotal = recompensaLuffy + recompensaZoro;
console.log ("Recompensa combinada do Capitão e Imediato:", recompensaTotal);

const recompensaBuggy = 3189000000000;
const luffyMaisForte = recompensaLuffy > recompensaBuggy;

console.log (`A recompensa do Luffy é maior que a do Biggy?: ${luffyMaisForte}`);

const nomeDoTesouro = "One Piece";
console.log ("Este é o tesouro verdadeiro? :", nomeDoTesouro === "One Piece")

const temComida = true;
const temNavegador = true;
const marinhaPorPerto = false;

const podeNavegar = temComida && temNavegador;
console.log (`Podemos zapar para a próxima ilha?  ${podeNavegar}`)

const podeFestejar = temComida || recompensaLuffy > 0;
console.log (`Bora ter um banquete? ${podeFestejar}`);

const estamosSeguros = !marinhaPorPerto;
console.log (`A costa está limpa? ${estamosSeguros} `);