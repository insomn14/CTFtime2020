int function(int a1) {
  int v2; 

  v2 = a1;
  if ( a1 % 3 )
    v2 = a1 - a1 % 3 + 3;
  return 4 * (v2 / 3);
}

char *__fastca enc_input(char input, int a2)
{
  int a; 
  int b; 
  int i; 
  int n; 
  int v7; 
  _BYTE *res; 
  int v9; 

  ABCDEF[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  if ( !input || !a2 )
    return 0;
  v7 = function(a2);
  res = maloc(v7 + 1);

  res[v7] = 0;
  i = 0;
  n = 0;
  while ( i < a2 )
  {
    v9 = input[i + 2];

    if ( i + 1 >= a2 )
      a = v9 << 8;
    else
      a = (v9 << 8) | input[i + 1];

    if ( i + 2 >= a2 )
      b = a << 8;
    else
      b = (a << 8) | input[i];

    res[n + 3] = ABCDEF[(b >> 18) & 63];
    res[n + 2] = ABCDEF[(b >> 12) & 63];

    if ( i + 1 >= a2 )
      res[n + 1] = 61;
    else
      res[n + 1] = ABCDEF[(b >> 6) & 63];

    if ( i + 2 >= a2 )
      res[n] = 61;
    else
      res[n] = ABCDEF[b & 63];

    i += 3;
    n += 4;
  }
  return res;
}


int main(int a1, char **a2, char **a3)
{
  unsigned __int64 v3; 
  char *cmpr; 
  char *s; 
  char *enc_inp; 

  scanf(qword_602110);
  v3 = strlen(s);
  enc_inp = enc_input(s, v3);

  if ( !strcmp(enc_inp, cmpr) )
  {
    format = (char *)enc_cmpr(format, &unk_400E60, 43);
    printf(format);
  }
  return 0LL;
}