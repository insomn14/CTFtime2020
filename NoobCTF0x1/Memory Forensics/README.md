# [Memory Forensic] Solution

## Mr. Pr0xy's Gift :) 10pts

```
I have some gifts for you in zip file. Download the file to get it. 

Good Luck !!! Hackers

`Link`: https://www.shortto.com/memdump
```

Download https://www.shortto.com/memdump and Extract image.zip

FLAG : `noob{Welcome_To_Memory_Forensic}`

***

## ##Parent Process## 80pts

```
What is the parent process id of Desktop Windows Manager?

Author: r3curs1v3_pr0xy
```

We can use <i>volatility</i> with pslist as Plugin command

```
# insomn14 @ unknow in ~/CTFtime2020/NoobCTF0x1/Memory Forensics on git:master x [17:56:32] 
$ vol.py --profile=Win7SP0x64 -f image.raw pslist
...
...
0xfffffa8003cb7190 dwm.exe                2512    856      3       70      1      0 2020-06-02 19:41:51 UTC+0000
...
...
```

FLAG : `noob{856}`

***

## Malicious Process 100pts



```
# insomn14 @ unknow in ~/CTFtime2020/NoobCTF0x1/Memory Forensics on git:master x [17:52:04] 
$ vol.py --profile=Win7SP0x64 -f image.raw cmdline
...
...
************************************************************************
spmm.exe pid:   2940
Command line : "C:\ProgramData\Security Monitor\{827D21CC-A22D-45D6-23CA-451DDAC769BA}\spmm.exe" "Spyrix Free Keylogger 11.5.21"
************************************************************************
...
...
```

FLAG : `noob{spmm.exe}`

