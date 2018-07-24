CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c=.o)

LIBRARIES =    -lcrypto_hash    -lcrypto_hashblocks    -lcrypto_verify    -lfastrandombytes    -lcrypto_rng    -lcrypto_stream    -lcrypto_core    -lkernelrandombytes
INCLUDES  = -I../crypto_hash -I../crypto_hashblocks -I../crypto_verify -I../fastrandombytes -I../crypto_rng -I../crypto_stream -I../crypto_core -I../kernelrandombytes

.PHONY: all clean full_clean

all: bin/libcrypto_sign.so bin/libcrypto_sign.a module.preprocessed

bin/libcrypto_sign.so: bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libcrypto_sign.so *.o -L../bin/static $(LIBRARIES)

bin/libcrypto_sign.a: bin/libcrypto_sign.so bin $(OBJECTS)
	ar rcs bin/libcrypto_sign.a *.o

bin:
	mkdir -p bin

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -I../include -c -fPIC -x c -o "$@" "$<"

module.preprocessed: module.h
	$(CC) -I../include -E -o module.preprocessed module.h

clean:
	rm -f *.o

full_clean: clean
	rm -rf bin
	rm -f module.preprocessed
