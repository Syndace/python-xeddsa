// #include "api.h"
#define CRYPTO_BYTES 32
#define CRYPTO_SCALARBYTES 32

// #include <stdint.h>

// #include "crypto_int32.h"
typedef int32_t crypto_int32;

// #include "crypto_scalarmult_curve25519.h"
#define crypto_scalarmult_curve25519_ref10_BYTES 32
#define crypto_scalarmult_curve25519_ref10_SCALARBYTES 32
 
extern int crypto_scalarmult_curve25519_ref10(unsigned char *,const unsigned char *,const unsigned char *);
extern int crypto_scalarmult_curve25519_ref10_base(unsigned char *,const unsigned char *);

// #include "crypto_scalarmult.h"

// #include "fe.h"
typedef crypto_int32 fe[10];

/*
fe means field element.
Here the field is \Z/(2^255-19).
An element t, entries t[0]...t[9], represents the integer
t[0]+2^26 t[1]+2^51 t[2]+2^77 t[3]+2^102 t[4]+...+2^230 t[9].
Bounds on each t[i] vary depending on context.
*/

extern void crypto_scalarmult_curve25519_ref10_fe_frombytes(fe,const unsigned char *);
extern void crypto_scalarmult_curve25519_ref10_fe_tobytes(unsigned char *,fe);

extern void crypto_scalarmult_curve25519_ref10_fe_copy(fe,fe);
extern void crypto_scalarmult_curve25519_ref10_fe_0(fe);
extern void crypto_scalarmult_curve25519_ref10_fe_1(fe);
extern void crypto_scalarmult_curve25519_ref10_fe_cswap(fe,fe,unsigned int);

extern void crypto_scalarmult_curve25519_ref10_fe_add(fe,fe,fe);
extern void crypto_scalarmult_curve25519_ref10_fe_sub(fe,fe,fe);
extern void crypto_scalarmult_curve25519_ref10_fe_mul(fe,fe,fe);
extern void crypto_scalarmult_curve25519_ref10_fe_sq(fe,fe);
extern void crypto_scalarmult_curve25519_ref10_fe_mul121666(fe,fe);
extern void crypto_scalarmult_curve25519_ref10_fe_invert(fe,fe);
