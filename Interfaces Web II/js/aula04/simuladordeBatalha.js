const ForcaNavio = prompt("Qual é a força do navio? (um numero de 1 a 10)");
const numeroTripulantes = prompt("Qual é a quantidade de tripulantes inimigos? ");
const marCalmo = confirm("O mar está calmo?")
const nossaForca = 8; 
const podemosVencer = (nossaForca > ForcaNavio && numeroTripulantes < 50) || marCalmo; 
if (podemosVencer === true) {
    console.log (`Voce venceu: ${podemosVencer}`)
}
else{
    console.log (`Voce perdeu: ${podemosVencer}`)
}
