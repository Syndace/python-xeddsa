// #include "api.h"
#define CRYPTO_KEYBYTES 32
#define CRYPTO_OUTPUTBYTES 736

// #include "crypto_rng_salsa20.h"
#define crypto_rng_salsa20_ref_KEYBYTES 32
#define crypto_rng_salsa20_ref_OUTPUTBYTES 736
 
extern int crypto_rng_salsa20_ref(unsigned char *,unsigned char *,const unsigned char *);

// #include "crypto_rng.h"
