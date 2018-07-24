CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c=.o)

LIBRARIES =
INCLUDES  =

.PHONY: all clean full_clean

all: bin/libcrypto_hashblocks.so bin/libcrypto_hashblocks.a module.preprocessed

bin/libcrypto_hashblocks.so: bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libcrypto_hashblocks.so *.o -L../bin/static $(LIBRARIES)

bin/libcrypto_hashblocks.a: bin/libcrypto_hashblocks.so bin $(OBJECTS)
	ar rcs bin/libcrypto_hashblocks.a *.o

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
