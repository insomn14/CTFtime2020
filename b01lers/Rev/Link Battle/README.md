<div style="text-align: justify">

# Link Battle 100 Points

## Description
```  
Hmm....I hope you paid attention in class, spies!

Author: @novafacing
File: libflaggen.so
Size: 15.77 KB 
MD5: f2c2f9306bdbae9522d200db5bd9f55d
```

## Problem
```
~/CTFtime2020/b01lers/Rev/Link Battle ❯ file libflaggen.so
libflaggen.so: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=7cde260814d11798b4c5ca7b87f3a5a40b1aeb75, not stripped
```

In these chal we were given [*"Shared Object"*](libflaggen.so) file. If we open file with radare2, we can see clearly theres's function name `sym.getflag`.

```
[0x00001050]> afl
0x00001050    4 41   -> 34   entry0
0x00001110   14 320  -> 312  sym.getflag
0x00001030    1 6            sym.imp.putchar
```
```
[0x00001050]> pdg@sym.getflag

undefined8 sym.getflag(uint32_t arg1)
{
    ...
    
    if (arg1 != 0x1a0a) {
        return 0;
    }
    uVar10 = 0;
    _obj.start_state = 0x2122df7763817b1d;
    *(undefined4 *)0x40b8 = 0xbbb8887a;
    _obj.lfsr = 0x2122df7763817b1d;
    *(undefined4 *)0x40a8 = 0xbbb8887a;
    while( true ) {
        puVar8 = (uint32_t *)obj.fflag;
        do {
            puVar7 = puVar8;
            uVar3 = *puVar7 + 0xfefefeff & ~*puVar7;
            uVar4 = uVar3 & 0x80808080;
            puVar8 = puVar7 + 1;
        } while (uVar4 == 0);
        bVar12 = (uVar3 & 0x8080) == 0;
        if (bVar12) {
            uVar4 = uVar4 >> 0x10;
        }
        if (bVar12) {
            puVar8 = (uint32_t *)((int64_t)puVar7 + 6);
        }
        if ((int64_t)puVar8 + (-0x4043 - (uint64_t)CARRY1((uint8_t)uVar4, (uint8_t)uVar4)) <= uVar10) break;
        iVar9 = 1;
        do {
            uVar1 = *(uint16_t *)(obj.lfsr + iVar9 * 2);
            iVar5 = 0;
            do {
                uVar2 = uVar1 >> 1;
                uVar11 = uVar1 & 1;
                uVar1 = uVar2;
                if (uVar11 != 0) {
                    uVar1 = uVar2 ^ 0xb400;
                }
                iVar5 = iVar5 + 1;
            } while (iVar5 != (int32_t)iVar9);
            *(uint16_t *)(obj.lfsr + iVar9 * 2) = uVar1;
            iVar9 = iVar9 + 1;
        } while (iVar9 != 6);
        pcVar6 = obj.lfsr;
        do {
            pcVar6 = pcVar6 + 2;
        } while (pcVar6 != (code *)0x40aa);
        uVar10 = uVar10 + 1;
        sym.imp.putchar();
    }
    return 1;
}
```

As we can see in the `sym.getflag` function, the parameter `arg1` will compare it to the hex `0x1a0a` = `6666` in decimal. After that the function will start decrypting the `obj.fflag`.

## Solution
We can use python library *ctypes* to call `sym.getflag` function.

```
~/CTFtime2020/b01lers/Rev/Link Battle on master ?1 ❯ python -c 'import ctypes; lib=ctypes.CDLL("./libflaggen.so"); lib.getflag(6666)'
flag{pl34s3_sp34k_3ngl1sh_m1n10n!_1v3_been_b4k1ng_und3r_th0s3_st00d1o_l1ghts!}
```

FLAG: `flag{pl34s3_sp34k_3ngl1sh_m1n10n!_1v3_been_b4k1ng_und3r_th0s3_st00d1o_l1ghts!}`

</div>