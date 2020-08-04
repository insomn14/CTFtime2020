import os
from z3 import *
from pwn import *
from subprocess import Popen, PIPE, STDOUT

# Solving sections
def bin_solving(data1, data2):
	s = Solver()
	a1 = [BitVec('a1_%d'%i, 8) for i in range(14)]
	s.add( (a1[4] ^ a1[0] ^ a1[2]) == data1[0] )
	s.add( (a1[4] ^ a1[2] ^ a1[6]) == data1[1] )
	s.add( (a1[6] ^ a1[4] ^ a1[8]) == data1[2] )
	s.add( (a1[8] ^ a1[6] ^ a1[10]) == data1[3] )
	s.add( (a1[10] ^ a1[8] ^ a1[12]) == data1[4] )
	s.add( (a1[12] ^ a1[10] ^ a1[1]) == data1[5] )
	s.add( (a1[1] ^ a1[12] ^ a1[3]) == data1[6] )
	s.add( (a1[3] ^ a1[1] ^ a1[5]) == data1[7] )
	s.add( (a1[5] ^ a1[3] ^ a1[7]) == data1[8] )
	s.add( (a1[7] ^ a1[5] ^ a1[9]) == data1[9] )
	s.add( (a1[9] ^ a1[7] ^ a1[11]) == data1[10] )
	s.add( (a1[11] ^ a1[9] ^ a1[13]) == data1[11] )
	s.add( (a1[13] ^ a1[11] ^ a1[0]) == data1[12] )
	s.add( (a1[0] ^ a1[13] ^ a1[2]) == data1[13] )
	s.add( (a1[1] ^ a1[0] ^ a1[2]) == data2[0] )
	s.add( (a1[2] ^ a1[1] ^ a1[3]) == data2[1] )
	s.add( (a1[3] ^ a1[2] ^ a1[4]) == data2[2] )
	s.add( (a1[4] ^ a1[3] ^ a1[5]) == data2[3] )
	s.add( (a1[5] ^ a1[4] ^ a1[6]) == data2[4] )
	s.add( (a1[6] ^ a1[5] ^ a1[7]) == data2[5] )
	s.add( (a1[7] ^ a1[6] ^ a1[8]) == data2[6] )
	s.add( (a1[8] ^ a1[7] ^ a1[9]) == data2[7] )
	s.add( (a1[9] ^ a1[8] ^ a1[10]) == data2[8] )
	s.add( (a1[10] ^ a1[9] ^ a1[11]) == data2[9] )
	s.add( (a1[11] ^ a1[10] ^ a1[12]) == data2[10] )
	s.add( (a1[12] ^ a1[11] ^ a1[13]) == data2[11] )
	s.add( (a1[13] ^ a1[12] ^ a1[0]) == data2[12] )
	s.add( (a1[0] ^ a1[13] ^ a1[1]) == data2[13] )
	if (s.check() == sat):
	  model = s.model()
	  res = ''.join(chr(int(str(model[a1[i]]))) for i in range(14))
	  return res
	else:
	  return 0

def arm_solving(data1, data2):
	s = Solver()
	a1 = [BitVec('a1_%d'%i, 8) for i in range(14)]
	s.add( (a1[2] ^ a1[4] ^ a1[0]) == data1[0] )
	s.add( (a1[6] ^ a1[4] ^ a1[2]) == data1[1] )
	s.add( (a1[8] ^ a1[6] ^ a1[4]) == data1[2] )
	s.add( (a1[10] ^ a1[8] ^ a1[6]) == data1[3] )
	s.add( (a1[12] ^ a1[10] ^ a1[8]) == data1[4] )
	s.add( (a1[1] ^ a1[12] ^ a1[10]) == data1[5] )
	s.add( (a1[3] ^ a1[1] ^ a1[12]) == data1[6] )
	s.add( (a1[5] ^ a1[3] ^ a1[1]) == data1[7] )
	s.add( (a1[7] ^ a1[5] ^ a1[3]) == data1[8] )
	s.add( (a1[9] ^ a1[7] ^ a1[5]) == data1[9] )
	s.add( (a1[11] ^ a1[9] ^ a1[7]) == data1[10] )
	s.add( (a1[13] ^ a1[11] ^ a1[9]) == data1[11] )
	s.add( (a1[0] ^ a1[13] ^ a1[11]) == data1[12] )
	s.add( (a1[2] ^ a1[0] ^ a1[13]) == data1[13] )
	s.add( (a1[2] ^ a1[1] ^ a1[0]) == data2[0] )
	s.add( (a1[3] ^ a1[2] ^ a1[1]) == data2[1] )
	s.add( (a1[4] ^ a1[3] ^ a1[2]) == data2[2] )
	s.add( (a1[5] ^ a1[4] ^ a1[3]) == data2[3] )
	s.add( (a1[6] ^ a1[5] ^ a1[4]) == data2[4] )
	s.add( (a1[7] ^ a1[6] ^ a1[5]) == data2[5] )
	s.add( (a1[8] ^ a1[7] ^ a1[6]) == data2[6] )
	s.add( (a1[9] ^ a1[8] ^ a1[7]) == data2[7] )
	s.add( (a1[10] ^ a1[9] ^ a1[8]) == data2[8] )
	s.add( (a1[11] ^ a1[10] ^ a1[9]) == data2[9] )
	s.add( (a1[12] ^ a1[11] ^ a1[10]) == data2[10] )
	s.add( (a1[13] ^ a1[12] ^ a1[11]) == data2[11] )
	s.add( (a1[0] ^ a1[13] ^ a1[12]) == data2[12] )
	s.add( (a1[1] ^ a1[0] ^ a1[13]) == data2[13] )
	if (s.check() == sat):
		model = s.model()
		res = ''.join(chr(int(str(model[a1[i]]))) for i in range(14))
		return res
	else:
		return 0

def aarch64_solving(data1, data2):
	s = Solver()
	a1 = [BitVec('a1_%d'%i, 8) for i in range(14)]
	s.add( (((a1[0] ^ a1[4]) & 0xFF ^ a1[2]) & 0xFF) == data1[0] )
	s.add( (((a1[2] ^ a1[4]) & 0xFF ^ a1[6]) & 0xFF) == data1[1] )
	s.add( (((a1[4] ^ a1[6]) & 0xFF ^ a1[8]) & 0xFF) == data1[2] )
	s.add( (((a1[6] ^ a1[8]) & 0xFF ^ a1[10]) & 0xFF) == data1[3] )
	s.add( (((a1[8] ^ a1[10]) & 0xFF ^ a1[12]) & 0xFF) == data1[4] )
	s.add( (((a1[10] ^ a1[12]) & 0xFF ^ a1[1]) & 0xFF) == data1[5] )
	s.add( (((a1[12] ^ a1[1]) & 0xFF ^ a1[3]) & 0xFF) == data1[6] )
	s.add( (((a1[1] ^ a1[3]) & 0xFF ^ a1[5]) & 0xFF) == data1[7] )
	s.add( (((a1[3] ^ a1[5]) & 0xFF ^ a1[7]) & 0xFF) == data1[8] )
	s.add( (((a1[5] ^ a1[7]) & 0xFF ^ a1[9]) & 0xFF) == data1[9] )
	s.add( (((a1[7] ^ a1[9]) & 0xFF ^ a1[11]) & 0xFF) == data1[10] )
	s.add( (((a1[9] ^ a1[11]) & 0xFF ^ a1[13]) & 0xFF) == data1[11] )
	s.add( (((a1[11] ^ a1[13]) & 0xFF ^ a1[0]) & 0xFF) == data1[12] )
	s.add( (((a1[13] ^ a1[0]) & 0xFF ^ a1[2]) & 0xFF) == data1[13] )
	s.add( (((a1[0] ^ a1[1]) & 0xFF ^ a1[2]) & 0xFF) == data2[0] )
	s.add( (((a1[1] ^ a1[2]) & 0xFF ^ a1[3]) & 0xFF) == data2[1] )
	s.add( (((a1[2] ^ a1[3]) & 0xFF ^ a1[4]) & 0xFF) == data2[2] )
	s.add( (((a1[3] ^ a1[4]) & 0xFF ^ a1[5]) & 0xFF) == data2[3] )
	s.add( (((a1[4] ^ a1[5]) & 0xFF ^ a1[6]) & 0xFF) == data2[4] )
	s.add( (((a1[5] ^ a1[6]) & 0xFF ^ a1[7]) & 0xFF) == data2[5] )
	s.add( (((a1[6] ^ a1[7]) & 0xFF ^ a1[8]) & 0xFF) == data2[6] )
	s.add( (((a1[7] ^ a1[8]) & 0xFF ^ a1[9]) & 0xFF) == data2[7] )
	s.add( (((a1[8] ^ a1[9]) & 0xFF ^ a1[10]) & 0xFF) == data2[8] )
	s.add( (((a1[9] ^ a1[10]) & 0xFF ^ a1[11]) & 0xFF) == data2[9] )
	s.add( (((a1[10] ^ a1[11]) & 0xFF ^ a1[12]) & 0xFF) == data2[10] )
	s.add( (((a1[11] ^ a1[12]) & 0xFF ^ a1[13]) & 0xFF) == data2[11] )
	s.add( (((a1[12] ^ a1[13]) & 0xFF ^ a1[0]) & 0xFF) == data2[12] )
	s.add( (((a1[13] ^ a1[0]) & 0xFF ^ a1[1]) & 0xFF) == data2[13] )
	if (s.check() == sat):
		model = s.model()
		res = ''.join(chr(int(str(model[a1[i]]))) for i in range(14))
		return res
	else:
		return 0

def powerpc64_solving(data1, data2):
	s = Solver()
	a1 = [BitVec('a1_%d'%i, 8) for i in range(14)]
	s.add((a1[0] ^ a1[4] ^ a1[2]) == data1[0])
	s.add((a1[2] ^ a1[4] ^ a1[6]) == data1[1])
	s.add((a1[4] ^ a1[6] ^ a1[8]) == data1[2])
	s.add((a1[6] ^ a1[8] ^ a1[10]) == data1[3])
	s.add((a1[8] ^ a1[10] ^ a1[0xc]) == data1[4])
	s.add((a1[10] ^ a1[0xc] ^ a1[1]) == data1[5])
	s.add((a1[0xc] ^ a1[1] ^ a1[3]) == data1[6])
	s.add((a1[1] ^ a1[3] ^ a1[5]) == data1[7])
	s.add((a1[3] ^ a1[5] ^ a1[7]) == data1[8])
	s.add((a1[5] ^ a1[7] ^ a1[9]) == data1[9])
	s.add((a1[7] ^ a1[9] ^ a1[0xb]) == data1[10])
	s.add((a1[9] ^ a1[0xb] ^ a1[0xd]) == data1[11])
	s.add((a1[0xb] ^ a1[0xd] ^ a1[0]) == data1[12])
	s.add((a1[0xd] ^ a1[0] ^ a1[2]) == data1[13])
	s.add((a1[0] ^ a1[1] ^ a1[2]) == data2[0])
	s.add((a1[1] ^ a1[2] ^ a1[3]) == data2[1])
	s.add((a1[2] ^ a1[3] ^ a1[4]) == data2[2])
	s.add((a1[3] ^ a1[4] ^ a1[5]) == data2[3])
	s.add((a1[4] ^ a1[5] ^ a1[6]) == data2[4])
	s.add((a1[5] ^ a1[6] ^ a1[7]) == data2[5])
	s.add((a1[6] ^ a1[7] ^ a1[8]) == data2[6])
	s.add((a1[7] ^ a1[8] ^ a1[9]) == data2[7])
	s.add((a1[8] ^ a1[9] ^ a1[10]) == data2[8])
	s.add((a1[9] ^ a1[10] ^ a1[0xb]) == data2[9])
	s.add((a1[10] ^ a1[0xb] ^ a1[0xc]) == data2[10])
	s.add((a1[0xb] ^ a1[0xc] ^ a1[0xd]) == data2[11])
	s.add((a1[0xc] ^ a1[0xd] ^ a1[0]) == data2[12])
	s.add((a1[0xd] ^ a1[0] ^ a1[1]) == data2[13])
	if (s.check() == sat):
		model = s.model()
		res = ''.join(chr(int(str(model[a1[i]]))) for i in range(14))
		return res
	else:
		return 0

# scrap array
def powerpc64(exe):
	data1 = [int(exe.read(0x010020130+i*4,4).hex(), 16) for i in range(14)]
	data2 = [int(exe.read(0x010020168+i*4,4).hex(), 16) for i in range(14)]
	ans = powerpc64_solving(data1, data2)
	return ans

def arm_arm(exe):
	data1 = [int(exe.read(0x011008+i*4,1).hex(), 16) for i in range(14)]
	data2 = [int(exe.read(0x011040+i*4,1).hex(), 16) for i in range(14)]
	ans = arm_solving(data1, data2)
	return ans

def arm_x64(exe):
	data1 = [int(exe.read(0x012010+i*4,1).hex(), 16) for i in range(14)]
	data2 = [int(exe.read(0x012048+i*4,1).hex(), 16) for i in range(14)]
	ans = aarch64_solving(data1, data2)
	return ans

def bin_x86(exe):
	data1 = [int(exe.read(0x03020+i*4,1).hex(),16) for i in range(14)]
	data2 = [int(exe.read(0x03060+i*4,1).hex(), 16) for i in range(14)]
	ans = bin_solving(data1, data2)
	return ans

def bin_x64(exe):
	data1 = [int(exe.read(0x0202020+i*4,1).hex(),16) for i in range(14)]
	data2 = [int(exe.read(0x0202060+i*4,1).hex(), 16) for i in range(14)]
	ans = bin_solving(data1, data2)
	return ans

def compile(a1, a2, a3):
	args1 = 'bzip2 -vfd '
	args2 = 'chmod +x '
	command1 = args1 + a1
	command2 = args2 + a2
	os.system(command1+';'+command2)
	
def execute(fname, key):
	p = Popen(['./'+fname], stdout=PIPE, stdin=PIPE, stderr=PIPE)
	stdout_data = p.communicate(input=key.encode())[0]
	log.info(stdout_data)

keys = []
zipfile = 'surprise'
binfile = 'surprise.out'
newbin = 'binary'
arc = ['amd64', 'i386', 'aarch64', 'arm', 'powerpc64']

try:
	while True:
		compile(zipfile, binfile, newbin)
		exe = ELF(binfile)
		typ = exe.arch

		if typ in arc:
			log.info(f'Arch : {typ} Found')
			if typ == arc[0]:
				key = bin_x64(exe)
			elif typ == arc[1]:
				key = bin_x86(exe)
			elif typ == arc[2]:
				cmd = 'sudo ln -sf /usr/aarch64-linux-gnu/lib/libc.so.6  /lib/libc.so.6'
				os.system(cmd)
				key = arm_x64(exe)
			elif typ == arc[3]:
				cmd = 'sudo ln -sf /usr/arm-linux-gnueabihf/lib/libc.so.6  /lib/libc.so.6'
				os.system(cmd)
				key = arm_arm(exe)
			elif typ == arc[4]:
				cmd = 'sudo ln -sf /usr/powerpc64-linux-gnu/lib/libc.so.6  /lib/libc.so.6'
				os.system(cmd)
				key = powerpc64(exe)
			execute(binfile, key)
		else:
			log.info(f'Arch : {typ} not detect')
except pwnlib.exception.PwnlibException:
	os.system('./'+binfile)
except Exception as err:
	print(keys)
	print(err)