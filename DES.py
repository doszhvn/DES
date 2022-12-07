import numpy as np
import hashlib

x = (input('Введите слово='))

encoded = x.encode()
result = hashlib.sha256(encoded)


def text_to_bits(text, encoding='utf-8' + ' ', errors='surrogatepass'):
  bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
  return bits.zfill(8 * ((len(bits) + 7) // 8))


y = text_to_bits(x)
print(y)

masy = list(y)



def inser(mmm):
  py = 64 - len(x) * 8
  for i in range(py):
    mmm.insert(0, 0)



inser(masy)

print("First iteration: ")
print(masy)

masss = masy

masss[0] = masy[58 - 1]
masss[1] = masy[50 - 1]
masss[2] = masy[42 - 1]
masss[3] = masy[34 - 1]
masss[4] = masy[26 - 1]
masss[5] = masy[18 - 1]
masss[6] = masy[10 - 1]
masss[7] = masy[2 - 1]
masss[8] = masy[60 - 1]
masss[9] = masy[52 - 1]
masss[10] = masy[44 - 1]
masss[11] = masy[36 - 1]
masss[12] = masy[28 - 1]
masss[13] = masy[20 - 1]
masss[14] = masy[12 - 1]
masss[15] = masy[4 - 1]
masss[16] = masy[62 - 1]
masss[17] = masy[54 - 1]
masss[18] = masy[46 - 1]
masss[19] = masy[38 - 1]
masss[20] = masy[30 - 1]
masss[21] = masy[22 - 1]
masss[22] = masy[14 - 1]
masss[23] = masy[6 - 1]
masss[24] = masy[64 - 1]
masss[25] = masy[56 - 1]
masss[26] = masy[48 - 1]
masss[27] = masy[40 - 1]
masss[28] = masy[32 - 1]
masss[29] = masy[24 - 1]
masss[30] = masy[16 - 1]
masss[31] = masy[8 - 1]
masss[32] = masy[57 - 1]
masss[33] = masy[49 - 1]
masss[34] = masy[41 - 1]
masss[35] = masy[33 - 1]
masss[36] = masy[25 - 1]
masss[37] = masy[17 - 1]
masss[38] = masy[9 - 1]
masss[39] = masy[1 - 1]
masss[40] = masy[59 - 1]
masss[41] = masy[51 - 1]
masss[42] = masy[43 - 1]
masss[43] = masy[35 - 1]
masss[44] = masy[27 - 1]
masss[45] = masy[19 - 1]
masss[45] = masy[11 - 1]
masss[47] = masy[3 - 1]
masss[48] = masy[61 - 1]
masss[49] = masy[53 - 1]
masss[50] = masy[45 - 1]
masss[51] = masy[37 - 1]
masss[52] = masy[29 - 1]
masss[53] = masy[21 - 1]
masss[54] = masy[13 - 1]
masss[55] = masy[5 - 1]
masss[56] = masy[63 - 1]
masss[57] = masy[55 - 1]
masss[58] = masy[47 - 1]
masss[59] = masy[39 - 1]
masss[60] = masy[31 - 1]
masss[61] = masy[23 - 1]
masss[62] = masy[15 - 1]
masss[63] = masy[7 - 1]

print("First permutation: ")
print(masss)
masyu = list(masss)

length = len(masyu)

middle_index = length // 2

first_half = masyu[:middle_index]
second_half = masyu[middle_index:]

print("Division into two:")
print(first_half)
print(second_half)
a = (input('Введите ключ='))

msasy = list(text_to_bits(a))

inser(msasy)
mass = msasy
print(msasy)

mass[0] = msasy[58 - 1 - 1]
mass[1] = msasy[50 - 1 - 1]
mass[2] = msasy[42 - 1 - 1]
mass[3] = msasy[34 - 1 - 1]
mass[4] = msasy[26 - 1 - 1]
mass[5] = msasy[18 - 1 - 1]
mass[6] = msasy[10 - 1 - 1]
mass[7] = msasy[2 - 1 - 1]
mass[8] = msasy[60 - 1 - 1 - 1]
mass[9] = msasy[52 - 1 - 1 - 1]
mass[10] = msasy[44 - 1 - 1 - 1]
mass[11] = msasy[36 - 1 - 1 - 1]
mass[12] = msasy[28 - 1 - 1 - 1]
mass[13] = msasy[20 - 1 - 1 - 1]
mass[14] = msasy[12 - 1 - 1 - 1]
mass[15] = msasy[4 - 1 - 1 - 1]
mass[16] = msasy[62 - 1 - 1 - 1 - 1]
mass[17] = msasy[54 - 1 - 1 - 1 - 1]
mass[18] = msasy[46 - 1 - 1 - 1 - 1]
mass[19] = msasy[38 - 1 - 1 - 1 - 1]
mass[20] = msasy[30 - 1 - 1 - 1 - 1]
mass[21] = msasy[22 - 1 - 1 - 1 - 1]
mass[22] = msasy[14 - 1 - 1 - 1 - 1]
mass[23] = msasy[6 - 1 - 1 - 1 - 1]
mass[24] = msasy[64 - 1 - 1 - 1 - 1 - 1]
mass[25] = msasy[56 - 1 - 1 - 1 - 1 - 1]
mass[26] = msasy[48 - 1 - 1 - 1 - 1 - 1]
masss[27] = msasy[40 - 1 - 1 - 1 - 1 - 1]
mass[28] = msasy[63 - 1]
mass[29] = msasy[55 - 1]
mass[30] = msasy[47 - 1]
mass[31] = msasy[39 - 1]
mass[32] = msasy[31 - 1]
mass[33] = msasy[23 - 1]
mass[34] = msasy[15 - 1]
mass[35] = msasy[7 - 1]
mass[36] = msasy[62 - 1]
mass[37] = msasy[54 - 1]
mass[38] = msasy[46 - 1]
mass[39] = msasy[38 - 1]
mass[40] = msasy[30 - 1]
mass[41] = msasy[22 - 1]
mass[42] = msasy[14 - 1]
mass[43] = msasy[6 - 1]
mass[44] = msasy[61 - 1]
mass[45] = msasy[53 - 1]
mass[45] = msasy[45 - 1]
mass[47] = msasy[37 - 1]
mass[48] = msasy[29 - 1]
mass[49] = msasy[21 - 1]
mass[50] = msasy[13 - 1]
mass[51] = msasy[5 - 1]
mass[52] = msasy[28 - 1]
mass[53] = msasy[20 - 1]
mass[54] = msasy[12 - 1]
mass[55] = msasy[4 - 1]


l0 = first_half

for i in range(0, 31):
  l0[i] = first_half[i + 1]
l0[31] = first_half[0]

print("Shift by one:")

print(l0)

r0 = second_half

for i in range(0, 31):
  r0[i] = second_half[i + 1]
r0[31] = second_half[0]

print(r0)
