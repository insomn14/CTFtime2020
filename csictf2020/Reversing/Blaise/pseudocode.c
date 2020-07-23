int f(int a1)
{
  int i;
  int v3;

  v3 = 1;
  for ( i = 2; i <= a1; ++i )
    v3 *= i;
  return v3;
}


int C(int a1, int a2)
{
  int v2;
  int v3;

  v2 = f(a1);
  v3 = f(a2);
  return v2 / (f(a1 - a2) * v3);
}

int process(int a1)
{
  int v2;
  int v3;
  int i;
  int v5;

  v5 = __readfsqword(0x28u);
  v3 = 1;
  for ( i = 0; (int)i <= (int)a1; ++i )
  {
    __isoc99_scanf("%d", &v2);
    if ( (int)C(a1, i) != v2 )
      v3 = 0;
  }
  if ( v3 == 1 )
    system("cat flag.txt");
  return 0;
}

int display_number(int a1, int a2)
{
  int v3;

  v3 = rand() % (a2 - a1 + 1) + a1;
  printf("%d\n", v3);
  return v3;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3;
  int v5;

  setbuf(stdout, 0);
  setbuf(stdin, 0);
  setbuf(stderr, 0);
  v3 = time(0);
  srand(v3);
  v5 = display_number(15, 20);
  process(v5);
  return 0;
}