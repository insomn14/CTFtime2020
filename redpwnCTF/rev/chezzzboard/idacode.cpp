int func_add(int a1, int a2, int a3)
{
  return (a2 + a3);
}

int func_mul(int a1, int a2, int a3)
{
  return (a3 * a2);
}

int func_2mul_add(int a1, int a2, int a3)
{
  return (2 * (a3 + a2));
}

int func_mod(int a1, int a2, int a3)
{
  return (a3 % a2);
}

int func_256sub_sub(int a1, int a2, int a3)
{
  return (256 - a2 - a3);
}

int func_sub(int a1, int a2, int a3)
{
  return (a2 - a3);
}

int func_0(int *a1)
{
  return *a1;
}

int func_1(int a1)
{
  return (a1 + 4);
}

int HITUNG_HITUNG(int a1)
{
  int i;
  int j;
  int v2;
  int v5;

  v2 = 0;
  for ( i = 0; i <= 7; ++i )
  {
    for ( j = 0; j <= 7; ++j )
    {
      v5 = func_0((16 * (8 * i + j) + a1));
      func_1(16 * (8 * i + j) + a1);
      switch ( v5 )
      {
        case 0:
          v2 += func_add(a1, 8 - i, j + 9);
          break;
        case 1:
          v2 += func_mul(a1, 8 - i, j + 9);
          break;
        case 2:
          v2 += func_2mul_add(a1, 8 - i, j + 9);
          break;
        case 3:
          v2 += func_mod(a1, 8 - i, j + 9);
          break;
        case 4:
          v2 += func_256sub_sub(a1, 8 - i, j + 9);
          break;
        case 5:
          v2 += func_sub(a1, 8 - i, j + 9);
          break;
        default:
          continue;
      }
    }
  }
  return v2;
}

__int64 __fastcall sub_561E32CCA9F4(__int64 a1, int a2, int a3)
{
  return 16 * (8LL * a2 + a3) + a1;
}

__int64 __fastcall sub_561E32CC9282(__int64 a1)
{
  return *(unsigned int *)(a1 + 4);
}


int FLAG_HERE(int a1)
{
  int v1;
  int v2;
  int v3;
  int v4;
  unsigned int v5;
  char v7;
  int v8;
  unsigned int v9;
  unsigned int v10;
  unsigned int v11;
  unsigned int v12;
  int v13;
  char v14;
  char v15;
  unsigned int v16;

  v16 = __readfsqword(0x28u);
  v7 = 0;
  while ( !v7 )
  {
    if ( (a1 + 1024) )
      std::cout << "Black: Move from" ;
    else
      std::cout << "White: Move from";
    std::cin >> &v14;
    v8 = *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](&v14, 0LL)
       - 48;
    v10 = *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](&v14, 1LL)
        - 65;
    v9 = 8 - v8;
    std::cout << "To\n";
    std::cin >> &v14;
    v11 = 8 - (*(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](&v14, 0LL) - 48);
    v12 = *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](&v14, 1LL) - 65;
    v2 = sub_561E32CCA9F4(a1, v9, v10);
    if (sub_561E32CC9282(v2) != (a1 + 1024) )
    {
      if (sub_561E32CCA4A2(a1, v9, v10, v11, v12) == 0 )
      {
        std::cout << "Invalid";
      }
      else
      {
        v7 = 1;
      }
    }
    else
    {
      std::cout << "Invalid";
    }
  }
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(&v15, &v14);
  v13 = HITUNG_HITUNG(a1);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(&v15);
  if ( v13 == 467 )
  {
    system("cat flag.txt");
    v5 = 0;
  }
  else
  {
    (a1 + 1024) = (a1 + 1024) != 1;
    v5 = 1;
  }
  return v5;
}