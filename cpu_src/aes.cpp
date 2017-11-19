#include<stdio.h>
#include<string.h>
#include "aes.h"
#include "tables.h"

void subBytes(unsigned char * state) {
  //Faz a substituição byte a byte pela S_BOX
  for(int i = 0; i < 16; i++)
    state[i] = S_BOX[state[i]];
}

void shiftRows(unsigned char * state) {
  unsigned char tmp[16];
  //0 shifts
  tmp[0] = state[0];
  tmp[4] = state[4];
  tmp[8] = state[8];
  tmp[12] = state[12];

  //1 shift para a esquerda
  tmp[1] = state[5];
  tmp[5] = state[9];
  tmp[9] = state[13];
  tmp[13] = state[1];

  //2 shifts para a esquerda
  tmp[2] = state[10];
  tmp[6] = state[14];
  tmp[10] = state[2];
  tmp[14] = state[6];

  //3 shifts para a esquerda
  tmp[3] = state[15];
  tmp[7] = state[3];
  tmp[11] = state[7];
  tmp[15] = state[11];
  memcpy(state, tmp, 16);
}

void addRoundKey(unsigned char * state, unsigned char * key) {
  //Xor byte a byte entre o estado e a chave
  for(int i = 0; i < 16; i++)
    state[i] ^= key[i];
}

void mixColumns(unsigned char * state) {
  //Algoritmo mix column
  //Operação em GF(2^8)
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
  //Copia os primeiros 16 bytes para a memoria
  memcpy(state, in_bytes, 16);

  //Adiciona a primeira chave
  addRoundKey(state, key);

  //N-1 rodadas
  for(int i = 0; i < (R_ROUNDS -1); i++) {
    subBytes(state);
    shiftRows(state);
    mixColumns(state);

    //Seleciona a próxima chave
    addRoundKey(state, key + (16 * (i + 1)));
  }
  //Última rodada
  subBytes(state);
  shiftRows(state);
  addRoundKey(state, key + 160);

  //Copia a resposta para a memória
  memcpy(in_bytes, state, 16);
}
