CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c=.o)

LIBRARIES =    -lcrypto_rng    -lcrypto_stream    -lcrypto_core    -lkernelrandombytes
INCLUDES  = -I../crypto_rng -I../crypto_stream -I../crypto_core -I../kernelrandombytes

.PHONY: all clean full_clean

all: bin/libfastrandombytes.so bin/libfastrandombytes.a module.preprocessed

bin/libfastrandombytes.so: bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libfastrandombytes.so *.o -L../bin/static $(LIBRARIES)

bin/libfastrandombytes.a: bin/libfastrandombytes.so bin $(OBJECTS)
	ar rcs bin/libfastrandombytes.a *.o

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
