all: aes test
	g++ *.o -o run
	rm *.o
aes:
	g++ -c aes.cpp
test:
	g++ -c test.cpp -L aes.o
