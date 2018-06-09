CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

crypto_scalarmult.so:
	mkdir -p bin
	$(CC) $(CFLAGS) -I../include -c -fpic -x c *.c
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/crypto_scalarmult.so *.o

clean:
	rm -f *.o
	rm -rf bin
