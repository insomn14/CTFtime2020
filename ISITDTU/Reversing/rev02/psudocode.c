void FUN_9388(byte param_1)
{
  FUN_93df(param_1,0);
  if ((char)(DAT_0033 & DAT_0041) < '\0') {
    FUN_939d(DAT_0033);
    return;
  }
  return;
}

byte FUN_944e(byte param_1)
{
  byte bVar1;
  ushort uVar2;
  
  bVar1 = *DAT_0031;
  uVar2 = (ushort)DAT_0031 & 0xff00;
  if (0xfd < (byte)DAT_0031) {
    DAT_0031._1_1_ = (char)(uVar2 >> 8);
    uVar2 = (ushort)(byte)(DAT_0031._1_1_ + 1) << 8;
  }
  DAT_0031 = (byte *)(uVar2 | (byte)((byte)DAT_0031 + 2));
  DAT_0041 = param_1 ^ bVar1;
  return param_1 ^ bVar1;
}


void RESET(byte param_1)
{
  undefined xx;
  byte yy;
  bool bVar1;
  char cVar2;
  char cVar3;
  short sVar4;
  bool bVar5;
  bool bVar6;
  
  write_1(DAT_4017,0x40);
  sVar4 = CONCAT11((char)((ushort)register0x22 >> 8),0xff);
  write_1(DAT_2001,0);
  write_1(DAT_4010,0);
  write_1(DAT_2000,0);
  read(DAT_2002);
  do {
    yy = read_1(DAT_2002);
  } while (-1 < (char)(param_1 & yy));
  do {
    yy = read_1(DAT_2002);
  } while (-1 < (char)(param_1 & yy));
  write_1(DAT_2006,0x3f);
  write_1(DAT_2006,0);
  yy = 0x20;
  do {
    write_1(DAT_2007,0xf);
    yy = yy - 1;
  } while (yy != 0);
  write_1(DAT_2006,0x20);
  write_1(DAT_2006,0);
  cVar2 = '\x10';
  do {
    do {
      write_1(DAT_2007,0);
      yy = yy + 1;
    } while (yy != 0);
    cVar2 = cVar2 + -1;
  } while (cVar2 != '\0');
  do {
    *(undefined *)(ushort)yy = 0;
    *(undefined *)((ushort)yy + 0x100) = 0;
    *(undefined *)((ushort)yy + 0x200) = 0;
    *(undefined *)((ushort)yy + 0x300) = 0;
    *(undefined *)((ushort)yy + 0x400) = 0;
    *(undefined *)((ushort)yy + 0x500) = 0;
    *(undefined *)((ushort)yy + 0x600) = 0;
    *(undefined *)((ushort)yy + 0x700) = 0;
    yy = yy + 1;
  } while (yy != 0);
  FUN_8276(4,0);
  FUN_824b();
  FUN_82a3();
  FUN_9460();
  FUN_9345();
  DAT_0031._0_1_ = 0;
  DAT_0031._1_1_ = 8;
  write_1(DAT_0016,0x80);
  write_1(DAT_2000,0x80);
  write_1(DAT_0018,6);
  cVar2 = read_1(DAT_0001);
  do {
    cVar3 = read_1(DAT_0001);
  } while (cVar2 == cVar3);
  cVar2 = '4';
  cVar3 = '\x18';
  do {
    do {
      cVar2 = cVar2 + -1;
    } while (cVar2 != '\0');
    cVar3 = cVar3 + -1;
  } while (cVar3 != '\0');
  yy = read_1(DAT_2002);
  write_1(DAT_0000,yy & 0x80);
  FUN_827d();
  FUN_8502(0,0);
  xx = read_1(DAT_0000);
  FUN_8a9c(xx,0x83,-0x6c);
  FUN_8e83(0x83,0x94);
  write_1(DAT_0019,0xfd);
  write_1(DAT_001a,0xfd);
  write_1(DAT_2005,0);
  write_1(DAT_2005,0);
  I = 0;
  do {
      FUN_8365();
      tmp = FUN_84c5(0);
    if (tmp != '\0') {
      if (tmp == -128) {
        tmp = 't';
      }
      if (tmp == '@') {
        tmp = 'u';
      }
      if (tmp == ' ') {
        tmp = 'a';
      }
      if (tmp == '\x10') {
        tmp = 'n';
      }
      if (tmp == '\x02') {
        tmp = 'l';
      }
      if (tmp == '\x01') {
        tmp = 'i';
      }
      if (tmp == '\b') {
        tmp = 'n';
      }
      if (tmp == '\x04') {
        tmp = 'h';
      }
                    /* AA */
      *(char *)((ushort)I + 0x300) = tmp;
      I = I + 1;
      tmp = '\0';
    }
  } while (0xf < I);
  FUN_827d();
  FUN_8228(0xaa,0x94);
  FUN_8560(0xca,0x21);
  
  bVar5 = CARRY1(AA,BB);
  bVar1 = bVar5 != false;
  if (CARRY1(AA + BB,CC) != false) {
    bVar1 = (bool)(bVar1 + '\x01');
  }
  if ((bVar1 == true) && ((byte)(AA + BB + CC + (bVar5 == false && bVar5)) == 'J')) {
    bVar6 = CARRY1(BB,CC);
    bVar5 = false;
    if (bVar6 != false) {
      bVar5 = bVar1;
    }
    if (CARRY1(BB + CC,DD) != false) {
      bVar5 = (bool)(bVar5 + '\x01');
    }
    if ((bVar5 == true) && ((byte)(BB + CC + DD + (bVar6 == false && bVar6)) == 'D')) {
      bVar6 = CARRY1(CC,DD);
      bVar1 = false;
      if (bVar6 != false) {
        bVar1 = bVar5;
      }
      if (CARRY1(CC + DD,EE) != false) {
        bVar1 = (bool)(bVar1 + '\x01');
      }
      if ((bVar1 == true) && ((byte)(CC + DD + EE + (bVar6 == false && bVar6)) == ';')) {
        bVar6 = CARRY1(DD,EE);
        bVar5 = false;
        if (bVar6 != false) {
          bVar5 = bVar1;
        }
        if (CARRY1(DD + EE,FF) != false) {
          bVar5 = (bool)(bVar5 + '\x01');
        }
        if ((bVar5 == true) && ((byte)(DD + EE + FF + (bVar6 == false && bVar6)) == 'C')) {
          bVar6 = CARRY1(EE,FF);
          bVar1 = false;
          if (bVar6 != false) {
            bVar1 = bVar5;
          }
          if (CARRY1(EE + FF,GG) != false) {
            bVar1 = (bool)(bVar1 + '\x01');
          }
          if ((bVar1 == true) && ((byte)(EE + FF + GG + (bVar6 == false && bVar6)) == 'C')) {
            bVar6 = CARRY1(FF,GG);
            bVar5 = false;
            if (bVar6 != false) {
              bVar5 = bVar1;
            }
            if (CARRY1(FF + GG,HH) != false) {
              bVar5 = (bool)(bVar5 + '\x01');
            }
            if ((bVar5 == true) && ((byte)(FF + GG + HH + (bVar6 == false && bVar6)) == '?')) {
              bVar6 = CARRY1(GG,HH);
              bVar1 = false;
              if (bVar6 != false) {
                bVar1 = bVar5;
              }
              if (CARRY1(GG + HH,II) != false) {
                bVar1 = (bool)(bVar1 + '\x01');
              }
              if ((bVar1 == true) && ((byte)(GG + HH + II + (bVar6 == false && bVar6)) == 'B')) {
                bVar6 = CARRY1(HH,II);
                bVar5 = false;
                if (bVar6 != false) {
                  bVar5 = bVar1;
                }
                if (CARRY1(HH + II,JJ) != false) {
                  bVar5 = (bool)(bVar5 + '\x01');
                }
                if ((bVar5 == true) && ((byte)(HH + II + JJ + (bVar6 == false && bVar6)) == 'B')) {
                  bVar6 = CARRY1(II,JJ);
                  bVar1 = false;
                  if (bVar6 != false) {
                    bVar1 = bVar5;
                  }
                  if (CARRY1(II + JJ,KK) != false) {
                    bVar1 = (bool)(bVar1 + '\x01');
                  }
                  if ((bVar1 == true) && ((byte)(II + JJ + KK + (bVar6 == false && bVar6)) == 'B'))
                  {
                    bVar6 = CARRY1(JJ,KK);
                    bVar5 = false;
                    if (bVar6 != false) {
                      bVar5 = bVar1;
                    }
                    if (CARRY1(JJ + KK,LL) != false) {
                      bVar5 = (bool)(bVar5 + '\x01');
                    }
                    if ((bVar5 == true) && ((byte)(JJ + KK + LL + (bVar6 == false && bVar6)) == '7')
                       ) {
                      bVar6 = CARRY1(KK,LL);
                      bVar1 = false;
                      if (bVar6 != false) {
                        bVar1 = bVar5;
                      }
                      if (CARRY1(KK + LL,MM) != false) {
                        bVar1 = (bool)(bVar1 + '\x01');
                      }
                      if ((bVar1 == true) &&
                         ((byte)(KK + LL + MM + (bVar6 == false && bVar6)) == '=')) {
                        bVar6 = CARRY1(LL,MM);
                        bVar5 = false;
                        if (bVar6 != false) {
                          bVar5 = bVar1;
                        }
                        if (CARRY1(LL + MM,NN) != false) {
                          bVar5 = (bool)(bVar5 + '\x01');
                        }
                        if ((bVar5 == true) &&
                           ((byte)(LL + MM + NN + (bVar6 == false && bVar6)) == 'C')) {
                          bVar6 = CARRY1(MM,NN);
                          bVar1 = false;
                          if (bVar6 != false) {
                            bVar1 = bVar5;
                          }
                          if (CARRY1(MM + NN,OO) != false) {
                            bVar1 = (bool)(bVar1 + '\x01');
                          }
                          if ((bVar1 == true) &&
                             ((byte)(MM + NN + OO + (bVar6 == false && bVar6)) == 'K')) {
                            bVar6 = CARRY1(NN,OO);
                            bVar5 = false;
                            if (bVar6 != false) {
                              bVar5 = bVar1;
                            }
                            if (CARRY1(NN + OO,PP) != false) {
                              bVar5 = (bool)(bVar5 + '\x01');
                            }
                            if ((bVar5 == true) && ((byte)(NN + OO + PP + (bVar6 == false && bVar6)) == 'L')) {
                              I = 0;
                              while (yy = "Correct! ISITDTU{"[I], "Correct! ISITDTU{"[I] != 0) {
                                cVar2 = "Correct! ISITDTU{"[I];
                                                                PRINT(cVar2);
                                I = I + 1;
                              }
                              while (I = yy, 0x23 < I) {
                                // xx = *(I + 0x310);
                                // WIERD(xx);
                                
                                // yy = I;
                                // WIERD(yy);

                                // xx = FUN_9388(0x10);
                                // DAT_0039 = CONCAT11(bVar5 + '\x03',xx);

                                yy = *DAT_0039;
                                yy = FUN_944e(yy);

                                PRINT(yy);
                                yy = I + 1;
                              }
                              PRINT('}');
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  yy = read_1(DAT_0018);
  write_1(DAT_0018,yy | 0x18);
  FUN_8365();
  return;
}

