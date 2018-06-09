CC     = /usr/bin/gcc
CFLAGS = -Wall -Werror -g

kernelrandombytes.a:
	mkdir -p bin
	($(CC) $(CFLAGS) -c -fpic -x c getentropy.c  && mv getentropy.o  kernelrandombytes.o) || \
	($(CC) $(CFLAGS) -c -fpic -x c getentropy2.c && mv getentropy2.o kernelrandombytes.o) || \
	($(CC) $(CFLAGS) -c -fpic -x c getrandom.c   && mv getrandom.o   kernelrandombytes.o) || \
	($(CC) $(CFLAGS) -c -fpic -x c getrandom2.c  && mv getrandom2.o  kernelrandombytes.o) || \
	($(CC) $(CFLAGS) -c -fpic -x c getrandom3.c  && mv getrandom3.o  kernelrandombytes.o) || \
	($(CC) $(CFLAGS) -c -fpic -x c urandom.c     && mv urandom.o     kernelrandombytes.o)
	ar rcs bin/kernelrandombytes.a kernelrandombytes.o

test: kernelrandombytes.a
	$(CC) $(CFLAGS) -x c test.c -o bin/test -Lbin -l:kernelrandombytes.a
	bin/test

clean:
	rm -f *.o
	rm -rf bin
