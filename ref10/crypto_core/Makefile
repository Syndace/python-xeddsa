CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

crypto_core.a:
	mkdir -p bin
	$(CC) $(CFLAGS) -c -fpic -x c *.c
	ar rcs bin/crypto_core.a *.o

clean:
	rm -f *.o
	rm -rf bin
