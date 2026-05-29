let localizacaoAtual = "Torre dos Vingadores";
 console.log ("Equipe reportando de: ", localizacaoAtual);

localizacaoAtual = "Wakanda"; //O valor de 'let' pode mudar. 
console.log ("Nova localização:", localizacaoAtual)

// PROMPT É A MENSAGEM QUE O JS EXOBE NA TELA DO USUARIO

const lider = "Capitão América"; // 'const' é fixo

 alert("Iniciando protocolo de Recrutamento de Novos Vingadores");

const nomeRecruta = prompt ("Qual é o codinome de herói?");
 const poderRecruta = prompt ("Descreva o poder primcipal: ");

 const aceitaTermos = confirm("Você jura proteger a Terra E SEGUIR AS ORDENS DA S.H.I.E.L.D?");

 console.log (
    `--FICHA DE RECRUTAMENTO--
    Codinome: $(nomeRecruta)
    Poder: ${poderRecruta}
    Aceitou os termos: ${aceitaTermos}
    `
);

 alert ("Recruta" + nomeRecruta + ", seus dados foram enviados para o Nick Fury. Aguarde.");

//  EXERCICIOS JAVA SCRIPT
let meuVingador = "Homem de Ferro";
const joiasDoInfinito = 6;
const hulkEsmaga = true;
 console.log (
    `--FICHA DE RECRUTAMENTO--
    Meu vingador favorito: ${meuVingador}
    Joias do infinito: ${joiasDoInfinito}
    Hulk esmaga?: ${hulkEsmaga}
-----------------------------------------------
    `
);


const nomeAgente = "Miguel";
let nivelAgente = 17;
console.log (`Agente ${nomeAgente} tem nivel de acesso de ${nivelAgente}`);

const identidade = "Peter Parker";
console.log (identidade);

identidade = "Tony Stark";


// Desafio final
const nomePersonagem = prompt("Qual é o seu personagem? ");
const planetaOrigem = prompt ("Qual é o planeta de origem ? ");
const vilao = confirm ("Seu personagem é um vilão? ");
if (vilao) {
    alert (`ALERTA VERMELHO!: ${nomePersonagem} do planeta ${planetaOrigem} é uma ameaça!`);
}
else{
    alert(`RELATORIO: ${nomePersonagem} do planeta ${planetaOrigem} é um aliado potencial! `);
}