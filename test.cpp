#include<stdio.h>
#include<iostream>
#include<string.h>
#include "aes.h"
using namespace std;

//
void help();

//DEBUG
void printState(unsigned char * state, int size);

void printState(unsigned char * state, int size) {
  for(int i = 0; i < size; i++)
    printf("%c", state[i]);
}

int main(int argc, char ** argv) {
  long fsize = 0L, //Tamanho do arquivo
       bytes_read = 0L; //Quantidade de bytes lidos pelo fread

  FILE * fin; // Pointer para o arquivo
  unsigned char * fbytes = NULL; //Bytes do arquivo

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
    Conta a quantidade de bytes do arquivo
  */
  fseek(fin, 0L, SEEK_END);
  fsize = ftell(fin) - 1;
  rewind(fin);
  //Verifica se o tamanho do arquivo é múltiplo de 16. Caso não for, encontra o próximo múltiplo de 16 a partir
  //do tamanho do arquivo
  if (fsize % 16 != 0)
    fsize = fsize + (16 - (fsize % 16));

  //Lê os bytes do arquivo e adiciona padding caso necessário
  fbytes = new unsigned char[fsize];
  bytes_read = fread(fbytes, sizeof(unsigned char), fsize, fin) - 1;

  if (bytes_read < fsize)
    memset((fbytes + bytes_read), 0, (fsize - bytes_read));
  unsigned char exp_key[EXP_KEY_SIZE];
  addKeyExpansion(key, exp_key);

  for(int i = 0; i < fsize; i+= 16) {
    //Processa os bytes de 16 em 16
    aes(fbytes + i, exp_key);
  }
  //DEBUG
  for(int i = 0; i < fsize; i += 16)
    printState(fbytes + i, fsize);
  //Libera a memória alocada
  delete [] fbytes;
  fclose(fin);
  return 0;
}
