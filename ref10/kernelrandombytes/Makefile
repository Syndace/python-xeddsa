CC     := gcc
CFLAGS := -Wall -Werror

SOURCES := $(wildcard *.c)
OBJECTS := $(filter-out urandom.o test.o, $(SOURCES:.c=.o))

MODULE := libkernelrandombytes

ifeq ($(OS),Windows_NT)
	D := dll
	S := lib

	IMPORT_LIB = -Wl,--out-implib,"$@.$(S)"

	MKDIR := mkdir
	RMDIR := rd /s /q
	RM    := del

	COPY_OBJECT = if not exist kernelrandombytes.o copy "$@" kernelrandombytes.o

	URANDOM :=
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		D := so
		S := a

		IMPORT_LIB =

		MKDIR := mkdir -p
		RMDIR := rm -rf
		RM    := rm -f

		COPY_OBJECT = cp -n "$@" kernelrandombytes.o

		URANDOM := urandom.o
	endif
	ifeq ($(UNAME_S),Darwin)
		D := # TODO
		S := # TODO

		IMPORT_LIB = # TODO

		MKDIR := mkdir -p
		RMDIR := rm -rf
		RM    := rm -f

		COPY_OBJECT = # TODO

		URANDOM :=
	endif
endif

LIBRARIES :=
INCLUDES  :=

DYNAMIC := bin/$(MODULE).$(D)
STATIC  := bin/$(MODULE).$(S)

.PHONY: all clean full_clean test

all: $(DYNAMIC) $(STATIC) bin/test

$(DYNAMIC): bin kernelrandombytes.o
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined $(IMPORT_LIB) -o "$@" kernelrandombytes.o -L../bin/static $(LIBRARIES)

$(STATIC): $(DYNAMIC) bin kernelrandombytes.o
	ar rcs "$@" kernelrandombytes.o

bin/test: $(STATIC)
	$(CC) $(CFLAGS) -x c test.c -o "$@" -Lbin -l:$(MODULE).$(S)

test: bin/test
	$<

bin:
	$(MKDIR) "$@"

kernelrandombytes.o: | $(OBJECTS) $(URANDOM)

%.o: %.c
	-$(CC) $(CFLAGS) $(INCLUDES) -I../include -DBUILD -c -fPIC -x c -o "$@" "$<"
	-$(COPY_OBJECT)

rtlgenrandom.o: rtlgenrandom.c
	-$(CC) $(CFLAGS) $(INCLUDES) -I../include -DBUILD -c -fPIC -x c -o "$@" "$<" -lADVAPI32
	-$(COPY_OBJECT)

clean:
	-$(RM) *.o

full_clean: clean
	-$(RMDIR) bin
