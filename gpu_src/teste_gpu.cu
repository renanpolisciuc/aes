#include<stdio.h>
#include<iostream>
#include<string.h>
#include "aes_gpu.h"

using namespace std;

#define MAX_BUFFER_SIZE  536870912
__host__
void printState(unsigned char * state, int size) {
  for(int i = 0; i < size; i++)
    printf("%X ", state[i]);
  printf("\n");
}

int main(int argc, char ** argv) {
  long buffSize = 0L, //Tamanho do arquivo
       bytesRead = 0L,
       fileSize = 0L; //Quantidade de bytes lidos pelo fread

  FILE * fin; // Pointer para o arquivo
  unsigned char * buffer = NULL; //Bytes do arquivo
  unsigned char * buffGPU = NULL, *buffGPUOut = NULL;
  unsigned char * keysGPU = NULL;

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
    memset((buffer + bytesRead), 0, (buffSize - bytesRead));

  cudaMalloc((void**)&buffGPU, sizeof(unsigned char) * buffSize);
  cudaMalloc((void**)&buffGPUOut, sizeof(unsigned char) * buffSize);
  cudaMalloc((void**)&keysGPU, sizeof(unsigned char) * EXP_KEY_SIZE);
  cudaMemcpy(buffGPU, buffer, sizeof(unsigned char) * buffSize, cudaMemcpyHostToDevice);
  cudaMemcpy(keysGPU, exp_key, sizeof(unsigned char) * EXP_KEY_SIZE, cudaMemcpyHostToDevice);
  /* Algoritmo aqui */
  int nBlocks = 1;
  int nTh = buffSize / 16;

  aes<<<nBlocks, nTh>>>(buffGPU, buffGPUOut, keysGPU, nTh);

  cudaMemcpy(buffer, buffGPUOut, sizeof(unsigned char) * buffSize, cudaMemcpyDeviceToHost);

  //DEBUG
  for(int i = 0; i < buffSize; i += 16)
    printState(buffer + i, 16);

  //Libera a memória alocada
  cudaFree(buffGPU);
  cudaFree(buffGPUOut);
  cudaFree(keysGPU);
  delete [] buffer;
  fclose(fin);
  return 0;
}
