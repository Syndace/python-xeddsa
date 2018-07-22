CC      = /usr/bin/gcc
CFLAGS  = -Wall -Werror -g
OBJECTS = $(patsubst %.c,%.o,$(wildcard *.c))

.PHONY: clean

bin/crypto_core.a: bin $(OBJECTS)
	ar rcs bin/crypto_core.a *.o

bin:
	mkdir -p bin

%.o: %.c
	$(CC) $(CFLAGS) -c -fpic -x c -o "$@" "$<"

clean:
	rm -rf bin
	rm -f *.o
