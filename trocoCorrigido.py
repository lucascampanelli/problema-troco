# Escreva um algoritmo que retorne um TROCO de qualquer valor. As notas possíveis são 200, 100, 50, 20, 10, 5 e 2 reais.
# A função objetivo é retornar a menor quantidade de notas possível.

def troco(valor):

  notas = [200, 100, 50, 20, 10, 5, 2];
  total = 0;
  notasDevolvidas = [];
  aDevolver = valor;

  for i in range(len(notas)):
    qntNotas = aDevolver // notas[i];

    ## Melhoria feita após sugestão do professor: Mostrar as notas que foram devolvidas.
    if(qntNotas > 0):
      notasDevolvidas.append(notas[i]);
    
    aDevolver -= qntNotas * notas[i];
    total += qntNotas;

  print("Notas devolvidas: ", notasDevolvidas);
  print("Total: ", total);