print('Atbilstības pārbaudītājs')

#vecuma ievade ar pārbaudi
try:
    age = int(input('Ievadi vecumu: '))
except ValueError:
    print('Kļūda, vecumam jābūt veselam skaitlim!')
    exit()
if age < 0:
    print('Kļūda, vecums nevar būt negatīvs.')
    exit()

#jā/nē ievade ar pārbaudi
license_input = input('Vai ir autovadītāja apliecība? (j/n): ').lower()
if license_input !='j' and license_input !='n':
    print('Kļūda, atblidē jāievada j vai n')
    exit()
has_license = license_input == 'j'
student_input = input('Vai ir students? (j/n): ').lower()
if student_input !='j' and student_input !='n':
    print('Kļūda, atblidē jāievada j vai n')
    exit()
has_student = student_input == 'j'
veteran_input = input('Vai ir veterāns? (j/n): ').lower()
if veteran_input !='j' and veteran_input !='n':
    print('Kļūda, atblidē jāievada j vai n')
    exit()
has_veteran = veteran_input == 'j'
is_student = student_input == 'j'
is_veteran = veteran_input == 'j'

#nosacījumi
can_vote = age >=18
can_rent = age >=21 and has_license
sen_discount = age >= 65 or is_veteran
stu_discount = 16 <= age <= 26 and is_student

#rezultati
print(f"{'Balsošana:':<20} {'Jā' if can_vote else 'Nē'}")
if can_rent:
    print(f"{'Auto īre:':<20} {'Jā'}")
else:
    if age < 21:
        print(f"{'Auto īre:':<20} {'Nē (par jaunu)'}")
    elif not has_license:
        print(f"{'Auto īre:':<20} {'Nē (nav apliecības)'}")
    else:
        print(f"{'Auto īre:':<20} {'Nē'}")
print(f"{'Senioru atlaide:':<20} {'Jā' if sen_discount else 'Nē'}")
print(f"{'Studentu atlaide:':<20} {'Jā' if stu_discount else 'Nē'}")