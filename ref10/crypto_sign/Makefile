CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c=.o)

LIBRARIES = -l:crypto_hash.a -l:crypto_hashblocks.a -l:crypto_verify.a -l:fastrandombytes.a -l:kernelrandombytes.a -l:crypto_rng.a -l:crypto_stream.a -l:crypto_core.a

.PHONY: all clean full_clean

all: bin/libcrypto_sign.so module.preprocessed

bin/libcrypto_sign.so: bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libcrypto_sign.so *.o -L../bin $(LIBRARIES)

bin:
	mkdir -p bin

%.o: %.c
	$(CC) $(CFLAGS) -I../include -I../crypto_hash -c -fpic -x c -o "$@" "$<"

module.preprocessed: module.h
	$(CC) -I../include -E -o module.preprocessed module.h

clean:
	rm -rf bin
	rm -f *.o

full_clean: clean
	rm -f module.preprocessed
