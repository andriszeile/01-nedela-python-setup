print('A daļa - Saraksti')
#izveido jaunu sarakstu [], list() ar 9 elementiem
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Izveidots saraksts:')
print(numbers)
#pievieno elementu 
numbers.append(10)
print('Sarakstam beigās pievienots 10:')
print(numbers)
#dzēš saraksta pēdējo elementu un atgriež mainīgajam
removed = numbers.pop()
print('Sarakstam dzēš pēdējo elementu un atgriež mainīgajam:')
print(numbers)
print(f'Nodzēstais elements: {removed}')
#pievieno nodzēsto elementu atpakaļ
numbers.append(removed)
print('Sarakstam beigās pievieno nodzēsto elementu kā mainīgo:')
print(numbers)
#atrodam sarakstā elementa 3 indeksu
indekss = numbers.index(3)
print(f'Saraksts elementa 3 indeksa vērtība {indekss}')
#aiz elementa 3 ievietojam elementu 10
print('Aiz saraksta 3 ievietojam elementu 10')
numbers.insert(indekss + 1, 10)
print(numbers)
#dzēšam ievietoto elementu 10
print('Dzēšam sarakstā pirmo sastapto elementu 10')
numbers.remove(10)
#numbers.pop(indekss + 1) var arī pēc elementa indeksa nodzēst
print(numbers)

#saraksta elementu summa un vidējais bez sum() un len() izmantošanas
total = 0
count = 0
for el in numbers:
    total += el
    count += 1
average = total / count
print(f'Summa: {total}, Vidējais: {average:.2f}')

#pāra skaitļu filtrēšana
even_numbers = list()
for el in numbers:
    if el % 2 == 0:
        even_numbers.append(el)
print(f'Pāra skaitļi: {even_numbers}')

#šķēlumi [start:stop:step] - indeksiem
frist_three = numbers[:3]
last_two = numbers[-2:]
every_second = numbers[::2]
print(f'Pirmie 3 saraksta elementi: {frist_three}')
print(f'Pēdējie 2 saraksta elementi: {last_two}')
print(f'Katrs 2. saraksta elements: {every_second}')


print('\nB daļa - Vārdnīcas')
#izveido vārdnīcu
students = {
    'Juris': 89,
    'Aigars': 73,
    'Inese': 97
}

#pievieno jaunu studentu
students['Jānis'] = 87

#maina studenta atzīmi
students['Aigars'] = 79

#izvada visus studentus sadalot pa pāriem (atslēga, vērtība)
for name, grade in students.items():
    print(f'{name}: {grade}')

#atrod labāko studentu
best_name = ''
best_grade = -1 #
for name, grade in students.items():
    if grade > best_grade:
        best_grade = grade
        best_name = name
print(f'Labākais students: {best_name} ar {best_grade} ballēm.')


print('\nC daļa - Kombinācija')
print('Studenti ar atzīmi >= 80')
#saraksts ar vārdnīcām
student_list = [
    {'name': 'Juris', 'grade': 89},
    {'name': 'Aigars', 'grade': 79},
    {'name': 'Inese', 'grade': 97},
    {'name': 'Jānis', 'grade': 87},
    {'name': 'Olga', 'grade': 94}
]

#izvelk vārdus un atzīmes, ja atzīme >=80
#atsevišķos sarakstos lai ar zip() var;ētu tos apvienot
names = []
grades = []
for el in student_list:
    if el['grade'] >= 80:
        names.append(el['name'])
        grades.append(el['grade'])
#parāda izveidotos sarakstus
print(names)
print(grades)
#izmantojot dubulto izpakošanu
#apvieno sarakstus ar zip() un numurē ar enumerate()
for i, (name, grade) in enumerate(zip(names, grades), start = 1):
    print(f'{i}. {name} - {grade}')

