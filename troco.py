# Escreva um algoritmo que retorne um TROCO de qualquer valor. As notas possíveis são 200, 100, 50, 20, 10, 5 e 2 reais.
# A função objetivo é retornar a menor quantidade de notas possível.

def obterTroco(valor):

  notas = [200, 100, 50, 20, 10, 5, 2];

  notasDevolvidas = [];
  
  while((valor - somaNotas(notasDevolvidas)) > 0):
  
    maiorNota = 0;

    notaAtual = 0;
    
    for nota in notas:
      if (nota > maiorNota) and (valor - (somaNotas(notasDevolvidas) + nota)) >= 0:
        notasDevolvidas.append(nota);
        notaAtual = nota;
        break;

    if notaAtual == 0:
      break;

  print("Troco: ", notasDevolvidas)

def somaNotas(notas):

  somatoria = 0;
  
  for nota in notas:
    somatoria += nota;

  return somatoria;