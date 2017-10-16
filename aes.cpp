#include<stdio.h>
#include<iostream>
#include<string.h>
#include "aes.h"

using namespace std;

void help() {
  cout << "./aes_gpu -i <entrada> -c <chave> -o <saida>" << endl;
}

int main(int argc, char ** argv) {
  long fsize = 0L, //Tamanho do arquivo
       bytes_read = 0L; //Quantidade de bytes lidos pelo fread

  FILE * fin; // Pointer para o arquivo
  unsigned char * fbytes = NULL; //Bytes do arquivo

  fin = fopen(argv[1], "r"); //Abre o arquivo como leitura

  //Verificar se o arquivo foi 'aberto'
  if (fin == NULL) {
    cout << "Ocorreu uma falha ao tentar abrir o arquivo " << argv[1] << endl;
    return -1;
  }

  /**
    Conta a quantidade de bytes do arquivo
  */
  fseek(fin, 0L, SEEK_END);
  fsize = ftell(fin);
  rewind(fin);

  //Verifica se o tamanho do arquivo é múltiplo de 16. Caso não for, encontra o próximo múltiplo de 16 a partir
  //do tamanho do arquivo
  if (fsize % 16 != 0)
    fsize = fsize + (16 - (fsize % 16));

  //Lê os bytes do arquivo e adiciona padding caso necessário
  fbytes = new unsigned char[fsize];
  bytes_read = fread(fbytes, sizeof(unsigned char), fsize, fin);
  if (bytes_read < fsize)
    memset((fbytes + bytes_read), 0, (fsize - bytes_read));


  delete [] fbytes;
  fclose(fin);
  return 0;
}
