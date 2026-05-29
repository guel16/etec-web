// ARRAY
aliancaRebelde = ["Luke Skywalker", "Leia Organa", "Han Solo"];
console.log ("Esquadrao inicial:", aliancaRebelde);
console.log (aliancaRebelde[1])
// Adicionando um novo membro finalcom push ()
aliancaRebelde.push ("Chewbacca");
console.log ("Reforços chegaram:", aliancaRebelde)

// Adicionando um memnro de inicio com .unshift()
aliancaRebelde.unshift("Landro Calrissian");
console.log("Um velho amigo se juntou à causa: ", aliancaRebelde[0])
// Removendo o ultimo .pop()
aliancaRebelde.pop();
console.log ("Chwie foi consertar a Falcon...", aliancaRebelde)

// Removendo o primeiro membro com .shift()
aliancaRebelde.shift();
console.log ("Lando foi cuidade de Bespin...", aliancaRebelde)
// Objetos
const millenniumFalcon = {
    nome: "Millennium Falcon",
    piloto: "Han Solo",
    "ano de fabricacao": 60 //Bby 
}
millenniumFalcon.copiloto = "Chewbacca"
console.log ("Ano:", millenniumFalcon['ano de fabricacao'])

// Verificacao se uma propriedade existe
const temHyperdrive = 'hiperdryve' in millenniumFalcon;
console.log (`A nave possui um hyperdryve? ${temHyperdrive}`)

const droids = [
    {nome: "R2-D2", funcao: "Astromecânico"},
    {nome: "C-3PO", funcao: "Protocolo"}
]
droids[0].funcao = "Herio Aliança"
console.log ("Função do R2-D2 atualizada: ", droids[0])