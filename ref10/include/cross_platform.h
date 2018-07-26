#ifndef cross_platform_h
#define cross_platform_h

#ifdef _WIN32

// On Windows, the functions needs to explicitly be marked as import/export.
#define IMPORT __declspec(dllimport)
#define EXPORT __declspec(dllexport)

#elif __APPLE__

// On Apple OS', no such marking is required.
#define IMPORT
#define EXPORT

#elif __linux__

// On Linux, no such marking is required.
#define IMPORT
#define EXPORT

#else
#   error "Unknown OS"
#endif

#ifdef BUILD
#define INTERFACE EXPORT
#else
#define INTERFACE IMPORT
#endif

#endif
