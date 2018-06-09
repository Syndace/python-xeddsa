CC        = /usr/bin/gcc
CFLAGS    = -Wall -Werror -g
LIBRARIES = -l:crypto_hash.a -l:crypto_hashblocks.a -l:crypto_verify.a -l:fastrandombytes.a -l:kernelrandombytes.a -l:crypto_rng.a -l:crypto_stream.a -l:crypto_core.a

crypto_sign.so:
	mkdir -p bin
	$(CC) $(CFLAGS) -I../include -I../crypto_hash -c -fpic -x c *.c
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/crypto_sign.so *.o -L../bin $(LIBRARIES)

clean:
	rm -f *.o
	rm -rf bin
