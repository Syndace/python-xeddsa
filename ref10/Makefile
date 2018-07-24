.PHONY: all clean full_clean

all: libcrypto_scalarmult libcrypto_sign



bin:
	mkdir -p bin

bin/static: bin
	mkdir -p bin/static

bin/dynamic: bin
	mkdir -p bin/dynamic



.PHONY: libcrypto_scalarmult build_crypto_scalarmult

libcrypto_scalarmult: bin/static/libcrypto_scalarmult.a bin/dynamic/libcrypto_scalarmult.so

build_crypto_scalarmult:
	$(MAKE) -C crypto_scalarmult

bin/static/libcrypto_scalarmult.a: bin/static build_crypto_scalarmult
	cp crypto_scalarmult/bin/libcrypto_scalarmult.a bin/static/

bin/dynamic/libcrypto_scalarmult.so: bin/dynamic build_crypto_scalarmult
	cp crypto_scalarmult/bin/libcrypto_scalarmult.so bin/dynamic/



.PHONY: libcrypto_sign build_crypto_sign

libcrypto_sign: bin/static/libcrypto_sign.a bin/dynamic/libcrypto_sign.so

build_crypto_sign: libcrypto_hash libcrypto_verify libfastrandombytes
	$(MAKE) -C crypto_sign

bin/static/libcrypto_sign.a: bin/static build_crypto_sign
	cp crypto_sign/bin/libcrypto_sign.a bin/static/

bin/dynamic/libcrypto_sign.so: bin/dynamic build_crypto_sign
	cp crypto_sign/bin/libcrypto_sign.so bin/dynamic/



.PHONY: libcrypto_core build_crypto_core

libcrypto_core: bin/static/libcrypto_core.a bin/dynamic/libcrypto_core.so

build_crypto_core:
	$(MAKE) -C crypto_core

bin/static/libcrypto_core.a: bin/static build_crypto_core
	cp crypto_core/bin/libcrypto_core.a bin/static/

bin/dynamic/libcrypto_core.so: bin/dynamic build_crypto_core
	cp crypto_core/bin/libcrypto_core.so bin/dynamic/



.PHONY: libcrypto_hash build_crypto_hash

libcrypto_hash: bin/static/libcrypto_hash.a bin/dynamic/libcrypto_hash.so

build_crypto_hash: libcrypto_hashblocks
	$(MAKE) -C crypto_hash

bin/static/libcrypto_hash.a: bin/static build_crypto_hash
	cp crypto_hash/bin/libcrypto_hash.a bin/static/

bin/dynamic/libcrypto_hash.so: bin/dynamic build_crypto_hash
	cp crypto_hash/bin/libcrypto_hash.so bin/dynamic/



.PHONY: libcrypto_hashblocks build_crypto_hashblocks

libcrypto_hashblocks: bin/static/libcrypto_hashblocks.a bin/dynamic/libcrypto_hashblocks.so

build_crypto_hashblocks:
	$(MAKE) -C crypto_hashblocks

bin/static/libcrypto_hashblocks.a: bin/static build_crypto_hashblocks
	cp crypto_hashblocks/bin/libcrypto_hashblocks.a bin/static/

bin/dynamic/libcrypto_hashblocks.so: bin/dynamic build_crypto_hashblocks
	cp crypto_hashblocks/bin/libcrypto_hashblocks.so bin/dynamic/



.PHONY: libcrypto_rng build_crypto_rng

libcrypto_rng: bin/static/libcrypto_rng.a bin/dynamic/libcrypto_rng.so

build_crypto_rng: libcrypto_stream
	$(MAKE) -C crypto_rng

bin/static/libcrypto_rng.a: bin/static build_crypto_rng
	cp crypto_rng/bin/libcrypto_rng.a bin/static/

bin/dynamic/libcrypto_rng.so: bin/dynamic build_crypto_rng
	cp crypto_rng/bin/libcrypto_rng.so bin/dynamic/



.PHONY: libcrypto_stream build_crypto_stream

libcrypto_stream: bin/static/libcrypto_stream.a bin/dynamic/libcrypto_stream.so

build_crypto_stream: libcrypto_core
	$(MAKE) -C crypto_stream

bin/static/libcrypto_stream.a: bin/static build_crypto_stream
	cp crypto_stream/bin/libcrypto_stream.a bin/static/

bin/dynamic/libcrypto_stream.so: bin/dynamic build_crypto_stream
	cp crypto_stream/bin/libcrypto_stream.so bin/dynamic/



.PHONY: libcrypto_verify build_crypto_verify

libcrypto_verify: bin/static/libcrypto_verify.a bin/dynamic/libcrypto_verify.so

build_crypto_verify:
	$(MAKE) -C crypto_verify

bin/static/libcrypto_verify.a: bin/static build_crypto_verify
	cp crypto_verify/bin/libcrypto_verify.a bin/static/

bin/dynamic/libcrypto_verify.so: bin/dynamic build_crypto_verify
	cp crypto_verify/bin/libcrypto_verify.so bin/dynamic/



.PHONY: libfastrandombytes build_fastrandombytes

libfastrandombytes: bin/static/libfastrandombytes.a bin/dynamic/libfastrandombytes.so

build_fastrandombytes: libcrypto_rng libkernelrandombytes
	$(MAKE) -C fastrandombytes

bin/static/libfastrandombytes.a: bin/static build_fastrandombytes
	cp fastrandombytes/bin/libfastrandombytes.a bin/static/

bin/dynamic/libfastrandombytes.so: bin/dynamic build_fastrandombytes
	cp fastrandombytes/bin/libfastrandombytes.so bin/dynamic/



.PHONY: libkernelrandombytes build_kernelrandombytes

libkernelrandombytes: bin/static/libkernelrandombytes.a bin/dynamic/libkernelrandombytes.so

build_kernelrandombytes:
	$(MAKE) -C kernelrandombytes
	$(MAKE) -C kernelrandombytes test

bin/static/libkernelrandombytes.a: bin/static build_kernelrandombytes
	cp kernelrandombytes/bin/libkernelrandombytes.a bin/static/

bin/dynamic/libkernelrandombytes.so: bin/dynamic build_kernelrandombytes
	cp kernelrandombytes/bin/libkernelrandombytes.so bin/dynamic/



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
	rm -rf bin
