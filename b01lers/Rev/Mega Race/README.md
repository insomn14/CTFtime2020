<div style="text-align: justify">

# Mega Race 100 Points

## Description
```
There are 5 levels. This is level 2. Are you ready? Start your engines!

Author: @novafacing
File: mega-race
Size: 7.39 KB
MD5: 5d74802ba8a2dc3c928d3abf80420542
```

## Problem
```
~/CTFtime2020/b01lers/Rev/Mega Race ❯ ./mega-race
ENTER THE CHECKERED FLAG: 
```
On the challenge this time we were given file [*"mega-race.gzip"*](mega-race.gzip) that contain file binary [*"mega-race"*](mega-race), as seen in the program we are asked to enter the correct flags.

```
[0x00001480]> pdg@sym.scram

void sym.scram(char *arg1)
{
    char *pcVar1;
    char *s;
    char *var_10h;
    undefined8 var_8h;
    
    pcVar1 = (char *)sym.imp.strlen(arg1);
    var_10h = (char *)0x0;
    while (var_10h < pcVar1) {
        var_10h[(int64_t)arg1] = var_10h[(int64_t)arg1] ^ 0x77;
        var_10h = var_10h + 1;
    }
    return;
}

[0x00001480]> pdg@sym.getpasswd

int64_t sym.getpasswd(uint64_t arg1)
{
    int64_t iVar1;
    int64_t iVar2;
    undefined8 size;
    char *s;
    
    iVar1 = sym.imp.calloc(arg1 + 1, 1);
    iVar2 = sym.imp.fgets(iVar1, arg1 & 0xffffffff, _reloc.stdin, arg1 & 0xffffffff);
    if (iVar2 == 0) {
    // WARNING: Subroutine does not return
        sym.imp.exit(1);
    }
    *(undefined *)(arg1 + iVar1) = 0;
    return iVar1;
}

[0x00001480]> pdg@sym.asdfghjkl

bool sym.asdfghjkl(void)
{
    int32_t iVar1;
    char *arg1;
    char *s1;
    
    sym.imp.printf("ENTER THE CHECKERED FLAG: ");
    arg1 = (char *)sym.getpasswd(0x26);
    sym.scram(arg1);
    iVar1 = sym.imp.strcmp(arg1, obj.pass);
    return iVar1 == 0;
}

[0x00001480]> ps @ obj.pass
\x11\x1b\x16\x10\x0c\x14G\x19\x10\x05C\x03\x02\x1bC\x03FG\x19\x0d(\x0eG\x02(\x16\x05D(\x03\x1fD(0".V

```
After performing the static analysis we get a function to xor our input.
Each character in our input will be xored with hex `0x77`, the result of xored will be compared with the string in `obj.pass`.

## Solution
To get the flags, we can easily perform an xor operation on `obj.pass`
```
>>> data = b'\x11\x1b\x16\x10\x0c\x14G\x19\x10\x05C\x03\x02\x1bC\x03FG\x19\x0d(\x05D(\x03\x1fD(0".V'
>>> 
>>> 
>>> ''.join(chr(i^0x77) for i in data)
'flag{c0ngr4tul4t10nz_y0u_ar3_th3_GUY!'
```

```
~/CTFtime2020/b01lers/Rev/Mega Race ❯ ./mega-race
ENTER THE CHECKERED FLAG: flag{c0ngr4tul4t10nz_y0u_ar3_th3_GUY!}
Wow, you really hacked the OSS password? Nice work!
```

FLAG: `flag{c0ngr4tul4t10nz_y0u_ar3_th3_GUY!}`
</div>