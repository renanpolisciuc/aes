#include<stdio.h>
#include<string.h>
#include "aes_gpu.h"
#include "tables_gpu.h"

__device__
void subBytes(unsigned char * state) {
  //Faz a substituição byte a byte pela S_BOX
  for(int i = 0; i < 16; i++)
    state[i] = S_BOX[state[i]];
}

__device__
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
  cudaMemcpy(state, tmp, 16, cudaMemcpyDeviceToDevice);
}

__device__
void addRoundKey(unsigned char * state, unsigned char * key) {
  //Xor byte a byte entre o estado e a chave
  for(int i = 0; i < 16; i++)
    state[i] ^= key[i];
}
__device__
void mixColumns(unsigned char * state) {
  //Algoritmo mix column
  //Operação em GF(2^8)
}

__global__
void aes(unsigned char * in_bytes, unsigned char * key) {

}
