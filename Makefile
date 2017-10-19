all: make_cpu make_gpu
make_cpu: aes test
	g++ *.o -o run
	rm *.o
make_gpu: aes test_gpu
aes:
	g++ -c aes.cpp
aes_gpu:
	nvcc -ccbin g++-4.7 -c aes_gpu.cu
test:
	g++ -c test.cpp -L aes.o
test_gpu:
	nvcc -ccbin g++-4.7 teste_gpu.cu -o run_gpu -L aes_gpu.o
clean:
	rm *.o
