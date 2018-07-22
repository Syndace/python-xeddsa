.PHONY: all clean full_clean

all: bin/libcrypto_scalarmult.so bin/libcrypto_sign.so

bin:
	mkdir -p bin

bin/libcrypto_scalarmult.so: bin
	$(MAKE) -C crypto_scalarmult
	cp crypto_scalarmult/bin/libcrypto_scalarmult.so bin/

bin/libcrypto_sign.so: bin bin/crypto_core.a bin/crypto_hash.a bin/crypto_hashblocks.a bin/crypto_rng.a bin/crypto_stream.a bin/crypto_verify.a bin/fastrandombytes.a bin/kernelrandombytes.a
	$(MAKE) -C crypto_sign
	cp crypto_sign/bin/libcrypto_sign.so bin/

bin/crypto_core.a: bin
	$(MAKE) -C crypto_core
	cp crypto_core/bin/crypto_core.a bin/

bin/crypto_hash.a: bin
	$(MAKE) -C crypto_hash
	cp crypto_hash/bin/crypto_hash.a bin/

bin/crypto_hashblocks.a: bin
	$(MAKE) -C crypto_hashblocks
	cp crypto_hashblocks/bin/crypto_hashblocks.a bin/

bin/crypto_rng.a: bin
	$(MAKE) -C crypto_rng
	cp crypto_rng/bin/crypto_rng.a bin/

bin/crypto_stream.a: bin
	$(MAKE) -C crypto_stream
	cp crypto_stream/bin/crypto_stream.a bin/

bin/crypto_verify.a: bin
	$(MAKE) -C crypto_verify
	cp crypto_verify/bin/crypto_verify.a bin/

bin/fastrandombytes.a: bin
	$(MAKE) -C fastrandombytes
	cp fastrandombytes/bin/fastrandombytes.a bin/

bin/kernelrandombytes.a: bin
	$(MAKE) -C kernelrandombytes
	$(MAKE) -C kernelrandombytes test
	cp kernelrandombytes/bin/kernelrandombytes.a bin/

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
	rm -f bin/*.a

full_clean: clean
	$(MAKE) -C crypto_scalarmult full_clean
	$(MAKE) -C crypto_sign full_clean
	rm -rf bin
