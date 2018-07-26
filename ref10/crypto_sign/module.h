// #include "api.h"
#define CRYPTO_SECRETKEYBYTES 64
#define CRYPTO_PUBLICKEYBYTES 32
#define CRYPTO_BYTES 64

// #include <stdint.h>

// #include "crypto_int32.h"
typedef int32_t crypto_int32;

// #include "crypto_sign_ed25519.h"
#define crypto_sign_ed25519_ref10_SECRETKEYBYTES 64
#define crypto_sign_ed25519_ref10_PUBLICKEYBYTES 32
#define crypto_sign_ed25519_ref10_BYTES 64
 
extern int crypto_sign_ed25519_ref10(unsigned char *,unsigned long long *,const unsigned char *,unsigned long long,const unsigned char *);
extern int crypto_sign_ed25519_ref10_open(unsigned char *,unsigned long long *,const unsigned char *,unsigned long long,const unsigned char *);
extern int crypto_sign_ed25519_ref10_keypair(unsigned char *,unsigned char *);

// #include "crypto_sign.h"

// #include "fe.h"
typedef crypto_int32 fe[10];

/*
fe means field element.
Here the field is \Z/(2^255-19).
An element t, entries t[0]...t[9], represents the integer
t[0]+2^26 t[1]+2^51 t[2]+2^77 t[3]+2^102 t[4]+...+2^230 t[9].
Bounds on each t[i] vary depending on context.
*/

extern void crypto_sign_ed25519_ref10_fe_frombytes(fe,const unsigned char *);
extern void crypto_sign_ed25519_ref10_fe_tobytes(unsigned char *,const fe);

extern void crypto_sign_ed25519_ref10_fe_copy(fe,const fe);
extern int  crypto_sign_ed25519_ref10_fe_isnonzero(const fe);
extern int  crypto_sign_ed25519_ref10_fe_isnegative(const fe);
extern void crypto_sign_ed25519_ref10_fe_0(fe);
extern void crypto_sign_ed25519_ref10_fe_1(fe);
extern void crypto_sign_ed25519_ref10_fe_cmov(fe,const fe,unsigned int);

extern void crypto_sign_ed25519_ref10_fe_add(fe,const fe,const fe);
extern void crypto_sign_ed25519_ref10_fe_sub(fe,const fe,const fe);
extern void crypto_sign_ed25519_ref10_fe_neg(fe,const fe);
extern void crypto_sign_ed25519_ref10_fe_mul(fe,const fe,const fe);
extern void crypto_sign_ed25519_ref10_fe_sq(fe,const fe);
extern void crypto_sign_ed25519_ref10_fe_sq2(fe,const fe);
extern void crypto_sign_ed25519_ref10_fe_invert(fe,const fe);
extern void crypto_sign_ed25519_ref10_fe_pow22523(fe,const fe);

// #include "ge.h"
/*
ge means group element.

Here the group is the set of pairs (x,y) of field elements (see fe.h)
satisfying -x^2 + y^2 = 1 + d x^2y^2
where d = -121665/121666.

Representations:
  ge_p2 (projective): (X:Y:Z) satisfying x=X/Z, y=Y/Z
  ge_p3 (extended): (X:Y:Z:T) satisfying x=X/Z, y=Y/Z, XY=ZT
  ge_p1p1 (completed): ((X:Z),(Y:T)) satisfying x=X/Z, y=Y/T
  ge_precomp (Duif): (y+x,y-x,2dxy)
*/

typedef struct {
  fe X;
  fe Y;
  fe Z;
} ge_p2;

typedef struct {
  fe X;
  fe Y;
  fe Z;
  fe T;
} ge_p3;

typedef struct {
  fe X;
  fe Y;
  fe Z;
  fe T;
} ge_p1p1;

typedef struct {
  fe yplusx;
  fe yminusx;
  fe xy2d;
} ge_precomp;

typedef struct {
  fe YplusX;
  fe YminusX;
  fe Z;
  fe T2d;
} ge_cached;

extern void crypto_sign_ed25519_ref10_ge_tobytes(unsigned char *,const ge_p2 *);
extern void crypto_sign_ed25519_ref10_ge_p3_tobytes(unsigned char *,const ge_p3 *);
extern int  crypto_sign_ed25519_ref10_ge_frombytes_negate_vartime(ge_p3 *,const unsigned char *);

extern void crypto_sign_ed25519_ref10_ge_p2_0(ge_p2 *);
extern void crypto_sign_ed25519_ref10_ge_p3_0(ge_p3 *);
extern void crypto_sign_ed25519_ref10_ge_precomp_0(ge_precomp *);
extern void crypto_sign_ed25519_ref10_ge_p3_to_p2(ge_p2 *,const ge_p3 *);
extern void crypto_sign_ed25519_ref10_ge_p3_to_cached(ge_cached *,const ge_p3 *);
extern void crypto_sign_ed25519_ref10_ge_p1p1_to_p2(ge_p2 *,const ge_p1p1 *);
extern void crypto_sign_ed25519_ref10_ge_p1p1_to_p3(ge_p3 *,const ge_p1p1 *);
extern void crypto_sign_ed25519_ref10_ge_p2_dbl(ge_p1p1 *,const ge_p2 *);
extern void crypto_sign_ed25519_ref10_ge_p3_dbl(ge_p1p1 *,const ge_p3 *);

extern void crypto_sign_ed25519_ref10_ge_madd(ge_p1p1 *,const ge_p3 *,const ge_precomp *);
extern void crypto_sign_ed25519_ref10_ge_msub(ge_p1p1 *,const ge_p3 *,const ge_precomp *);
extern void crypto_sign_ed25519_ref10_ge_add(ge_p1p1 *,const ge_p3 *,const ge_cached *);
extern void crypto_sign_ed25519_ref10_ge_sub(ge_p1p1 *,const ge_p3 *,const ge_cached *);
extern void crypto_sign_ed25519_ref10_ge_scalarmult_base(ge_p3 *,const unsigned char *);
extern void crypto_sign_ed25519_ref10_ge_double_scalarmult_vartime(ge_p2 *,const unsigned char *,const ge_p3 *,const unsigned char *);

// #include "sc.h"
/*
The set of scalars is \Z/l
where l = 2^252 + 27742317777372353535851937790883648493.
*/

extern void crypto_sign_ed25519_ref10_sc_reduce(unsigned char *);
extern void crypto_sign_ed25519_ref10_sc_muladd(unsigned char *,const unsigned char *,const unsigned char *,const unsigned char *);
