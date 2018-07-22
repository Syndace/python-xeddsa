CC      = /usr/bin/gcc
CFLAGS  = -Wall -Werror -g
OBJECTS = $(patsubst %.c,%.o,$(wildcard *.c))

.PHONY: clean

bin/fastrandombytes.a: bin $(OBJECTS)
	ar rcs bin/fastrandombytes.a *.o

bin:
	mkdir -p bin

%.o: %.c
	$(CC) $(CFLAGS) -I../kernelrandombytes -I../crypto_rng -c -fpic -x c -o "$@" "$<"

clean:
	rm -rf bin
	rm -f *.o
