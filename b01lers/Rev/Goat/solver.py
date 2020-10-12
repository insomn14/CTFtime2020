#!/usr/bin/env python3
import java

with java:
	from java.util import Random
	rand = Random()
	rand.setSeed(431289)

arrn = [19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1]
res = [97, 122, 54, 50, 93, 66, 99, 117, 75, 51, 101, 78, 104, 119, 90, 53, 94, 36, 102, 84, 40, 69]

inp = [chr(res[i]^rand.nextInt(i+1)) for i in range(22)]
inp = ''.join(inp[arrn.index(i)] for i in range(22))

print(inp[::-1])