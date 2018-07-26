CC     := gcc
CFLAGS := -Wall -Werror

SOURCES := $(wildcard *.c)
OBJECTS := $(SOURCES:.c=.o)

MODULE := libcrypto_verify

ifeq ($(OS),Windows_NT)
	D := dll
	S := lib

	IMPORT_LIB = -Wl,--out-implib,"$@.$(S)"

	MKDIR := mkdir
	RMDIR := rd /s /q
	RM    := del
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		D := so
		S := a

		IMPORT_LIB =

		MKDIR := mkdir -p
		RMDIR := rm -rf
		RM    := rm -f
	endif
	ifeq ($(UNAME_S),Darwin)
		D := # TODO
		S := # TODO

		IMPORT_LIB = # TODO

		MKDIR := mkdir -p
		RMDIR := rm -rf
		RM    := rm -f
	endif
endif

LIBRARIES :=
INCLUDES  :=

DYNAMIC := bin/$(MODULE).$(D)
STATIC  := bin/$(MODULE).$(S)

.PHONY: all clean full_clean

all: $(DYNAMIC) $(STATIC)

$(DYNAMIC): bin $(OBJECTS)
	$(CC) $(CFLAGS) -shared -Wl,--no-undefined $(IMPORT_LIB) -o "$@" *.o -L../bin/static $(LIBRARIES)

$(STATIC): $(DYNAMIC) bin $(OBJECTS)
	ar rcs "$@" *.o

bin:
	$(MKDIR) "$@"

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -I../include -DBUILD -c -fPIC -x c -o "$@" "$<"

clean:
	-$(RM) *.o

full_clean: clean
	-$(RMDIR) bin
