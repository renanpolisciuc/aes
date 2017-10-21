all: clean make_cpu make_gpu

make_cpu: tables key_expansion aes test
	g++ *.o -o run
	rm aes.o test.o

tables:
	g++ -c tables.cpp
aes:
	g++ -c aes.cpp
test:
	g++ -c test.cpp -L aes.o


make_gpu: tables_gpu aes_gpu test_gpu
	nvcc -ccbin g++-4.7 *.o -o run_gpu
	rm aes_gpu.o tables_gpu.o key_expansion.o tables.o teste_gpu.o
tables_gpu:
	nvcc -ccbin g++-4.7 -c tables_gpu.cu
aes_gpu:
	nvcc -ccbin g++-4.7 -c aes_gpu.cu
test_gpu:
	nvcc -ccbin g++-4.7 -c teste_gpu.cu -L aes_gpu.o key_expansion.o tables_gpu.o

key_expansion:
	g++ -c key_expansion.cpp

clean:
	rm -f *.o run run_gpu
