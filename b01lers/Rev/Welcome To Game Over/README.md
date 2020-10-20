<div style="text-align: justify">

# Welcome To Game Over 100 Points

## Description
```
Welcome to the game, Shark Boy. I call the game....Game Over. Wait....shark boy isn't from this movie??? What?

You have a terminal and you have your wits. Find the exit. Good luck.

Author: @novafacing
File: game-over
Size: 16.67 KB
MD5: 864353a02a081583217023180193b86e
```

## Problem
```
~/CTFtime2020/b01lers/Rev/Welcome To Game Over on master ?6 ❯ ./game-over

sharkboy@gameover > ./getemail.sh
I was fired.                          
I know.
I hacked into the O.S.S. data files and saw the news.
It was probably my fault, I suppose.
I am sorry.%
```
In this challenge we are given a binary file [*game-over*](game-over). After executing the program we get a message, but don't give the quiet clue flag.

```
[0x00001100]> pdg@main

void main(void)
{
    char *var_8h;
    
    sym.imp.puts("\nsharkboy@gameover > ./getemail.sh");
    sym.imp.fflush(_reloc.stdout);
    sym.flashprint("**** INCOMING MESSAGE FROM CARMEN ****", 700, 5);
    sym.funprint(
                 "I was fired.\nI know.\nI hacked into the O.S.S. data files and saw the news.\nIt was probably my fault, I suppose.\nI am sorry."
                 , 300);
    sym._my_little_thumbling("flag{welc0me_to_th3_game<FIND_THE_REST_OF_THE_FLAG_IN_FUNCTION_NAMES>}");
    return;
}
```
After looking at the pseudocode of the `sym.main` function, we get a piece of the flag and a clue to get a chunk of that flag.

## Solution
The rest of the flags are the function names from the flags we found earlier.

```
    sym._my_little_thumbling("flag{welc0me_to_th3_game<FIND_THE_REST_OF_THE_FLAG_IN_FUNCTION_NAMES>}");
```

FLAG: `flag{welc0me_to_th3_game_my_little_thumbling}`
</div>