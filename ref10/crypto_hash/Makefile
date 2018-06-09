CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

crypto_hash.a:
	mkdir -p bin
	$(CC) $(CFLAGS) -I../crypto_hashblocks -c -fpic -x c *.c
	ar rcs bin/crypto_hash.a *.o

clean:
	rm -f *.o
	rm -rf bin
