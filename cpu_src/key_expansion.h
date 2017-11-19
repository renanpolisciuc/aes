/**
  Função addKeyExpansion do AES
  @param chave
  @param lista de chaves (1 chave para cada rodada + chave)
*/
void addKeyExpansion(unsigned char * key, unsigned char * exp_keys);

/**
  Função addKeyExpansionCore
  -Essa função faz a geração da chave i
  @param chave
  @param Iteração
*/
void addKeyExpansionCore(unsigned char * key, unsigned char i);

/**
  Função rotWord
  -Rotaciona uma word (4 bytes)
  @param palavra
*/
void rotWord(unsigned char * word);

/**
  Função subWord
  -Substitui cada byte da word por um byte na S_BOX
  @param palavra
*/
void subWord(unsigned char * word);

/**
  Função translateWord
  -Função auxiliar que tranlada uma matriz de tamanho 4 x 4
  @param palavra
*/
void translateWord(unsigned char * word);
