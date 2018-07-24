#include <Windows.h>

HMODULE advapi32 = LoadLibrary("ADVAPI32.DLL");
BOOLEAN (APIENTRY *RtlGenRandom)(PVOID, ULONG) = (BOOLEAN (APIENTRY*)(PVOID, ULONG)) GetProcAddress(advapi32, "SystemFunction036");

void kernelrandombytes(unsigned char *x,unsigned long long xlen)
{
  int i;

  while (xlen > 0) {
    if (xlen < 256) i = xlen; else i = 256;
    RtlGenRandom(x, i);
    x += i;
    xlen -= i;
  }
}
