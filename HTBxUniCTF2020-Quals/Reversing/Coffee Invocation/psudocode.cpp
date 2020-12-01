__int64 __fastcall JAV_SHIT1(__int64 java_thing, __int64 ARGV)
{
  void *AA; // rax
  void *EE; // rax
  __int64 (__fastcall *AA); // rbx
  __int64 BB; // r12
  __int64 CC; // rax
  __int64 DD; // rax
  __int64 FF; // rax
  __int64 HH; // rax
  void (__fastcall *JJ)(__int64, __int64, _QWORD, __int64); // rbx
  __int64 KK; // rax
  void (__fastcall *); // rbx
  __int64 WS; // rax
  void *NN; // rax
  void *OO; // rax
  __int64 java_THING; // [rsp+8h] [rbp-68h]
  __int64 LL; // [rsp+18h] [rbp-58h]
  void *NN; // [rsp+20h] [rbp-50h]
  __int64 verify1; // [rsp+28h] [rbp-48h]
  __int64 aa; // [rsp+30h] [rbp-40h]
  __int64 EE; // [rsp+38h] [rbp-38h]
  __int64 GG; // [rsp+40h] [rbp-30h]
  __int64 II; // [rsp+48h] [rbp-28h]
  __int64 MM; // [rsp+50h] [rbp-20h]
  unsigned __int64 AA6; // [rsp+58h] [rbp-18h]

  java_THING = java_thing;
  JAV_SHUTDOWN(java_thing, sub_1474);
  AA = CASE_CHOICE_ALPH(1);
  JAV_BYTE(java_thing, AA);
  EE = CASE_CHOICE_ALPH(2);
  JAV_SHORT(java_thing, EE);
  NN = FUNC_ANALYZE_PLZ(0, &LL);

  verify1 = *(java_THING + 40)(java_THING, "Verify1", 0, NN, LL);
  AA = *(java_thing + 1376);
  BB = *(java_THING + 1336)(java_THING, &STUPID_SHITTT);

  CC = *(java_THING + 48)(java_THING, "java/lang/String");// declaration String
  aa = AA(java_thing, 2, CC, BB);

  DD = *(java_THING + 1336)(java_THING, ARGV);
  EE = DD;
  FF = *(java_THING + 248)(java_THING, DD);

  HH = *(java_THING + 264)(java_THING, FF, "substring", "(II)Ljava/lang/String;");
  II = HH;
  JJ = *(java_thing + 1392);
  KK = *(java_THING + 272)(java_THING, EE, HH, 0, LAST_JAV_SHIT2); // KK = ARGV.SUBSTRING(0, 30)

  JJ(java_thing, aa, 0, KK);
   = *(java_thing + 1392);
  WS = *(java_THING + 1336)(java_THING, &Wierd_STRING);
  (java_thing, aa, 1, WS);
  MM = *(java_THING + 904)(java_THING, verify1, "main", "([Ljava/lang/String;)V");

  *(java_THING + 1128)(java_THING, verify1, MM, aa);

  NN = CASE_CHOICE_ALPH(0);
  JAV_BYTE(java_thing, NN);
  OO = CASE_CHOICE_ALPH(0);
  JAV_SHORT(java_thing, OO);
  return (unsigned int)XX;
}



__int64 __fastcall JAV_SHIT2(__int64 java_thing, __int64 ARGV)
{
  void *AA; // rax
  __int64 (__fastcall *EE)(__int64, __int64, __int64, __int64); // rbx
  __int64 FF; // r12
  __int64 GG; // rax
  __int64 II; // rax
  __int64 KK; // rax
  __int64 MM; // rax
  void (__fastcall *OO)(__int64, __int64, _QWORD, __int64); // rbx
  __int64 PP; // rax
  __int64 java_THING; // [rsp+8h] [rbp-68h]
  __int64 BB; // [rsp+18h] [rbp-58h]
  void *CC; // [rsp+20h] [rbp-50h]
  __int64 DD; // [rsp+28h] [rbp-48h]
  __int64 HH; // [rsp+30h] [rbp-40h]
  __int64 JJ; // [rsp+38h] [rbp-38h]
  __int64 LL; // [rsp+40h] [rbp-30h]
  __int64 NN; // [rsp+48h] [rbp-28h]
  __int64 QQ; // [rsp+50h] [rbp-20h]
  unsigned __int64 AA1; // [rsp+58h] [rbp-18h]

  java_THING = java_thing;
  XX = 2;
  JAV_SHUTDOWN(java_thing, sub_149A);
  AA = CASE_CHOICE_ALPH(3);
  JAV_CHAR(java_thing, AA);
  JAV_BOOLEAN(java_thing);

  CC = FUNC_ANALYZE_PLZ(1, &BB);
  DD = *(java_THING + 40)(java_THING, "Verify2", 0, CC, BB);
  EE = *(java_thing + 1376);
  FF = *(java_THING + 1336)(java_THING, &STUPID_SHITTT); // 0
  GG = *(java_THING + 48)(java_THING, "java/lang/String");
  HH = EE(java_thing, 1, GG, FF);

  II = *(java_THING + 1336)(java_THING, ARGV);
  JJ = II;
  KK = *(java_THING + 248)(java_THING, II);
  LL = KK;
  MM = *(java_THING + 264)(java_THING, KK, "substring", "(II)Ljava/lang/String;"); // MM = ARGV.SUBSTRING()

  OO = *(java_thing + 1392);
  PP = *(java_THING + 272)(java_THING, JJ, MM, LAST_JAV_SHIT2, LAST_JAV_SHIT2 + LAST_JAV_SHIT2_0);
  OO(java_thing, HH, 0, PP);
  QQ = *(java_THING + 904)(java_THING,DD,"main","([Ljava/lang/String;)V");
  *(java_THING + 1128)( java_THING, DD, QQ, HH);
  JAV_BOOLEAN(java_thing);
  return XX;
}