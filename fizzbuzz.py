import sys #imortē moduli, lai iegūtu komandrindas argumentu sarakstu
if len(sys.argv) < 2:
    print('Kļūda, nav norādīts skaitlis N!')
    exit()
try:
    N = int(sys.argv[1])
except ValueError:
    print('Kļūda, N jābūt veselam skaitlim!')
    exit()
if N <= 0:
    print('Kļūda, N jābūt pozitīvam skaitlim!')
    exit()

for i in range(1, N + 1):
    #tukša virkne, ja dalās, virknei pievieno atbilstošos vārdus
    text = ''
    if i % 3 == 0:
        text += 'Fizz'
    if i % 5 == 0:
        text += 'Buzz'
    if i % 7 == 0:
        text += 'Jazz'
    #veido izvades virkni, ja text tukša, drukā ciparu
    output = text if text != '' else f'{i}'

    print(f'{output}', end='')

    if i < N:
        print(', ', end='')
