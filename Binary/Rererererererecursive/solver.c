#include <stdio.h>
#include <stdint.h>
unsigned long long int print_flag(long long int a1)
{
  long long int v2; // [rsp+8h] [rbp-B8h] BYREF
  char *v3; // [rsp+10h] [rbp-B0h]
  long long int *v4; // [rsp+18h] [rbp-A8h]
  long long int v5[8]; // [rsp+20h] [rbp-A0h] BYREF
  int v6; // [rsp+60h] [rbp-60h]
  char s[8]; // [rsp+70h] [rbp-50h] BYREF
  long long int v8; // [rsp+78h] [rbp-48h]
  long long int v9; // [rsp+80h] [rbp-40h]
  long long int v10; // [rsp+88h] [rbp-38h]
  long long int v11; // [rsp+90h] [rbp-30h]
  long long int v12; // [rsp+98h] [rbp-28h]
  long long int v13; // [rsp+A0h] [rbp-20h]
  long long int v14; // [rsp+A8h] [rbp-18h]
  int v15; // [rsp+B0h] [rbp-10h]
  unsigned long long int v16; // [rsp+B8h] [rbp-8h]
  long long int savedregs; // [rsp+C0h] [rbp+0h] BYREF

  v2 = a1;
  v4 = &v2;
  v5[0] = 0xCF9B9E84989E9399LL;
  v5[1] = 0x8DA0CB93A097CF8DLL;
  v5[2] = 0x9190968C8D8A9CCCLL;
  v5[3] = 0x99CAC79BCFCFA09ALL;
  v5[4] = 0x9CC89DCB9E9DC9CDLL;
  v5[5] = 0xCC9C9DC999C69DCALL;
  v5[6] = 0xC6C8CDCEC89D9CCCLL;
  v5[7] = 0x9C9BC99CCAC8C699LL;
  v6 = 8572878;
  v3 = (char*)v5;
  *(long long int *)s = 0;
  v8 = 0;
  v9 = 0;
  v10 = 0;
  v11 = 0;
  v12 = 0;
  v13 = 0;
  v14 = 0;
  v15 = 0;
    while ( *v3 )
  {
    v3[80] = *((char *)v4 + (((char)v3 - ((unsigned char)&savedregs + 96)) & 7)) ^ *v3;
    ++v3;
  }
  puts(s);
  return 0;
}
int main(){
    unsigned long long int num=0xFFFFFFFFFFFFFFFF;
    print_flag(num);
}