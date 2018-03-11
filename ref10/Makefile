CC             = /usr/bin/gcc
CFLAGS         = -Wall -Werror -g
SODIUM_INCLUDE = /usr/local/include/sodium

ref10.so:
	$(CC) $(CFLAGS) -I$(SODIUM_INCLUDE) -c -fpic -x c *.c
	mkdir -p bin
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libref10.so *.o -lsodium 

clean:
	rm -f *.o
	rm -rf bin
