CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c=.o)

.PHONY: all clean full_clean

all: bin/libcrypto_scalarmult.so module.preprocessed

bin/libcrypto_scalarmult.so: bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libcrypto_scalarmult.so *.o

bin:
	mkdir -p bin

%.o: %.c
	$(CC) $(CFLAGS) -I../include -c -fpic -x c -o "$@" "$<"

module.preprocessed: module.h
	$(CC) -I../include -E -o module.preprocessed module.h

clean:
	rm -rf bin
	rm -f *.o

full_clean: clean
	rm -f module.preprocessed
