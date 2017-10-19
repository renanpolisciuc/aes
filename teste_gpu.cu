#include<stdio.h>
#include<iostream>
#include<string.h>
#include "aes.h"
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
  return 0;
}
