CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

fastrandombytes.a:
	mkdir -p bin
	$(CC) $(CFLAGS) -I../kernelrandombytes -I../crypto_rng -c -fpic -x c fastrandombytes.c
	ar rcs bin/fastrandombytes.a fastrandombytes.o

clean:
	rm -f *.o
	rm -rf bin
