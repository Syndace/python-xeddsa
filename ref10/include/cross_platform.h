#ifndef cross_platform_h
#define cross_platform_h

#ifdef _WIN32

// On Windows, the functions needs to explicitly be marked as import/export.
#define IMPORT __declspec(dllimport)
#define EXPORT __declspec(dllexport)

#elif __unix__

// On UNIX (using gcc), no such marking is required.
#define IMPORT
#define EXPORT

#else
#   error "Unsupported operating system (neither UNIX nor Windows)."
#endif

#ifdef BUILD
#define INTERFACE EXPORT
#else
#define INTERFACE IMPORT
#endif

#endif
