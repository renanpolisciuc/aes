#include<stdio.h>
#include<iostream>
#include<string.h>
#include <chrono>
#include <omp.h>
#include "aes.h"
#include "key_expansion.h"

using namespace std;
using namespace std::chrono;

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
       bytesRead = 0L; //Quantidade de bytes lidos pelo fread
  long long total_bytes = 0L;

  FILE * fin; // Pointer para o arquivo
  FILE * fout;
  unsigned char * buffer = NULL; //Bytes do arquivo
  double duracao = 0L, duracao_IO = 0L, duracao_proc = 0L;

  unsigned char key[16] = {
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 16
  };

  fin = fopen(argv[1], "r"); //Abre o arquivo como leitura
  fout = fopen("cpu.out", "w"); //Abre o arquivo como escrita

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
  /* Fork a team of threads giving them their own copies of variables */

  auto t1 = high_resolution_clock::now();
  while (bytesRead > 0) {

    total_bytes += bytesRead;

    if (bytesRead < MAX_BUFFER_SIZE)
      bytesRead -= 1; /* Se ler o último bloco do arquivo, desconsidera o EOF */

    buffSize = bytesRead;

    //Verifica se o tamanho do arquivo é múltiplo de 16. Caso não for, encontra o próximo múltiplo de 16 a partir
    //do tamanho do arquivo
    if (buffSize % 16 != 0)
      buffSize = buffSize + (16 - (buffSize % 16));

    if (bytesRead < buffSize)
      memset((buffer + bytesRead), 0, (buffSize - bytesRead));

    auto t1_p = high_resolution_clock::now();
    /* Execução do algoritmo AES */
    #pragma omp parallel for schedule(static)
    for(int i = 0; i < buffSize; i+= 16) {
      //Processa os bytes de 16 em 16
      aes(buffer + i, exp_key);
    }
    auto t2_p = high_resolution_clock::now();
    auto duration_P = duration_cast<milliseconds>( t2_p - t1_p );
    duracao_proc += duration_P.count();
    //DEBUG
    // for(int i = 0; i < buffSize; i += 16)
    //   printState(buffer + i, 16);

    auto t1_io = high_resolution_clock::now();
    fwrite(buffer, sizeof(unsigned char), buffSize, fout);
    bytesRead = fread(buffer, sizeof(unsigned char), MAX_BUFFER_SIZE, fin);
    memset(buffer, 0, MAX_BUFFER_SIZE * sizeof(unsigned char));
    auto t2_io = high_resolution_clock::now();
    auto duration_IO = duration_cast<milliseconds>( t2_io - t1_io );

    duracao_IO += duration_IO.count();
  }

  auto t2 = high_resolution_clock::now();
  auto duration = duration_cast<milliseconds>( t2 - t1 );
  duracao += duration.count();

  cout <<  ((double)total_bytes / 1000000000)   << " | " << (float) (duracao / 1000) << " | " <<  (float) (duracao_proc / 1000)<< " | " << (float) (duracao_IO / 1000) << endl;
  //Libera a memória alocada
  delete [] buffer;
  fclose(fin);
  fclose(fout);
  return 0;
}
