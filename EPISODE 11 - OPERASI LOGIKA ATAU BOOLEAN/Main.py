# OPERASI LOGIKA ATAU BOOLEAN

# not, or, and, xor

# NOT
print('====NOT====')
a = True
c = not a
print('data boolean =', a)
print('------------- NOT')
print('data c =', c)

# OR (Jika salah satu bernilai true, maka hasilnya adalah true)
print('====OR====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)


# XOR (jika duah buah nilai bernilai sama maka akan false, sebaliknya jika duah buah nilai berbeda maka hasilnya true)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)
