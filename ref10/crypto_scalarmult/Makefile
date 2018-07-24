CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c=.o)

LIBRARIES =
INCLUDES  =

.PHONY: all clean full_clean

all: bin/libcrypto_scalarmult.so bin/libcrypto_scalarmult.a module.preprocessed

bin/libcrypto_scalarmult.so: bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libcrypto_scalarmult.so *.o -L../bin/static $(LIBRARIES)

bin/libcrypto_scalarmult.a: bin/libcrypto_scalarmult.so bin $(OBJECTS)
	ar rcs bin/libcrypto_scalarmult.a *.o

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
