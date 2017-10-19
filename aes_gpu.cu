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
}

__device__
void addRoundKey(unsigned char * state, unsigned char * key) {
  //Xor byte a byte entre o estado e a chave
  for(int i = 0; i < 16; i++)
    state[i] ^= key[i];
}

__device__
void rotWord(unsigned char * word) {
  unsigned char tmp_word = word[0];
  //Rotaciona uma word
  word[0] = word[1];
  word[1] = word[2];
  word[2] = word[3];
  word[3] = tmp_word;
}

__device__
void subWord(unsigned char * word) {
  //Substitui cada byte da word por um byte da S_BOX
  for(int i = 0; i < 4; i++)
    word[i] = S_BOX[word[i]];
}

__device__
void addKeyExpansionCore(unsigned char * key, unsigned char i) {
  //Rotaciona, substitui e faz um xor com a tabela rcon (apenas os bits mais à esquerda)
  rotWord(key);
  subWord(key);
  key[0] ^= rcon[i];
}

__device__
void translateWord(unsigned char * word) {

}

__device__
void addKeyExpansion(unsigned char * key, unsigned char * exp_keys) {

}

__device__
void mixColumns(unsigned char * state) {
  //Algoritmo mix column
  //Operação em GF(2^8)
}

__global__
void aes(unsigned char * in_bytes, unsigned char * key) {

}
