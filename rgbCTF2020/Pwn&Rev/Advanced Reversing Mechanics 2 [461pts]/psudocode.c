char encryptFlag(char *input)
{
  char *i;
  bool v4;
  int v1;
  int v3;
  int v5;
  int v6;
  int v7;

  v1 = *input;
  if ( *input )
  {
    for ( i = input; ; v1 = *i )
    {

      v6 = (v1 - 10);
      if ( v1 <= 0x4F )
      {
        (v1) = v1 + 70;
        if ( v6 <= 0x50 )
          (v1) = v6;
      }

      *i++ = (((v1 - 7) ^ 0x43) << 6) | (((v1 - 7) ^ 0x43) >> 2);
      v7 = i - input;

      if ( !*i )
        break;

      v3 = v7 - 5 * ((((1717986919 * v7) >> 32) >> 1) - (v7));
      v4 = v3 == 2;
      v5 = ((*i << (v3 & 7)) | (*i >> v3)) & 0xFF;
      if ( v4 )
        (v5) = v5 - 1;
      *i = v5;

    }
  }
  return input;
}


int __cdecl main(int argc, const char **argv, const char **envp)
{
  int *v3;
  int v4;
  char *v5;
  int v6;
  int v8;

  v3 = (int *)&v8;
  v4 = stpcpy(&v8, argv[1], envp) - (_DWORD)&v8;
  encryptFlag(&v8);
  if ( v4 )
  {
    v5 = (char *)&v8 + v4;
    do
    {
      v6 = *v3++;
      printf("%02X, ", v6);
    }
    while ( v3 != (int *)v5 );
  }
  putchar(10);
  return 0;
}