from ctypes import *

libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libdl.so.2")

def gen_value(a1,a2,parm):
    for num in range(1,10):
        libc.srand((13 * ((100 * a1 + 10 * a2 + num) ^ 42) % 10067))
        res = libc.rand()
        if res == parm:
            return num
    return None

def main():
    val = [1754831936, 1322670498, 2075469024, 1924349448, 1737338032, 382094521, 2003484635, 1224890436, 613863398, 2131248558, 1855404474, 203716718, 2132752585, 54194304, 548400147, 2040844259, 348846481, 712829567, 198917626, 1999818593, 47214827, 117615071, 1948118465, 345110140, 2113220118, 443730372, 2136198019, 1427855150, 323649682, 1443247958]
    
    guess = [0 for _ in range(30)]
    guess[0] = gen_value(0,0,val[0])
    guess[1] = gen_value(0,4,val[1])
    guess[2] = gen_value(0,6,val[2])
    guess[3] = gen_value(0,7,val[3])
    guess[4] = gen_value(1,2,val[4])
    guess[5] = gen_value(1,4,val[5])
    guess[6] = gen_value(1,5,val[6])
    guess[7] = gen_value(1,6,val[7])
    guess[8] = gen_value(2,4,val[8])
    guess[9] = gen_value(2,5,val[9])
    guess[10] = gen_value(2,7,val[10])
    guess[11] = gen_value(3,0,val[11])
    guess[12] = gen_value(3,2,val[12])
    guess[13] = gen_value(4,0,val[13])
    guess[14] = gen_value(4,1,val[14])
    guess[15] = gen_value(4,7,val[15])
    guess[16] = gen_value(4,8,val[16])
    guess[17] = gen_value(5,6,val[17])
    guess[18] = gen_value(5,8,val[18])
    guess[19] = gen_value(6,1,val[19])
    guess[20] = gen_value(6,3,val[20])
    guess[21] = gen_value(6,4,val[21])
    guess[22] = gen_value(7,2,val[22])
    guess[23] = gen_value(7,3,val[23])
    guess[24] = gen_value(7,4,val[24])
    guess[25] = gen_value(7,6,val[25])
    guess[26] = gen_value(8,1,val[26])
    guess[27] = gen_value(8,2,val[27])
    guess[28] = gen_value(8,4,val[28])
    guess[29] = gen_value(8,8,val[29])
    for i,j in enumerate(guess):
        print(f'Guess: {j} --> Val: {val[i]}')
      
if __name__ == '__main__':
    main()
