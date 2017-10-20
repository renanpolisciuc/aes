all: make_cpu
make_cpu: tables key_expansion aes test
	g++ *.o -o run
	rm *.o

key_expansion:
	g++ -c key_expansion.cpp

tables:
	g++ -c tables.cpp

aes:
	g++ -c aes.cpp
test:
	g++ -c test.cpp -L aes.o

make_gpu: aes test_gpu
aes_gpu:
	nvcc -ccbin g++-4.7 -c aes_gpu.cu
test_gpu:
	nvcc -ccbin g++-4.7 teste_gpu.cu -o run_gpu -L aes_gpu.o

clean:
	rm *.o
