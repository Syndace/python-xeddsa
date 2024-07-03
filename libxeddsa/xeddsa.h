// #include <stdbool.h>
// #include <stdint.h>

extern void ed25519_priv_sign(uint8_t*, const uint8_t*, const uint8_t*, const uint32_t, const uint8_t*);
extern void ed25519_seed_sign(uint8_t*, const uint8_t*, const uint8_t*, const uint32_t);
extern int  ed25519_verify(const uint8_t*, const uint8_t*, const uint8_t*, const uint32_t);

//extern void curve25519_pub_to_ed25519_pub(uint8_t*, const uint8_t*, const bool);
extern void curve25519_pub_to_ed25519_pub(uint8_t*, const uint8_t*, const uint8_t);
extern int  ed25519_pub_to_curve25519_pub(uint8_t*, const uint8_t*);

extern void priv_to_curve25519_pub(uint8_t*, const uint8_t*);
extern void priv_to_ed25519_pub(uint8_t*, const uint8_t*);
extern void seed_to_ed25519_pub(uint8_t*, const uint8_t*);

//extern void priv_force_sign(uint8_t*, const uint8_t*, const bool);
extern void priv_force_sign(uint8_t*, const uint8_t*, const uint8_t);
extern void seed_to_priv(uint8_t*, const uint8_t*);

extern int  x25519(uint8_t*, const uint8_t*, const uint8_t*);

extern int  xeddsa_init();

extern const unsigned XEDDSA_VERSION_MAJOR;
extern const unsigned XEDDSA_VERSION_MINOR;
extern const unsigned XEDDSA_VERSION_REVISION;
