CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

crypto_hashblocks.a:
	mkdir -p bin
	$(CC) $(CFLAGS) -c -fpic -x c *.c
	ar rcs bin/crypto_hashblocks.a *.o

clean:
	rm -f *.o
	rm -rf bin
