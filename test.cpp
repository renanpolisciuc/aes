#include<stdio.h>
#include<iostream>
#include<string.h>
#include "aes.h"
#include "key_expansion.h"

using namespace std;

#define MAX_BUFFER_SIZE  536870912

//DEBUG
void printState(unsigned char * state, int size);

void printState(unsigned char * state, int size) {
  for(int i = 0; i < size; i++)
    printf("%X ", state[i]);
  cout << endl;
}

int main(int argc, char ** argv) {
  long buffSize = 0L, //Tamanho do arquivo
       bytesRead = 0L,
       fileSize = 0L; //Quantidade de bytes lidos pelo fread

  FILE * fin; // Pointer para o arquivo
  unsigned char * buffer = NULL; //Bytes do arquivo

  unsigned char key[16] = {
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 16
  };

  fin = fopen(argv[1], "r"); //Abre o arquivo como leitura

  //Verificar se o arquivo foi 'aberto'
  if (fin == NULL) {
    cout << "Ocorreu uma falha ao tentar abrir o arquivo " << argv[1] << endl;
    return -1;
  }

  /**
    Descobre o tamanho do arquivo para debug
  */
  fseek(fin, 0L, SEEK_END);
  fileSize = ftell(fin) - 1;
  rewind(fin);

  //Expansão de chaves
  unsigned char exp_key[EXP_KEY_SIZE];
  addKeyExpansion(key, exp_key);

  //Lê os bytes do arquivo e adiciona padding caso necessário
  buffer = new unsigned char[MAX_BUFFER_SIZE];
  bytesRead = fread(buffer, sizeof(unsigned char), MAX_BUFFER_SIZE, fin);
  while (bytesRead > 0) {
    if (bytesRead < MAX_BUFFER_SIZE)
      bytesRead -= 1; /* Se ler o último bloco do arquivo, desconsidera o EOF */

    buffSize = bytesRead;

    //Verifica se o tamanho do arquivo é múltiplo de 16. Caso não for, encontra o próximo múltiplo de 16 a partir
    //do tamanho do arquivo
    if (buffSize % 16 != 0)
      buffSize = buffSize + (16 - (buffSize % 16));

    if (bytesRead < buffSize)
      memset((buffer + bytesRead), 0, (buffSize - bytesRead));

    /* Execução do algoritmo AES */
    for(int i = 0; i < buffSize; i+= 16) {
      //Processa os bytes de 16 em 16
      aes(buffer + i, exp_key);
    }

    //DEBUG
    /*for(int i = 0; i < buffSize; i += 16)
      printState(buffer + i, 16);*/

    memset(buffer, 0, buffSize * sizeof(unsigned char));
    bytesRead = fread(buffer, sizeof(unsigned char), MAX_BUFFER_SIZE, fin);
  }
  //Libera a memória alocada
  delete [] buffer;
  fclose(fin);
  return 0;
}
