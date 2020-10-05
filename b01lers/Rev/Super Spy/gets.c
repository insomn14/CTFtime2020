#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
  int i;
  int j;
  int y;
  char cStack53[28];
  char local_34;
  char uStack48;
  char uStack44;
  char local_28;
  char uStack36;
  char uStack32;
  char local_1c;
  char *flag_enc = "\x00\x44\x06\x39\x1d\x55\x1c\x15\x16\x5a\x6a\x5d\x5c\x54\x21\x16\x25\x60\x16\x29\x59\x1f\x19\x55\x57\x10\x44\x11";

  i = 0;
  do {
    while (j = i + 1, (i & 1) != 0) {
      (&Arr1)[i] = (&flag_enc)[i];
      i = j;
      if (j == 0x1c) goto LAB_080004de;
    }
    (&Arr2)[i] = (&flag_enc)[i];
    i = j;
  } while (j != 0x1c);
LAB_080004de:
  y = 0;
  do {
    y = y + 1;
    if (y == 1) {
      local_34 = local_34 & 0xffffff00 | ((Arr20 ^ 0x7a) + 0x28);
      y = y + 2;
    }
    (&cStack53)[y] = ((&Arr1)[y] ^ (&UNK)[y]) + 0x28;
    y = y;
  } while (y != 0x1c);
  Arr20 = local_34;
}

