// #include "api.h"
#define CRYPTO_STATEBYTES 64
#define CRYPTO_BLOCKBYTES 128

// #include "crypto_hashblocks_sha512.h"
#define crypto_hashblocks_sha512_ref_STATEBYTES 64
#define crypto_hashblocks_sha512_ref_BLOCKBYTES 128
 
extern int crypto_hashblocks_sha512_ref(unsigned char *,const unsigned char *,unsigned long long);

// #include "crypto_hashblocks.h"
