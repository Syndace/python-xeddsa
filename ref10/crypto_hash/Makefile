CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c=.o)

LIBRARIES =    -lcrypto_hashblocks
INCLUDES  = -I../crypto_hashblocks

.PHONY: all clean full_clean

all: bin/libcrypto_hash.so bin/libcrypto_hash.a module.preprocessed

bin/libcrypto_hash.so: bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libcrypto_hash.so *.o -L../bin/static $(LIBRARIES)

bin/libcrypto_hash.a: bin/libcrypto_hash.so bin $(OBJECTS)
	ar rcs bin/libcrypto_hash.a *.o

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
