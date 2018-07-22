CC      = /usr/bin/gcc
CFLAGS  = -Wall -Werror -g
OBJECTS = $(patsubst %.c,%.o,$(wildcard *.c))

.PHONY: clean

bin/crypto_verify.a: bin $(OBJECTS)
	ar rcs bin/crypto_verify.a *.o

bin:
	mkdir -p bin

%.o: %.c
	$(CC) $(CFLAGS) -c -fpic -x c "$<"

clean:
	rm -rf bin
	rm -f *.o
