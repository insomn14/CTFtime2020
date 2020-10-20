<div style="text-align: justify">

# Thumb Thumb 100 Points

## Description
```
Once upon a time, there was a young Thumb Thumb named Juni. Juni was shy and had no self confidence, until one day evil Thumb Thumbs kidnapped his spy Thumb Thumb Parents.

WANTED: EVIL THUMB THUMB. CRIME: KIDNAPPING. HAVE YOU SEEN THIS THUMB?

Author: @novafacing
File: thumb-thumb
Size: 17.52 KB
MD5: cc35089e21b1f57ab7a17385b4e22be0
```

## Problem
The challenge this time we are given a binary file [*thumb-thumb*](thumb-thumb), if we execute the program will print a * thumb * in the form of ascii art. The following is the disassembly of one of the functions in the program.

```
[0x000011c0]> pdf @ sym.thumblings_assemble
│           0x000012a9      f30f1efa       endbr64
│           0x000012ad      55             push rbp
│           0x000012ae      4889e5         mov rbp, rsp
│           0x000012b1      4883c480       add rsp, 0xffffffffffffff80
│           0x000012b5      64488b042528.  mov rax, qword fs:[0x28]
│           0x000012be      488945f8       mov qword [canary], rax
│           0x000012c2      31c0           xor eax, eax
│           0x000012c4      c74590660000.  mov dword [var_70h], 0x66   ; 'f'
│           0x000012cb      c745e4750000.  mov dword [var_1ch], 0x75   ; 'u'
│           0x000012d2      c745a07b0000.  mov dword [var_60h], 0x7b   ; '{'
│           0x000012d9      c745ac6e0000.  mov dword [var_54h], 0x6e   ; 'n'
│           0x000012e0      c745b45f0000.  mov dword [var_4ch], 0x5f   ; '_'
│           0x000012e7      c745e86d0000.  mov dword [var_18h], 0x6d   ; 'm'
            ...
            ...
│           0x00001365      c745a4730000.  mov dword [var_5ch], 0x73   ; 's'
│           0x0000136c      c745e0680000.  mov dword [var_20h], 0x68   ; 'h'
│           0x00001373      c745ec620000.  mov dword [var_14h], 0x62   ; 'b'
│           0x0000137a      c745d0730000.  mov dword [var_30h], 0x73   ; 's'
│           0x00001381      c745f0350000.  mov dword [var_10h], 0x35   ; '5'
│           0x00001388      c745f47d0000.  mov dword [var_ch], 0x7d    ; '}'
│           0x0000138f      c7458c000000.  mov dword [var_74h], 0
│       ┌─< 0x00001396      eb11           jmp 0x13a9
│       │   ; CODE XREF from sym.thumblings_assemble @ 0x13ad
│      ┌──> 0x00001398      8b458c         mov eax, dword [var_74h]
│      ╎│   0x0000139b      4898           cdqe
│      ╎│   0x0000139d      c74485900000.  mov dword [rbp + rax*4 - 0x70], 0
│      ╎│   0x000013a5      83458c01       add dword [var_74h], 1
│      ╎│   ; CODE XREF from sym.thumblings_assemble @ 0x1396
│      ╎└─> 0x000013a9      837d8c19       cmp dword [var_74h], 0x19
│      └──< 0x000013ad      7ee9           jle 0x1398
│           0x000013af      90             nop
│           0x000013b0      488b45f8       mov rax, qword [canary]
│           0x000013b4      644833042528.  xor rax, qword fs:[0x28]
│       ┌─< 0x000013bd      7405           je 0x13c4
│       │   0x000013bf      e86cfdffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from sym.thumblings_assemble @ 0x13bd
│       └─> 0x000013c4      c9             leave
└           0x000013c5      c3             ret

```
From here we can see a character which I assume is a flag. The problem is that the flags are unlikely to ever print.

## Solution
To solve this challenge I did it by debugging the program, and defining a `PrintFlag` function to print the flags.

The following is a [*script*](solution.txt) of the `PrintFlag` function that I created.
```
set $i=0
set $addr=$rsp+16

while ($i < 27)
    printf "%s", $addr
    set $addr=$addr+4
    set $i=$i+1
    end
printf "\n"
end
```

Proof of concept.
```
~/CTFtimes2020/b01lers/Rev/Thumb Thumb > gdb -q ./thumb-thumb 
gef➤  start
...

gef➤  b *thumblings_assemble+230
Breakpoint 1 at 0x56081a61338f

gef➤  c
...
─────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007ffcd09705f0│+0x0000: 0x0000000000000000   ← $rsp
0x00007ffcd09705f8│+0x0008: 0x00007ffcd0972f9d  →  "/home/unknow/.linuxbrew/man:"
0x00007ffcd0970600│+0x0010: 0x0000006c00000066 ("f"?)
0x00007ffcd0970608│+0x0018: 0x0000006700000061 ("a"?)
0x00007ffcd0970610│+0x0020: 0x000000730000007b ("{"?)
0x00007ffcd0970618│+0x0028: 0x0000006e00000033 ("3"?)
0x00007ffcd0970620│+0x0030: 0x0000005f00000064 ("d"?)
0x00007ffcd0970628│+0x0038: 0x0000007500000030 ("0"?)
────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
   0x563b4e5b437a <thumblings_assemble+209> mov    DWORD PTR [rbp-0x30], 0x73
   0x563b4e5b4381 <thumblings_assemble+216> mov    DWORD PTR [rbp-0x10], 0x35
   0x563b4e5b4388 <thumblings_assemble+223> mov    DWORD PTR [rbp-0xc], 0x7d
 →0x563b4e5b438f <thumblings_assemble+230> mov    DWORD PTR [rbp-0x74], 0x0
...

gef➤  define PrintFlag
Type commands for definition of "PrintFlag".
End with a line saying just "end".
>
>set $i=0
>set $addr=$rsp+16
>
>while ($i < 27)
 >    printf "%s", $addr
 >    set $addr=$addr+4
 >    set $i=$i+1
 >    end
>printf "\n"
>end

gef➤  PrintFlag
flag{s3nd_0ur_b3st_thumb5}
```
FLAG: `flag{s3nd_0ur_b3st_thumb5}`
</div>