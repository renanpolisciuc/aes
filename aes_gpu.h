//Número de rodadas do AES 128 bits
#define R_ROUNDS 10

//Número de chaves do AES. 176 = 16 * 11 (1 para cada rodada do AES + chave escolhida pelo usuário)
#define EXP_KEY_SIZE 176

/**
  Função shiftRows do AES
  @param estado atual
*/
__device__ void shiftRows(unsigned char * state);

/**
  Função subbytes do AES
  @param estado atual
*/
__device__ void subBytes(unsigned char * state);

/**
  Função mixColumns do AES
  @param estado atual
*/
__device__ void mixColumns(unsigned char * state);

/**
  Função addRoundKey do AES
  @param estado atual
  @param chave da rodada atual
*/
__device__ void addRoundKey(unsigned char * state, unsigned char * key);

/**
  Função AES
  - Realiza a criptografia de in_bytes utilizando os algoritmos do AES
  @param in_bytes (16 bytes)
  @param key chave escolhida pelo usuário (16 bytes)
*/
__global__ void aes(unsigned char * in_bytes, unsigned char * key, int nBlocks);
