CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

crypto_stream.a:
	mkdir -p bin
	$(CC) $(CFLAGS) -I../crypto_core -c -fpic -x c *.c
	ar rcs bin/crypto_stream.a *.o

clean:
	rm -f *.o
	rm -rf bin
