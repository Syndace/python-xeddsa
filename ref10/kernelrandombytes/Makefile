CC      = /usr/bin/gcc
CFLAGS  = -Wall -Werror -g
OBJECTS = $(patsubst %.c,%.o,$(wildcard get*.c))

.PHONY: all test clean

all: bin/kernelrandombytes.a bin/test

bin/kernelrandombytes.a: bin kernelrandombytes.o
	ar rcs bin/kernelrandombytes.a kernelrandombytes.o

bin/test: bin/kernelrandombytes.a
	$(CC) $(CFLAGS) -x c test.c -o bin/test -Lbin -l:kernelrandombytes.a

test: bin/test
	bin/test

kernelrandombytes.o: | $(OBJECTS) urandom.o

bin:
	mkdir -p bin

%.o: %.c
	-$(CC) $(CFLAGS) -c -fpic -x c -o "$@" "$<" && cp -n "$@" kernelrandombytes.o

clean:
	rm -rf bin
	rm -f *.o
