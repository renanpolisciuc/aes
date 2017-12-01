//Número de rodadas do AES 128 bits
#define R_ROUNDS 10

//Número de chaves do AES. 176 = 16 * 11 (1 para cada rodada do AES + chave escolhida pelo usuário)
#define EXP_KEY_SIZE 176

#define MAX_CACHE 16384

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


//DEBUG
__host__ void printState(unsigned char * state, int size);
__host__ int getProximoMultiplo16(long numero);

/**
  Função addKeyExpansion do AES
  @param chave
  @param lista de chaves (1 chave para cada rodada + chave)
*/
__host__ void addKeyExpansion(unsigned char * key, unsigned char * exp_keys);

/**
  Função addKeyExpansionCore
  -Essa função faz a geração da chave i
  @param chave
  @param Iteração
*/
__host__ void addKeyExpansionCore(unsigned char * key, unsigned char i);

/**
  Função rotWord
  -Rotaciona uma word (4 bytes)
  @param palavra
*/
__host__ void rotWord(unsigned char * word);

/**
  Função subWord
  -Substitui cada byte da word por um byte na S_BOX
  @param palavra
*/
__host__ void subWord(unsigned char * word);

/**
  Função translateWord
  -Função auxiliar que tranlada uma matriz de tamanho 4 x 4
  @param palavra
*/
__host__ void translateWord(unsigned char * word);

/**
  Função AES - Implementada com Shared memory
  - Realiza a criptografia de in_bytes utilizando os algoritmos do AES
  @param in_bytes (16 bytes)
  @param key chave escolhida pelo usuário (16 bytes)
*/
__global__ void aes(unsigned char * in_bytes, unsigned char * key, int nBlocks);
