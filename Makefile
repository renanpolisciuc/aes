CXX = g++-4.7
CXX_FLAGS = -std=c++11 -O3 -Wall -fopenmp
HOST_COMPILER = $(CXX)
NVCC_FLAGS = -std=c++11 -O3 -ccbin $(HOST_COMPILER)

.PHONY: all make_cpu make_gpu clean

all: clean make_cpu make_gpu

make_cpu: tables key_expansion aes test
	$(CXX) *.o -o run
	@rm -f *.o

tables:
	$(CXX) $(CXX_FLAGS) -c cpu_src/tables.cpp
aes:
	$(CXX) $(CXX_FLAGS) -c cpu_src/aes.cpp
test:
	$(CXX) $(CXX_FLAGS) -c -Wall cpu_src/test.cpp
key_expansion:
	$(CXX) -c cpu_src/key_expansion.cpp


make_gpu: aes_gpu test_gpu
	nvcc $(NVCC_FLAGS) *.o -o gpu_src/run_gpu
	rm -f aes_gpu.o tables_gpu.o key_expansion.o tables.o teste_gpu.o
	mv gpu_src/run_gpu .
aes_gpu:
	nvcc $(NVCC_FLAGS) -c gpu_src/aes_gpu.cu
test_gpu:
	nvcc $(NVCC_FLAGS) -c gpu_src/teste_gpu.cu -L aes_gpu.o key_expansion.o tables_gpu.o


clean:
	@rm -f *.o run gpu_src/run_gpu
