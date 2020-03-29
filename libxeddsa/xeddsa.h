// #include <stdint.h>

extern int  xeddsa_init();
extern void curve25519_sign(uint8_t*, const uint8_t*, const uint8_t*, const uint32_t, const uint8_t*);
extern void curve25519_pub_to_ed25519_pub(uint8_t*, const uint8_t*);
