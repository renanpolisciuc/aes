#include "const.h"
/**
  Função shiftRows do AES
  @param estado atual
*/
void shiftRows(unsigned char * state);

/**
  Função subbytes do AES
  @param estado atual
*/
void subBytes(unsigned char * state);

/**
  Função mixColumns do AES
  @param estado atual
*/
void mixColumns(unsigned char * state);

/**
  Função addRoundKey do AES
  @param estado atual
  @param chave da rodada atual
*/
void addRoundKey(unsigned char * state, unsigned char * key);

/**
  Função AES
  - Realiza a criptografia de in_bytes utilizando os algoritmos do AES
  @param in_bytes (16 bytes)
  @param key chave escolhida pelo usuário (16 bytes)
*/
void aes(unsigned char * in_bytes, unsigned char * key);
