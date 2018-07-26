ifeq ($(OS),Windows_NT)
	D := dll
	S := lib

    SEP := \\

	MKDIR := mkdir
	RMDIR := rd /s /q
	CP    := copy
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		D := so
		S := a

        SEP := /

		MKDIR := mkdir -p
		RMDIR := rm -rf
		CP    := cp
	endif
	ifeq ($(UNAME_S),Darwin)
		D := # TODO
		S := # TODO

        SEP := /

		MKDIR := mkdir -p
		RMDIR := rm -rf
		CP    := cp
	endif
endif



.PHONY: all clean full_clean

all: libcrypto_scalarmult libcrypto_sign



bin:
	$(MKDIR) bin

bin/static: bin
	$(MKDIR) bin$(SEP)static

bin/dynamic: bin
	$(MKDIR) bin$(SEP)dynamic



.PHONY: libcrypto_scalarmult build_crypto_scalarmult

libcrypto_scalarmult: bin/static/libcrypto_scalarmult.$(S) bin/dynamic/libcrypto_scalarmult.$(D)

build_crypto_scalarmult:
	$(MAKE) -C crypto_scalarmult

bin/static/libcrypto_scalarmult.$(S): bin/static build_crypto_scalarmult
	$(CP) crypto_scalarmult$(SEP)bin$(SEP)libcrypto_scalarmult.$(S) bin$(SEP)static

bin/dynamic/libcrypto_scalarmult.$(D): bin/dynamic build_crypto_scalarmult
	$(CP) crypto_scalarmult$(SEP)bin$(SEP)libcrypto_scalarmult.$(D)* bin$(SEP)dynamic



.PHONY: libcrypto_sign build_crypto_sign

libcrypto_sign: bin/static/libcrypto_sign.$(S) bin/dynamic/libcrypto_sign.$(D)

build_crypto_sign: libcrypto_hash libcrypto_verify libfastrandombytes
	$(MAKE) -C crypto_sign

bin/static/libcrypto_sign.$(S): bin/static build_crypto_sign
	$(CP) crypto_sign$(SEP)bin$(SEP)libcrypto_sign.$(S) bin$(SEP)static

bin/dynamic/libcrypto_sign.$(D): bin/dynamic build_crypto_sign
	$(CP) crypto_sign$(SEP)bin$(SEP)libcrypto_sign.$(D)* bin$(SEP)dynamic



.PHONY: libcrypto_core build_crypto_core

libcrypto_core: bin/static/libcrypto_core.$(S) bin/dynamic/libcrypto_core.$(D)

build_crypto_core:
	$(MAKE) -C crypto_core

bin/static/libcrypto_core.$(S): bin/static build_crypto_core
	$(CP) crypto_core$(SEP)bin$(SEP)libcrypto_core.$(S) bin$(SEP)static

bin/dynamic/libcrypto_core.$(D): bin/dynamic build_crypto_core
	$(CP) crypto_core$(SEP)bin$(SEP)libcrypto_core.$(D)* bin$(SEP)dynamic



.PHONY: libcrypto_hash build_crypto_hash

libcrypto_hash: bin/static/libcrypto_hash.$(S) bin/dynamic/libcrypto_hash.$(D)

build_crypto_hash: libcrypto_hashblocks
	$(MAKE) -C crypto_hash

bin/static/libcrypto_hash.$(S): bin/static build_crypto_hash
	$(CP) crypto_hash$(SEP)bin$(SEP)libcrypto_hash.$(S) bin$(SEP)static

bin/dynamic/libcrypto_hash.$(D): bin/dynamic build_crypto_hash
	$(CP) crypto_hash$(SEP)bin$(SEP)libcrypto_hash.$(D)* bin$(SEP)dynamic



.PHONY: libcrypto_hashblocks build_crypto_hashblocks

libcrypto_hashblocks: bin/static/libcrypto_hashblocks.$(S) bin/dynamic/libcrypto_hashblocks.$(D)

build_crypto_hashblocks:
	$(MAKE) -C crypto_hashblocks

bin/static/libcrypto_hashblocks.$(S): bin/static build_crypto_hashblocks
	$(CP) crypto_hashblocks$(SEP)bin$(SEP)libcrypto_hashblocks.$(S) bin$(SEP)static

bin/dynamic/libcrypto_hashblocks.$(D): bin/dynamic build_crypto_hashblocks
	$(CP) crypto_hashblocks$(SEP)bin$(SEP)libcrypto_hashblocks.$(D)* bin$(SEP)dynamic



.PHONY: libcrypto_rng build_crypto_rng

libcrypto_rng: bin/static/libcrypto_rng.$(S) bin/dynamic/libcrypto_rng.$(D)

build_crypto_rng: libcrypto_stream
	$(MAKE) -C crypto_rng

bin/static/libcrypto_rng.$(S): bin/static build_crypto_rng
	$(CP) crypto_rng$(SEP)bin$(SEP)libcrypto_rng.$(S) bin$(SEP)static

bin/dynamic/libcrypto_rng.$(D): bin/dynamic build_crypto_rng
	$(CP) crypto_rng$(SEP)bin$(SEP)libcrypto_rng.$(D)* bin$(SEP)dynamic



.PHONY: libcrypto_stream build_crypto_stream

libcrypto_stream: bin/static/libcrypto_stream.$(S) bin/dynamic/libcrypto_stream.$(D)

build_crypto_stream: libcrypto_core
	$(MAKE) -C crypto_stream

bin/static/libcrypto_stream.$(S): bin/static build_crypto_stream
	$(CP) crypto_stream$(SEP)bin$(SEP)libcrypto_stream.$(S) bin$(SEP)static

bin/dynamic/libcrypto_stream.$(D): bin/dynamic build_crypto_stream
	$(CP) crypto_stream$(SEP)bin$(SEP)libcrypto_stream.$(D)* bin$(SEP)dynamic



.PHONY: libcrypto_verify build_crypto_verify

libcrypto_verify: bin/static/libcrypto_verify.$(S) bin/dynamic/libcrypto_verify.$(D)

build_crypto_verify:
	$(MAKE) -C crypto_verify

bin/static/libcrypto_verify.$(S): bin/static build_crypto_verify
	$(CP) crypto_verify$(SEP)bin$(SEP)libcrypto_verify.$(S) bin$(SEP)static

bin/dynamic/libcrypto_verify.$(D): bin/dynamic build_crypto_verify
	$(CP) crypto_verify$(SEP)bin$(SEP)libcrypto_verify.$(D)* bin$(SEP)dynamic



.PHONY: libfastrandombytes build_fastrandombytes

libfastrandombytes: bin/static/libfastrandombytes.$(S) bin/dynamic/libfastrandombytes.$(D)

build_fastrandombytes: libcrypto_rng libkernelrandombytes
	$(MAKE) -C fastrandombytes

bin/static/libfastrandombytes.$(S): bin/static build_fastrandombytes
	$(CP) fastrandombytes$(SEP)bin$(SEP)libfastrandombytes.$(S) bin$(SEP)static

bin/dynamic/libfastrandombytes.$(D): bin/dynamic build_fastrandombytes
	$(CP) fastrandombytes$(SEP)bin$(SEP)libfastrandombytes.$(D)* bin$(SEP)dynamic



.PHONY: libkernelrandombytes build_kernelrandombytes

libkernelrandombytes: bin/static/libkernelrandombytes.$(S) bin/dynamic/libkernelrandombytes.$(D)

build_kernelrandombytes:
	$(MAKE) -C kernelrandombytes
	$(MAKE) -C kernelrandombytes test

bin/static/libkernelrandombytes.$(S): bin/static build_kernelrandombytes
	$(CP) kernelrandombytes$(SEP)bin$(SEP)libkernelrandombytes.$(S) bin$(SEP)static

bin/dynamic/libkernelrandombytes.$(D): bin/dynamic build_kernelrandombytes
	$(CP) kernelrandombytes$(SEP)bin$(SEP)libkernelrandombytes.$(D)* bin$(SEP)dynamic



clean:
	$(MAKE) -C crypto_core clean
	$(MAKE) -C crypto_hash clean
	$(MAKE) -C crypto_hashblocks clean
	$(MAKE) -C crypto_rng clean
	$(MAKE) -C crypto_scalarmult clean
	$(MAKE) -C crypto_sign clean
	$(MAKE) -C crypto_stream clean
	$(MAKE) -C crypto_verify clean
	$(MAKE) -C fastrandombytes clean
	$(MAKE) -C kernelrandombytes clean

full_clean: clean
	$(MAKE) -C crypto_core full_clean
	$(MAKE) -C crypto_hash full_clean
	$(MAKE) -C crypto_hashblocks full_clean
	$(MAKE) -C crypto_rng full_clean
	$(MAKE) -C crypto_scalarmult full_clean
	$(MAKE) -C crypto_sign full_clean
	$(MAKE) -C crypto_stream full_clean
	$(MAKE) -C crypto_verify full_clean
	$(MAKE) -C fastrandombytes full_clean
	$(MAKE) -C kernelrandombytes full_clean
	-$(RMDIR) bin
