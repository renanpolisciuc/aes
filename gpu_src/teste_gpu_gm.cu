#include<stdio.h>
#include<iostream>
#include<string.h>
#include <chrono>
#include "aes_gpu.h"

using namespace std;
using namespace std::chrono;

#define MAX_BUFFER_SIZE  getProximoMultiplo16(536870912)
//#define MAX_BUFFER_SIZE  CACHE_SIZE
#define MAX_THR_PBLK 1024

#define HANDLE_ERROR(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true) {
  if (code != cudaSuccess) {
    fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
    if (abort) exit(code);
  }
}

__host__
void printState(unsigned char * state, int size) {
  for(int i = 0; i < size; i++)
    printf("%X ", state[i]);
  printf("\n");
}

__host__
int getProximoMultiplo16(long numero) {
  int n = numero;
  if (n % 16 != 0)
    n = n + (16 - (n % 16));
  return n;
}

int main(int argc, char ** argv) {
  long buffSize = 0L, //Tamanho do arquivo
       bytesRead = 0L; //Quantidade de bytes lidos pelo fread
  long long total_bytes = 0L;

  FILE * fin; // Pointer para o arquivo
  FILE * fout;
  unsigned char * buffer = NULL; //Bytes do arquivo
  unsigned char * buffGPU = NULL;
  unsigned char * keysGPU = NULL;

  unsigned char key[16] = {
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 16
  };

  cudaEvent_t start, stop;
  float time_run = 0.0, time_total = 0.0;

  fin = fopen(argv[1], "r"); //Abre o arquivo como leitura
  fout = fopen("gpu.out", "w"); //Abre o arquivo como escrita

  //Verificar se o arquivo foi 'aberto'
  if (fin == NULL) {
    cout << "Ocorreu uma falha ao tentar abrir o arquivo " << argv[1] << endl;
    return -1;
  }

  //Expansão de chaves
  unsigned char exp_key[EXP_KEY_SIZE];
  addKeyExpansion(key, exp_key);

  //Lê os bytes do arquivo e adiciona padding caso necessário
  buffer = new unsigned char[MAX_BUFFER_SIZE];
  bytesRead = fread(buffer, sizeof(unsigned char), MAX_BUFFER_SIZE, fin);
  HANDLE_ERROR(cudaMalloc((void**)&buffGPU, sizeof(unsigned char) * MAX_BUFFER_SIZE));
  HANDLE_ERROR(cudaMalloc((void**)&keysGPU, sizeof(unsigned char) * EXP_KEY_SIZE));
  HANDLE_ERROR(cudaMemcpy(keysGPU, exp_key, sizeof(unsigned char) * EXP_KEY_SIZE, cudaMemcpyHostToDevice));


  HANDLE_ERROR(cudaEventCreate(&start));
  HANDLE_ERROR(cudaEventCreate(&stop));
  HANDLE_ERROR(cudaEventRecord(start, 0));

  while (bytesRead > 0) {

    total_bytes += bytesRead;
    if (bytesRead < MAX_BUFFER_SIZE)
      bytesRead -= 1; /* Se ler o último bloco do arquivo, desconsidera o EOF */

    buffSize = bytesRead;

    //Verifica se o tamanho do arquivo é múltiplo de 16. Caso não for, encontra o próximo múltiplo de 16 a partir
    //do tamanho do arquivo
    buffSize = getProximoMultiplo16(buffSize);

    if (bytesRead < buffSize)
      memset((buffer + bytesRead), 0, (buffSize - bytesRead));

    HANDLE_ERROR(cudaMemcpy(buffGPU, buffer, sizeof(unsigned char) * MAX_BUFFER_SIZE, cudaMemcpyHostToDevice));

    int nBlocks = 1;
    int nTh = buffSize / 16;

    if (nTh > MAX_THR_PBLK) {
      nBlocks = (nTh / MAX_THR_PBLK) + 1;
      nTh = MAX_THR_PBLK;
    }
    aes<<<nBlocks, nTh>>>(buffGPU, keysGPU, (buffSize / 16));
    time_total += time_run;
    HANDLE_ERROR(cudaMemcpy(buffer, buffGPU, sizeof(unsigned char) * MAX_BUFFER_SIZE, cudaMemcpyDeviceToHost));

    // for(int i = 0; i < buffSize; i += 16)
    //   printState(buffer + i, 16);
    fwrite(buffer, sizeof(unsigned char), buffSize, fout);
    memset(buffer, 0, MAX_BUFFER_SIZE * sizeof(unsigned char));
    bytesRead = fread(buffer, sizeof(unsigned char), MAX_BUFFER_SIZE, fin);

  }

  HANDLE_ERROR(cudaEventRecord(stop, 0));
  HANDLE_ERROR(cudaEventSynchronize(stop));
  HANDLE_ERROR(cudaEventElapsedTime(&time_run, start, stop));
  HANDLE_ERROR(cudaEventDestroy(start));
  HANDLE_ERROR(cudaEventDestroy(stop));

  cout <<  ((double)total_bytes / 1000000000)   << " | " << (float) (time_run / 1000) << endl;

  //Libera a memória alocada
  cudaFree(buffGPU);
  cudaFree(keysGPU);
  delete [] buffer;
  fclose(fin);
  fclose(fout);
  return 0;
}
