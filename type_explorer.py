print('1) Pamata tipi + type()')

s1 = '5'
s2 = 'Labdien'
i1 = 5
i2 = 0
f1 = 3.14
f2 = 0.0
b1 = True
b2 = False
n1 = None
n2 = None

values = [s1, s2, i1, i2, f1, f2, b1, b2, n1, n2]
for i in values:
    print(f"\Vērtība {i!r:>10} --> {type(i)}")