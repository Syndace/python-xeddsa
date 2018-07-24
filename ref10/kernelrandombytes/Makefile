CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

SOURCES = $(wildcard *.c)
OBJECTS = $(filter-out urandom.o test.o, $(SOURCES:.c=.o))

LIBRARIES =
INCLUDES  =

.PHONY: all clean full_clean

all: bin/libkernelrandombytes.so bin/libkernelrandombytes.a module.preprocessed bin/test

bin/libkernelrandombytes.so: bin kernelrandombytes.o
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined -o bin/libkernelrandombytes.so kernelrandombytes.o -L../bin/static $(LIBRARIES)

bin/libkernelrandombytes.a: bin/libkernelrandombytes.so bin kernelrandombytes.o
	ar rcs bin/libkernelrandombytes.a kernelrandombytes.o

bin/test: bin/libkernelrandombytes.a
	$(CC) $(CFLAGS) -x c test.c -o bin/test -Lbin -l:libkernelrandombytes.a

test: bin/test
	bin/test

bin:
	mkdir -p bin

kernelrandombytes.o: | $(OBJECTS) urandom.o

%.o: %.c
	-$(CC) $(CFLAGS) $(INCLUDES) -I../include -c -fPIC -x c -o "$@" "$<" && cp -n "$@" kernelrandombytes.o

module.preprocessed: module.h
	$(CC) -I../include -E -o module.preprocessed module.h

clean:
	rm -f *.o

full_clean: clean
	rm -rf bin
	rm -f module.preprocessed
