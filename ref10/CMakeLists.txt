cmake_minimum_required(VERSION 3.5)

include(CheckSymbolExists)

if (UNIX)
    CHECK_SYMBOL_EXISTS(getentropy         "sys/random.h"            RANDOM_SOURCE_getentropy)
    CHECK_SYMBOL_EXISTS(getentropy         "unistd.h"                RANDOM_SOURCE_getentropy2)
    CHECK_SYMBOL_EXISTS(getrandom          "unistd.h;sys/random.h"   RANDOM_SOURCE_getrandom)
    CHECK_SYMBOL_EXISTS(getrandom          "unistd.h;linux/random.h" RANDOM_SOURCE_getrandom2)
    #CHECK_SYMBOL_EXISTS(SYS_getrandom      "unistd.h;syscall.h"      RANDOM_SOURCE_getrandom3)
    set(RANDOM_SOURCE_getrandom3 FALSE)
    CHECK_SYMBOL_EXISTS(SecRandomCopyBytes "Security/Security.h"     RANDOM_SOURCE_secrandomcopybytes)

    if (RANDOM_SOURCE_getentropy OR RANDOM_SOURCE_getentropy2 OR RANDOM_SOURCE_getrandom OR RANDOM_SOURCE_getrandom2 OR RANDOM_SOURCE_getrandom3 OR RANDOM_SOURCE_secrandomcopybytes)
        set(RANDOM_SOURCE_urandom FALSE)
    else ()
        set(RANDOM_SOURCE_urandom TRUE)
    endif ()
else (UNIX)
    set(RANDOM_SOURCE_getentropy         FALSE)
    set(RANDOM_SOURCE_getentropy2        FALSE)
    set(RANDOM_SOURCE_getrandom          FALSE)
    set(RANDOM_SOURCE_getrandom2         FALSE)
    set(RANDOM_SOURCE_getrandom3         FALSE)
    set(RANDOM_SOURCE_secrandomcopybytes FALSE)
    set(RANDOM_SOURCE_urandom            FALSE)
endif (UNIX)

if (WIN32)
    set(RANDOM_SOURCE_rtlgenrandom TRUE)
else (WIN32)
    set(RANDOM_SOURCE_rtlgenrandom FALSE)
endif (WIN32)

if (NOT UNIX OR WIN32)
    message(FATAL_ERROR "Unsupported operating system (neither UNIX nor Windows). CMake will exit.")
endif ()

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin/static)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin/dynamic)

include_directories(include)

###############
# crypto_core #
###############

set(crypto_core_sources
    crypto_core/core.c
)

add_library(crypto_core_objects OBJECT ${crypto_core_sources})

set_property(TARGET crypto_core_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_core_static  STATIC $<TARGET_OBJECTS:crypto_core_objects>)
add_library(crypto_core_dynamic SHARED $<TARGET_OBJECTS:crypto_core_objects>)

###############
# crypto_hash #
###############

set(crypto_hash_sources
    crypto_hash/hash.c
)

add_library(crypto_hash_objects OBJECT ${crypto_hash_sources})

set_property(TARGET crypto_hash_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_hash_static  STATIC $<TARGET_OBJECTS:crypto_hash_objects>)
add_library(crypto_hash_dynamic SHARED $<TARGET_OBJECTS:crypto_hash_objects>)

#####################
# crypto_hashblocks #
#####################

set(crypto_hashblocks_sources
    crypto_hashblocks/blocks.c
)

add_library(crypto_hashblocks_objects OBJECT ${crypto_hashblocks_sources})

set_property(TARGET crypto_hashblocks_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_hashblocks_static  STATIC $<TARGET_OBJECTS:crypto_hashblocks_objects>)
add_library(crypto_hashblocks_dynamic SHARED $<TARGET_OBJECTS:crypto_hashblocks_objects>)

##############
# crypto_rng #
##############

set(crypto_rng_sources
    crypto_rng/rng.c
)

add_library(crypto_rng_objects OBJECT ${crypto_rng_sources})

set_property(TARGET crypto_rng_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_rng_static  STATIC $<TARGET_OBJECTS:crypto_rng_objects>)
add_library(crypto_rng_dynamic SHARED $<TARGET_OBJECTS:crypto_rng_objects>)

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

add_library(crypto_scalarmult_objects OBJECT ${crypto_scalarmult_sources})

set_property(TARGET crypto_scalarmult_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_scalarmult_static  STATIC $<TARGET_OBJECTS:crypto_scalarmult_objects>)
add_library(crypto_scalarmult_dynamic SHARED $<TARGET_OBJECTS:crypto_scalarmult_objects>)

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

add_library(crypto_sign_objects OBJECT ${crypto_sign_sources})

set_property(TARGET crypto_sign_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_sign_static  STATIC $<TARGET_OBJECTS:crypto_sign_objects>)
add_library(crypto_sign_dynamic SHARED $<TARGET_OBJECTS:crypto_sign_objects>)

#################
# crypto_stream #
#################

set(crypto_stream_sources
    crypto_stream/stream.c
    crypto_stream/xor.c
)

add_library(crypto_stream_objects OBJECT ${crypto_stream_sources})

set_property(TARGET crypto_stream_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_stream_static  STATIC $<TARGET_OBJECTS:crypto_stream_objects>)
add_library(crypto_stream_dynamic SHARED $<TARGET_OBJECTS:crypto_stream_objects>)

#################
# crypto_verify #
#################

set(crypto_verify_sources
    crypto_verify/verify.c
)

add_library(crypto_verify_objects OBJECT ${crypto_verify_sources})

set_property(TARGET crypto_verify_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(crypto_verify_static  STATIC $<TARGET_OBJECTS:crypto_verify_objects>)
add_library(crypto_verify_dynamic SHARED $<TARGET_OBJECTS:crypto_verify_objects>)

###################
# fastrandombytes #
###################

set(fastrandombytes_sources
    fastrandombytes/fastrandombytes.c
)

add_library(fastrandombytes_objects OBJECT ${fastrandombytes_sources})

set_property(TARGET fastrandombytes_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(fastrandombytes_static  STATIC $<TARGET_OBJECTS:fastrandombytes_objects>)
add_library(fastrandombytes_dynamic SHARED $<TARGET_OBJECTS:fastrandombytes_objects>)

#####################
# kernelrandombytes #
#####################

set(kernelrandombytes_sources
    kernelrandombytes/test.c
)

if (RANDOM_SOURCE_getentropy)
    list(APPEND kernelrandombytes_sources kernelrandombytes/getentropy.c)
endif ()

if (RANDOM_SOURCE_getentropy2)
    list(APPEND kernelrandombytes_sources kernelrandombytes/getentropy2.c)
endif ()

if (RANDOM_SOURCE_getrandom)
    list(APPEND kernelrandombytes_sources kernelrandombytes/getrandom.c)
endif ()

if (RANDOM_SOURCE_getrandom2)
    list(APPEND kernelrandombytes_sources kernelrandombytes/getrandom2.c)
endif ()

if (RANDOM_SOURCE_getrandom3)
    list(APPEND kernelrandombytes_sources kernelrandombytes/getrandom3.c)
endif ()

if (RANDOM_SOURCE_secrandomcopybytes)
    list(APPEND kernelrandombytes_sources kernelrandombytes/secrandomcopybytes.c)
endif ()

if (RANDOM_SOURCE_rtlgenrandom)
    list(APPEND kernelrandombytes_sources kernelrandombytes/rtlgenrandom.c)
endif ()

if (RANDOM_SOURCE_urandom)
    list(APPEND kernelrandombytes_sources kernelrandombytes/urandom.c)
endif ()

add_library(kernelrandombytes_objects OBJECT ${kernelrandombytes_sources})

set_property(TARGET kernelrandombytes_objects PROPERTY POSITION_INDEPENDENT_CODE TRUE)

add_library(kernelrandombytes_static  STATIC $<TARGET_OBJECTS:kernelrandombytes_objects>)
add_library(kernelrandombytes_dynamic SHARED $<TARGET_OBJECTS:kernelrandombytes_objects>)

################
# DEPENDENCIES #
################

target_link_libraries(crypto_sign_static
    crypto_hash_static
    crypto_hashblocks_static
    crypto_verify_static
    fastrandombytes_static
    crypto_rng_static
    crypto_stream_static
    crypto_core_static
    kernelrandombytes_static
)

target_link_libraries(crypto_sign_dynamic
    crypto_hash_dynamic
    crypto_hashblocks_dynamic
    crypto_verify_dynamic
    fastrandombytes_dynamic
    crypto_rng_dynamic
    crypto_stream_dynamic
    crypto_core_dynamic
    kernelrandombytes_dynamic
)

target_include_directories(crypto_sign_objects PRIVATE
    crypto_hash
    crypto_hashblocks
    crypto_verify
    fastrandombytes
    crypto_rng
    crypto_stream
    crypto_core
    kernelrandombytes
)

target_link_libraries(crypto_hash_static  crypto_hashblocks_static)
target_link_libraries(crypto_hash_dynamic crypto_hashblocks_dynamic)
target_include_directories(crypto_hash_objects PRIVATE crypto_hashblocks)

target_link_libraries(fastrandombytes_static  crypto_rng_static  crypto_stream_static  crypto_core_static  kernelrandombytes_static)
target_link_libraries(fastrandombytes_dynamic crypto_rng_dynamic crypto_stream_dynamic crypto_core_dynamic kernelrandombytes_dynamic)
target_include_directories(fastrandombytes_objects PRIVATE crypto_rng crypto_stream crypto_core kernelrandombytes)

target_link_libraries(crypto_rng_static  crypto_stream_static  crypto_core_static)
target_link_libraries(crypto_rng_dynamic crypto_stream_dynamic crypto_core_dynamic)
target_include_directories(crypto_rng_objects PRIVATE crypto_stream crypto_core)

target_link_libraries(crypto_stream_static  crypto_core_static)
target_link_libraries(crypto_stream_dynamic crypto_core_dynamic)
target_include_directories(crypto_stream_objects PRIVATE crypto_core)
