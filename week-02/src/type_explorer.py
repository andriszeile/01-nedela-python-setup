print('1) Pamata tipi + type()')
s1 = '3'
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
    #!r jeb repr() - tehniskais objekta pieraksts (str drukā ar pēdiņām)
    print(f"\Vērtība {i!r:>10} --> {type(i)}")

print('2) Virkņu savienošana')
print('5' + '3')        #'53' (str + str = apvienošana)
#print('5' + 3)         #TypeError, (str + int = TypeError, Python nav automātiskās konversijas) 
print(int('5') + 3)     #8 (tiešā konversija int('str') + int = saskaitīšana)
print('5' * 4)          #5555 (str * int) = str atkārtošana

print('3. Truthy/Falsy piemēri')
print('empty text:', bool(''))    #False, tukša virkne
print('empty text:', bool('a'))   #True, virkne ar saturu 
print('zero:', bool(0))           #False, jo 0 ir falsy
print('one:', bool(1))            #True, jo 1 ir truthy
print('None:', bool(None))        #False, jo None ir falsy

print('4. Datu tipu pārveides (explicit conversion)')
#str uz int
strtoint = '123'
print('str -> int:', strtoint, '->', int(strtoint))
#int uz float
inttofloat = 10
print('int -> float:', inttofloat, '->', float(inttofloat))
#float uz int (tiek atmesta decimāldaļa, citi domā ka noapaļo uz leju)
floattoint = 8.5
print('float -> int:', floattoint, '->', int(floattoint))

#str uz int
bstr = '3.14'
#print('str -> int:', bstr, '->', int(bstr)) - pa tiešo nesanāk, jo virkne esatur veselu sk.
print('str -> int:', bstr, '->', int(float(bstr))) #str -> float -> int
#robežgadījumi
try:
    result = int('abc')
    print(result)
except:
    print("Kļūda: 'abc' nevar pārveidot par int")

try:
    result = float(None)
    print(result)
except:
    print("Kļūda: None nevar pārveidot par float")

print('5. Jauktā aritmētika')
print(True * 5)         #5 (True==1, 1*5=5)
print(False * 0.5)      #0.0 (False==0, 0*0.5=0.0)
print(False / True)     #0.0 (0/1 vajadzētu būt 0, bet python dalīšanā dot float)

print('6. Interesantie gadījumi')
print(0.1 + 0.2 == 0.3) #False (sliktā kļūda), jo 0.1 un 0.2 nevar
                        #saglabāt binārajā sistēmā, sanāk bezgalīgs sk.
                        #0.1 patiesībā ir 0.10000000000000000555...
                        #0.2 patiesībā ir 0.20000000000000001110...
                        #Python 0.1 + 0.2 redz kā 0.30000000000000004 !=0.3
print(round(2.5))       #2 Python robežgadījumos izmanto noapaļošanu 
print(round(3.5))       #4 līdz tuvākajam pāra skailtim
print('Laikam beigas')