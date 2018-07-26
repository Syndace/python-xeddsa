// #include "api.h"
#define CRYPTO_OUTPUTBYTES 64
#define CRYPTO_INPUTBYTES 16
#define CRYPTO_KEYBYTES 32
#define CRYPTO_CONSTBYTES 16

// #include "crypto_core_salsa20.h"
#define crypto_core_salsa20_ref_OUTPUTBYTES 64
#define crypto_core_salsa20_ref_INPUTBYTES 16
#define crypto_core_salsa20_ref_KEYBYTES 32
#define crypto_core_salsa20_ref_CONSTBYTES 16
 
extern int crypto_core_salsa20_ref(unsigned char *,const unsigned char *,const unsigned char *,const unsigned char *);

// #include "crypto_core.h"
