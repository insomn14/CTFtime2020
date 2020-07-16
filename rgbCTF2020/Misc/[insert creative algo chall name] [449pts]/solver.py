from itertools import permutations
from itertools import cycle

def check_arr(a1, a2):
	cond = []
	for cnt in range(len(a2)):
		if sorted(a1) != sorted(a2[cnt]):
			cond.append(True)
		else:
			cond.append(False)
	return all(cond)

def check(a1, a2):
	cond = []
	for i in a1:
		if i not in a2:
			cond.append(True)
		else:
			cond.append(False)
	return all(cond)

def main():
	x = int(input('x = '))
	n = int(input('n = '))
	print(f'All possible unique combinations for x = {x} and n = {n}:')

	found = [2**i for i in range(n)]
	total = sum(found)

	save = []
	for a in range(x):
		for first in permutations(found, x-a):
			tmp1 = sum(first)
			for b in range(x):
				for second in permutations(found, x-b):
					tmp2 = sum(second)
					if tmp2 != tmp1 and check(first, second):
						for c in range(x):
							for third in permutations(found, x-c):
								tmp3 = sum(third)
								if tmp3 != tmp1 and tmp3 != tmp2 and check(first, third) and check(second, third):
									for d in range(x):
										for four in permutations(found, x-d):
											tmp4 = sum(four)
											if tmp4 != tmp1 and tmp4 != tmp2 and tmp4 != tmp3 and check(first, four) and check(second, four) and check(third, four):
												res, arr = sum([tmp1, tmp2, tmp3, tmp4]), [tmp1, tmp2, tmp3, tmp4]
												if res == total and check_arr(arr, save):
													save.append(arr)
													print(f'{tmp1}  {tmp2}  {tmp3} {tmp4} = {res}')

	print(f'Final Output:\n{len(save)}')
	print(f'(There are {len(save)} combinations generated above)')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()