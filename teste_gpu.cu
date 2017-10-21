#include<stdio.h>
#include<iostream>
#include<string.h>
#include "aes_gpu.h"
#include "key_expansion.h"
using namespace std;

#define MAX_BUFFER_SIZE  536870912

//DEBUG
void printState(unsigned char * state, int size);

void printState(unsigned char * state, int size) {
  for(int i = 0; i < size; i++)
    printf("%X ", state[i]);
  cout << endl;
}

int main(int argc, char ** argv) {
  long buffSize = 0L, //Tamanho do arquivo
       bytesRead = 0L,
       fileSize = 0L; //Quantidade de bytes lidos pelo fread

  FILE * fin; // Pointer para o arquivo
  unsigned char * buffer = NULL; //Bytes do arquivo
  unsigned char * buffGPU = NULL;

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
    Descobre o tamanho do arquivo para debug
  */
  fseek(fin, 0L, SEEK_END);
  fileSize = ftell(fin) - 1;
  rewind(fin);

  //Expansão de chaves
  unsigned char exp_key[EXP_KEY_SIZE];
  addKeyExpansion(key, exp_key);

  //Lê os bytes do arquivo e adiciona padding caso necessário
  buffer = new unsigned char[MAX_BUFFER_SIZE];
  bytesRead = fread(buffer, sizeof(unsigned char), MAX_BUFFER_SIZE, fin) - 1;
  buffSize = bytesRead;
  if (bytesRead % 16 != 0)
    buffSize = bytesRead + (16 - (bytesRead % 16));

  if (bytesRead < buffSize)
    memset((buffer + bytesRead), 'c', (buffSize - bytesRead));

  cudaMalloc((void**)&buffGPU, sizeof(unsigned char) * buffSize);
  cudaMemcpy(buffGPU, buffer, sizeof(unsigned char) * buffSize, cudaMemcpyHostToDevice);
  /* Algoritmo aqui */
  int nBlocks = 1;
  int nTh = buffSize / 16;

  aes<<<nBlocks, nTh>>>(buffGPU, exp_key, nTh);

  cudaMemcpy(buffer, buffGPU, sizeof(unsigned char) * buffSize, cudaMemcpyDeviceToHost);
  cout << buffer << endl;
  //Libera a memória alocada
  cudaFree(buffGPU);
  delete [] buffer;
  fclose(fin);
  return 0;
}
