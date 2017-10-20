#include <string.h>
#include "const.h"
#include "tables.h"
#include "key_expansion.h"

void rotWord(unsigned char * word) {
  unsigned char tmp_word = word[0];
  //Rotaciona uma word
  word[0] = word[1];
  word[1] = word[2];
  word[2] = word[3];
  word[3] = tmp_word;
}
void subWord(unsigned char * word) {
  //Substitui cada byte da word por um byte da S_BOX
  for(int i = 0; i < 4; i++)
    word[i] = S_BOX[word[i]];
}

void addKeyExpansionCore(unsigned char * key, unsigned char i) {
  //Rotaciona, substitui e faz um xor com a tabela rcon (apenas os bits mais à esquerda)
  rotWord(key);
  subWord(key);
  key[0] ^= rcon[i];
}
void translateWord(unsigned char * word) {
  //transforma linha em coluna
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

  //As primeiras 4 words são a propria chave
  memcpy(exp_keys, key, 16);

  //Gera todas as chaves para as rodadas
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
