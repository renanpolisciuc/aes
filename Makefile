all: clean make_cpu make_gpu

make_cpu: tables key_expansion aes test
	g++ *.o -o run
	rm -f *.o

tables:
	g++ -c tables.cpp
aes:
	g++ -c aes.cpp
test:
	g++ -c test.cpp -L aes.o
key_expansion:
	g++ -c key_expansion.cpp


make_gpu: tables_gpu aes_gpu test_gpu
	nvcc -ccbin g++-4.7 *.o -o gpu_src/run_gpu
	rm -f aes_gpu.o tables_gpu.o key_expansion.o tables.o teste_gpu.o
tables_gpu:
	nvcc -ccbin g++-4.7 -c gpu_src/tables_gpu.cu
aes_gpu:
	nvcc -ccbin g++-4.7 -c gpu_src/aes_gpu.cu
test_gpu:
	nvcc -ccbin g++-4.7 -c gpu_src/teste_gpu.cu -L aes_gpu.o key_expansion.o tables_gpu.o


clean:
	rm -f *.o run gpu_src/run_gpu
