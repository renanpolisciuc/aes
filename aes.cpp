#include<stdio.h>
#include<iostream>
#include<string.h>
#include "aes.h"

using namespace std;
void subBytes(unsigned char * state) {
  for(int i = 0; i < 16; i++)
    state[i] = S_BOX[state[i]];
}

void shiftRows(unsigned char * state) {
  unsigned char tmp[16];
  tmp[0] = state[0];
  tmp[4] = state[4];
  tmp[8] = state[8];
  tmp[12] = state[12];

  tmp[1] = state[5];
  tmp[5] = state[9];
  tmp[9] = state[13];
  tmp[13] = state[1];

  tmp[2] = state[10];
  tmp[6] = state[14];
  tmp[10] = state[2];
  tmp[14] = state[6];

  tmp[3] = state[15];
  tmp[7] = state[3];
  tmp[11] = state[7];
  tmp[15] = state[11];
  memcpy(state, tmp, 16);
}

void aes(unsigned char * in_bytes, unsigned char * chave) {
  unsigned char state[16];
  memcpy(state, in_bytes, 16);
  subBytes(state);
  shiftRows(state);
  for(int i = 0; i < 16; i++) {
    printf("[%X]", state[i]);
  }
  cout << endl;

  for(int i = 0; i < (R_ROUNDS -1); i++) {
  }
}

int main(int argc, char ** argv) {
  long fsize = 0L, //Tamanho do arquivo
       bytes_read = 0L; //Quantidade de bytes lidos pelo fread

  FILE * fin; // Pointer para o arquivo
  unsigned char * fbytes = NULL; //Bytes do arquivo
  unsigned char chave[16] = {
    0x0, 0x1, 0x2, 0x3,
    0x4, 0x5, 0x6, 0x7,
    0x8, 0x9, 0xA, 0xB,
    0xC, 0xD, 0xE, 0xF
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
  fsize = ftell(fin);
  rewind(fin);

  //Verifica se o tamanho do arquivo é múltiplo de 16. Caso não for, encontra o próximo múltiplo de 16 a partir
  //do tamanho do arquivo
  if (fsize % 16 != 0)
    fsize = fsize + (16 - (fsize % 16));

  //Lê os bytes do arquivo e adiciona padding caso necessário
  fbytes = new unsigned char[fsize];
  bytes_read = fread(fbytes, sizeof(unsigned char), fsize, fin);
  if (bytes_read < fsize)
    memset((fbytes + bytes_read), 0, (fsize - bytes_read));

  for(int i = 0; i < fsize; i+= 16) {
    //Processa os bytes de 16 em 16
    aes(fbytes + i, chave);
  }

  //Libera a memória alocada
  delete [] fbytes;
  fclose(fin);
  return 0;
}
