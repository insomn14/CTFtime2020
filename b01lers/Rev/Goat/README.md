<div style="text-align: justify">

# Goat 200 Points

## Description
```
You've done Reverse Engineering in C... Can you do it in Java?

File: CrackMe.class
Size: 1.96 KB
MD5: f28f5016afb41928d976a91974223982
```

## Problem
```
~/CTFtime2020/b01lers/Rev/Goat on master !25 ?4 ❯ java CrackMe
What is the flag?
test
Not the flag :(
```
Pada tantangan kali ini kita diberikan sebuah file kelas java. Hampir sama dengan tantangan sebelum-sebelumnya, kita dminta untuk memasukan flag yang tepat. Berikut ini adalah hasil decompileasi dari [*CrackMe*](CrackMe.class) menggunakan [*Bytecode Viewer*](https://bytecodeviewer.com/).

```
        ...
        for (n = 0; n < string.length() / 2; ++n) {
            char c = arrc[string.length() - n - 1];
            arrc[string.length() - n - 1] = arrc[n];
            arrc[n] = c;
        }
        int[] arrn = new int[]{19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1};
        int[] arrn2 = new int[arrc.length];
        for (int i = arrn.length - 1; i >= 0; --i) {
            arrn2[i] = arrc[arrn[i]];
        }
        Random random = new Random();
        random.setSeed(431289L);
        int[] arrn3 = new int[string.length()];
        for (int i = 0; i < string.length(); ++i) {
            arrn3[i] = arrn2[i] ^ random.nextInt(i + 1);
        }
        Object object = "";
        for (int i = 0; i < arrn3.length; ++i) {
            object = (String)object + arrn3[i] + ".";
        }
        if (((String)object).equals("97.122.54.50.93.66.99.117.75.51.101.78.104.119.90.53.94.36.102.84.40.69.")) {
            System.out.println("Congrats! You got the flag!");
            return;
        }
        ...
```
As we can see our input will be rewritten upside down, then each position will be returned according to the `arrn` array. After that each index of our input will be xored with `random.nextInt (i + 1)` with the seed value `431289`, and the last one after our input is changed to `Object` the next step our input is compared to a string `object` .

## Solution
Since the only encryption used is to xor the input, we can easily solve this challenge by finding the value for `random.nextInt` with the seed `431289` then passing xor to the comparison value. The following is the output of my [*solver*](solver.py).

```
~/CTFtime2020/b/Rev/Goat on master !25 ?3 ❯ python solver.py
flag{J4V4_I$_th3_G04T}
```
```
~/CTFtime2020/b01lers/Rev/Goat on master !25 ?3 ❯ java CrackMe 
What is the flag?
flag{J4V4_I$_th3_G04T}
Congrats! You got the flag!
```

FLAG: `flag{J4V4_I$_th3_G04T}`
</div>