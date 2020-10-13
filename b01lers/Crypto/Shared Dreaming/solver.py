from pwn import xor

a1_a2_a3_a4 = 0x8ba4c4dfce33fd6101cf5c56997531c024a10f1dc323eb7fe3841ac389747fb90e3418f90011ef2610fa3636cd6cf0002d19faa30d39161fbd45cc58abff6a84
a2_a3_a4 = 0xf969375145322aba697ce9b4e00aa88e81ffe5c306b1b98148f33c4581b2ac39bc95f13b27c39f2311a590b7e27cdbdb7599f615acd70c45378e44fb319b8cb6
a1_a3 = 0x855249b385f7b1d9923f71feb3bdee1032963ab51aa7b9d89a20c08c381e77890aa8849702d8791f8e636e833928ba6ea44c5f261983b7e29bd82e44b77fe03b
flag_a3_RandByte = 0xf694bc3d12a0673aead8fc4fdf964f5ec0c1d938e722bf333000f300088ead0dec1e7e03720331098068c13a066ca9bca89850a8ee67feb8471af5f47b4c0f13

# Where RandByte[0] == RandByte[1] and len(RandByte) == len(flag)

c1 =  a1_a2_a3_a4 ^ a2_a3_a4
print(f"c1: {hex(c1)}")

c3 = c1 ^ a1_a3
print(f"c3: {hex(c3)}")

c2_c4 = c3 ^ a2_a3_a4
print(f"c2_c4: {hex(c2_c4)}")

flag_RandByte = c3 ^ flag_a3_RandByte
print(f"flag_RandByte: {hex(flag_RandByte)}")

