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

void addRoundKey(unsigned char * state, unsigned char * key) {
  /*for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
      state[i * 4 + j] ^= key[j * 4 + i];*/
  for(int i = 0; i < 16; i++)
    state[i] ^= key[i];
}

void rotWord(unsigned char * word) {
  unsigned char tmp_word = word[0];
  word[0] = word[1];
  word[1] = word[2];
  word[2] = word[3];
  word[3] = tmp_word;
}
void subWord(unsigned char * word) {
  for(int i = 0; i < 4; i++)
    word[i] = S_BOX[word[i]];
}

void addKeyExpansionCore(unsigned char * in, unsigned char i) {
  rotWord(in);
  subWord(in);
  in[0] ^= rcon[i];
}
void translateWord(unsigned char * word) {
  unsigned char tmp[16];
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
      tmp[i * 4 + j] = word[4 * j + i];
  memcpy(word, tmp, 16);
}

void addKeyExpansion(unsigned char * key, unsigned char * exp_keys) {
  int bytesGenerated = 16;
  int rconIte = 1;
  unsigned char tmp[4];
  memcpy(exp_keys, key, 16);

  while(bytesGenerated < EXP_KEY_SIZE) {
    for(int i = 0; i < 4; i++)
      tmp[i] = exp_keys[i + bytesGenerated - 4];

    if (bytesGenerated % 16 == 0)
      addKeyExpansionCore(tmp, rconIte++);

    for(int i = 0; i < 4; i++) {
      exp_keys[bytesGenerated] = exp_keys[bytesGenerated - 16] ^ tmp[i];
      bytesGenerated++;
    }
  }
}

void mixColumns(unsigned char * state) {
  unsigned char tmp[16];
  tmp[0] = (unsigned char)(mul2[state[0]] ^ mul3[state[1]] ^ state[2] ^ state[3]);
  tmp[1] = (unsigned char)(state[0] ^ mul2[state[1]] ^ mul3[state[2]] ^ state[3]);
  tmp[2] = (unsigned char)(state[0] ^ state[1] ^ mul2[state[2]] ^ mul3[state[3]]);
  tmp[3] = (unsigned char)(mul3[state[0]] ^ state[1] ^ state[2] ^ mul2[state[3]]);

  tmp[4] = (unsigned char)(mul2[state[4]] ^ mul3[state[5]] ^ state[6] ^ state[7]);
  tmp[5] = (unsigned char)(state[4] ^ mul2[state[5]] ^ mul3[state[6]] ^ state[7]);
  tmp[6] = (unsigned char)(state[4] ^ state[5] ^ mul2[state[6]] ^ mul3[state[7]]);
  tmp[7] = (unsigned char)(mul3[state[4]] ^ state[5] ^ state[6] ^ mul2[state[7]]);

  tmp[8] = (unsigned char)(mul2[state[8]] ^ mul3[state[9]] ^ state[10] ^ state[11]);
  tmp[9] = (unsigned char)(state[8] ^ mul2[state[9]] ^ mul3[state[10]] ^ state[11]);
  tmp[10] = (unsigned char)(state[8] ^ state[9] ^ mul2[state[10]] ^ mul3[state[11]]);
  tmp[11] = (unsigned char)(mul3[state[8]] ^ state[9] ^ state[10] ^ mul2[state[11]]);

  tmp[12] = (unsigned char)(mul2[state[12]] ^ mul3[state[13]] ^ state[14] ^ state[15]);
  tmp[13] = (unsigned char)(state[12] ^ mul2[state[13]] ^ mul3[state[14]] ^ state[15]);
  tmp[14] = (unsigned char)(state[12] ^ state[13] ^ mul2[state[14]] ^ mul3[state[15]]);
  tmp[15] = (unsigned char)(mul3[state[12]] ^ state[13] ^ state[14] ^ mul2[state[15]]);
  memcpy(state, tmp, 16);
}

void aes(unsigned char * in_bytes, unsigned char * key) {
  unsigned char state[16];
  memcpy(state, in_bytes, 16);
  addRoundKey(state, key);

  for(int i = 0; i < (R_ROUNDS -1); i++) {
    subBytes(state);
    shiftRows(state);
    mixColumns(state);
    addRoundKey(state, key + (16 * (i + 1)));
  }
  subBytes(state);
  shiftRows(state);
  addRoundKey(state, key + 160);
  memcpy(in_bytes, state, 16);
}

void printState(unsigned char * state, int size) {
  for(int i = 0; i < size; i++) {
    printf("%X ", state[i]);
  }
  cout << endl;
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
    printState(fbytes + i, 16);
  //Libera a memória alocada
  delete [] fbytes;
  fclose(fin);
  return 0;
}
