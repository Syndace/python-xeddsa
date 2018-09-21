cmake_minimum_required(VERSION 3.5)

INCLUDE(CheckSymbolExists)

if (UNIX)
    CHECK_SYMBOL_EXISTS(getentropy         "sys/random.h"            RANDOM_SOURCE_getentropy)
    CHECK_SYMBOL_EXISTS(getentropy         "unistd.h"                RANDOM_SOURCE_getentropy2)
    CHECK_SYMBOL_EXISTS(getrandom          "unistd.h;sys/random.h"   RANDOM_SOURCE_getrandom)
    CHECK_SYMBOL_EXISTS(getrandom          "unistd.h;linux/random.h" RANDOM_SOURCE_getrandom2)
    CHECK_SYMBOL_EXISTS(SYS_getrandom      "unistd.h;syscall.h"      RANDOM_SOURCE_getrandom3)
    CHECK_SYMBOL_EXISTS(SecRandomCopyBytes "Security/Security.h"     RANDOM_SOURCE_secrandomcopybytes)

    if () # None of the above
        set(RANDOM_SOURCE_urandom TRUE)
    endif ()
endif (UNIX)

set(RANDOM_SOURCE_rtlgenrandom WIN32)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin/static)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin/dynamic)

include_directories(include)

###############
# crypto_core #
###############

set(crypto_core_sources
    crypto_core/core.c
)

add_library(crypto_core_static  STATIC ${crypto_core_sources})
add_library(crypto_core_dynamic SHARED ${crypto_core_sources})

###############
# crypto_hash #
###############

set(crypto_hash_sources
    crypto_hash/hash.c
)

add_library(crypto_hash_static  STATIC ${crypto_hash_sources})
add_library(crypto_hash_dynamic SHARED ${crypto_hash_sources})

#####################
# crypto_hashblocks #
#####################

set(crypto_hashblocks_sources
    crypto_hashblocks/blocks.c
)

add_library(crypto_hashblocks_static  STATIC ${crypto_hashblocks_sources})
add_library(crypto_hashblocks_dynamic SHARED ${crypto_hashblocks_sources})

##############
# crypto_rng #
##############

set(crypto_rng_sources
    crypto_rng/rng.c
)

add_library(crypto_rng_static  STATIC ${crypto_rng_sources})
add_library(crypto_rng_dynamic SHARED ${crypto_rng_sources})

#####################
# crypto_scalarmult #
#####################

set(crypto_scalarmult_sources
    crypto_scalarmult/base.c
    crypto_scalarmult/fe_0.c
    crypto_scalarmult/fe_1.c
    crypto_scalarmult/fe_add.c
    crypto_scalarmult/fe_copy.c
    crypto_scalarmult/fe_cswap.c
    crypto_scalarmult/fe_frombytes.c
    crypto_scalarmult/fe_invert.c
    crypto_scalarmult/fe_mul121666.c
    crypto_scalarmult/fe_mul.c
    crypto_scalarmult/fe_sq.c
    crypto_scalarmult/fe_sub.c
    crypto_scalarmult/fe_tobytes.c
    crypto_scalarmult/scalarmult.c
)

add_library(crypto_scalarmult_static  STATIC ${crypto_scalarmult_sources})
add_library(crypto_scalarmult_dynamic SHARED ${crypto_scalarmult_sources})

###############
# crypto_sign #
###############

set(crypto_sign_sources
    crypto_sign/fe_0.c
    crypto_sign/fe_1.c
    crypto_sign/fe_add.c
    crypto_sign/fe_cmov.c
    crypto_sign/fe_copy.c
    crypto_sign/fe_frombytes.c
    crypto_sign/fe_invert.c
    crypto_sign/fe_isnegative.c
    crypto_sign/fe_isnonzero.c
    crypto_sign/fe_mul.c
    crypto_sign/fe_neg.c
    crypto_sign/fe_pow22523.c
    crypto_sign/fe_sq2.c
    crypto_sign/fe_sq.c
    crypto_sign/fe_sub.c
    crypto_sign/fe_tobytes.c
    crypto_sign/ge_add.c
    crypto_sign/ge_double_scalarmult.c
    crypto_sign/ge_frombytes.c
    crypto_sign/ge_madd.c
    crypto_sign/ge_msub.c
    crypto_sign/ge_p1p1_to_p2.c
    crypto_sign/ge_p1p1_to_p3.c
    crypto_sign/ge_p2_0.c
    crypto_sign/ge_p2_dbl.c
    crypto_sign/ge_p3_0.c
    crypto_sign/ge_p3_dbl.c
    crypto_sign/ge_p3_tobytes.c
    crypto_sign/ge_p3_to_cached.c
    crypto_sign/ge_p3_to_p2.c
    crypto_sign/ge_precomp_0.c
    crypto_sign/ge_scalarmult_base.c
    crypto_sign/ge_sub.c
    crypto_sign/ge_tobytes.c
    crypto_sign/keypair.c
    crypto_sign/open.c
    crypto_sign/sc_muladd.c
    crypto_sign/sc_reduce.c
    crypto_sign/sign.c
)

add_library(crypto_sign_static  STATIC ${crypto_sign_sources})
add_library(crypto_sign_dynamic SHARED ${crypto_sign_sources})

#################
# crypto_stream #
#################

set(crypto_stream_sources
    crypto_stream/stream.c
    crypto_stream/xor.c
)

add_library(crypto_stream_static  STATIC ${crypto_stream_sources})
add_library(crypto_stream_dynamic SHARED ${crypto_stream_sources})

#################
# crypto_verify #
#################

set(crypto_verify_sources
    crypto_verify/verify.c
)

add_library(crypto_verify_static  STATIC ${crypto_verify_sources})
add_library(crypto_verify_dynamic SHARED ${crypto_verify_sources})

###################
# fastrandombytes #
###################

set(fastrandombytes_sources
    fastrandombytes/fastrandombytes.c
)

add_library(fastrandombytes_static  STATIC ${fastrandombytes_sources})
add_library(fastrandombytes_dynamic SHARED ${fastrandombytes_sources})

#####################
# kernelrandombytes #
#####################

set(kernelrandombytes_sources
    kernelrandombytes/getentropy2.c
    kernelrandombytes/getentropy.c
    kernelrandombytes/getrandom2.c
    kernelrandombytes/getrandom3.c
    kernelrandombytes/getrandom.c
    kernelrandombytes/rtlgenrandom.c
    kernelrandombytes/secrandomcopybytes.c
    kernelrandombytes/test.c
    kernelrandombytes/urandom.c
)

add_library(kernelrandombytes_static  STATIC ${kernelrandombytes_sources})
add_library(kernelrandombytes_dynamic SHARED ${kernelrandombytes_sources})

################
# DEPENDENCIES #
################

target_link_libraries(crypto_sign_static  crypto_hash_static  crypto_verify_static  fastrandombytes_static)
target_link_libraries(crypto_sign_dynamic crypto_hash_dynamic crypto_verify_dynamic fastrandombytes_dynamic)

target_link_libraries(crypto_hash_static  crypto_hashblocks_static)
target_link_libraries(crypto_hash_dynamic crypto_hashblocks_dynamic)

target_link_libraries(fastrandombytes_static  crypto_rng_static  kernelrandombytes_static)
target_link_libraries(fastrandombytes_dynamic crypto_rng_dynamic kernelrandombytes_dynamic)

target_link_libraries(crypto_rng_static  crypto_stream_static)
target_link_libraries(crypto_rng_dynamic crypto_stream_dynamic)

target_link_libraries(crypto_stream_static  crypto_core_static)
target_link_libraries(crypto_stream_dynamic crypto_core_dynamic)
