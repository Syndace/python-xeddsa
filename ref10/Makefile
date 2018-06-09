all: crypto_scalarmult.so crypto_sign.so

prepare:
	mkdir -p bin

crypto_scalarmult.so: prepare
	$(MAKE) -C crypto_scalarmult crypto_scalarmult.so
	cp crypto_scalarmult/bin/crypto_scalarmult.so bin/

crypto_sign.so: crypto_core.a crypto_hash.a crypto_hashblocks.a crypto_rng.a crypto_stream.a crypto_verify.a fastrandombytes.a kernelrandombytes.a
	$(MAKE) -C crypto_sign crypto_sign.so
	cp crypto_sign/bin/crypto_sign.so bin/

crypto_core.a: prepare
	$(MAKE) -C crypto_core crypto_core.a
	cp crypto_core/bin/crypto_core.a bin/

crypto_hash.a: prepare
	$(MAKE) -C crypto_hash crypto_hash.a
	cp crypto_hash/bin/crypto_hash.a bin/

crypto_hashblocks.a: prepare
	$(MAKE) -C crypto_hashblocks crypto_hashblocks.a
	cp crypto_hashblocks/bin/crypto_hashblocks.a bin/

crypto_rng.a: prepare
	$(MAKE) -C crypto_rng crypto_rng.a
	cp crypto_rng/bin/crypto_rng.a bin/

crypto_stream.a: prepare
	$(MAKE) -C crypto_stream crypto_stream.a
	cp crypto_stream/bin/crypto_stream.a bin/

crypto_verify.a: prepare
	$(MAKE) -C crypto_verify crypto_verify.a
	cp crypto_verify/bin/crypto_verify.a bin/

fastrandombytes.a: prepare
	$(MAKE) -C fastrandombytes fastrandombytes.a
	cp fastrandombytes/bin/fastrandombytes.a bin/

kernelrandombytes.a: prepare
	$(MAKE) -C kernelrandombytes kernelrandombytes.a
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
	rm -rf bin
