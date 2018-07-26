// #include "api.h"
#define CRYPTO_KEYBYTES 32
#define CRYPTO_NONCEBYTES 8

// #include "crypto_stream_salsa20.h"
#define crypto_stream_salsa20_ref_KEYBYTES 32
#define crypto_stream_salsa20_ref_NONCEBYTES 8
 
extern int crypto_stream_salsa20_ref(unsigned char *,unsigned long long,const unsigned char *,const unsigned char *);
extern int crypto_stream_salsa20_ref_xor(unsigned char *,const unsigned char *,unsigned long long,const unsigned char *,const unsigned char *);

// #include "crypto_stream.h"
