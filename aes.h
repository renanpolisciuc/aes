
#define R_ROUNDS 10
#define EXP_KEY_SIZE 176


void help();
void shiftRows(unsigned char * state);
void subBytes(unsigned char * state);
void addRoundKey(unsigned char * state, unsigned char * key);
void addKeyExpansion(unsigned char * key, unsigned char * exp_keys);
void addKeyExpansionCore(unsigned char * in, unsigned char i);
void mixColumns(unsigned char * state);
void aes(unsigned char * in_bytes, unsigned char * key);
void rotWord(unsigned char * word);
void subWord(unsigned char * word);
void translateWord(unsigned char * word);

//DEBUG
void printState(unsigned char * state, int size);
