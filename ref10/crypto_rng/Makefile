CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

crypto_rng.a:
	mkdir -p bin
	$(CC) $(CFLAGS) -I../crypto_stream -c -fpic -x c *.c
	ar rcs bin/crypto_rng.a *.o

clean:
	rm -f *.o
	rm -rf bin
