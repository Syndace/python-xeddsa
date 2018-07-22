CC      = /usr/bin/gcc
CFLAGS  = -Wall -Werror -g
OBJECTS = $(patsubst %.c,%.o,$(wildcard *.c))

.PHONY: clean

bin/crypto_rng.a: bin $(OBJECTS)
	ar rcs bin/crypto_rng.a *.o

bin:
	mkdir -p bin

%.o: %.c
	$(CC) $(CFLAGS) -I../crypto_stream -c -fpic -x c -o "$@" "$<"

clean:
	rm -rf bin
	rm -f *.o
