CC             = /usr/bin/gcc
CFLAGS         = -Wall -Werror -g
SODIUM_INCLUDE = /usr/local/include/sodium

ref10.so:
	$(CC) $(CFLAGS) -I$(SODIUM_INCLUDE) -c -fpic *.c
	mkdir -p bin
	$(CC) $(CFLAGS) -shared -lsodium -o bin/libref10.so *.o

clean:
	rm -f *.o
	rm -rf bin
