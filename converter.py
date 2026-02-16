#konstantes
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR =0.84235020

#izvēlne
print('Vienību konvertors')
print('Izvēlies kategoriju:')
print('1 - km <-> mi')
print('2 - kg <-> lb')
print('3 - l <-> gal')
print('4 - USD <-> EUR')
#konversijas izvēle
choise = input('Tava izvēle (1-4): ')

if choise == '1':
    #virziena izvēle
    print('Virziens:')
    print('1 - km -> mi')
    print('2 - mi -> km')
    direction = input('> ')

    if direction == '1':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value * KM_TO_MI
        print(f'{value:.2f} km = {result:.2f} mi')
    elif direction == '2':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value / KM_TO_MI
        print(f'{value:.2f} mi = {result:.2f} km')
    else: #nepareiza virziena izvade
        print('Kļūda, virziena vērtība 1 vai 2')

elif choise == '2':
    #virziena izvēle
    print('Virziens:')
    print('1 - kg -> lb')
    print('2 - lb -> kg')
    direction = input('> ')

    if direction == '1':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value * KG_TO_LB
        print(f'{value:.2f} kg = {result:.2f} lb')
    elif direction == '2':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value / KG_TO_LB
        print(f'{value:.2f} lb = {result:.2f} kg')
    else: #nepareiza virziena izvade
        print('Kļūda, virziena vērtība 1 vai 2')

elif choise == '3':
    #virziena izvēle
    print('Virziens:')
    print('1 - l -> gal')
    print('2 - gal -> l')
    direction = input('> ')
    
    if direction == '1':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value * L_TO_GAL
        print(f'{value:.2f} l = {result:.2f} gal')
    elif direction == '2':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value / L_TO_GAL
        print(f'{value:.2f} gal = {result:.2f} l')
    else: #nepareiza virziena izvade
        print('Kļūda, virziena vērtība 1 vai 2')

elif choise == '4':
    #virziena izvēle
    print('Virziens:')
    print('1 - USD -> EUR')
    print('2 - EUR -> USDl')
    direction = input('> ')
    #nepareizas ievadītās vērtības pārbaude

    if direction == '1':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value * USD_TO_EUR
        print(f'{value:.2f} USD = {result:.2f} EUR')
    elif direction == '2':
        #nepareizas ievadītās vērtības pārbaude
        try:
            value = float(input('Ievadi vērtību: '))
        except:
            print('Kļūda, jāievada skaitlis!')
            exit()
        result = value / USD_TO_EUR
        print(f'{value:.2f} EUR = {result:.2f} USD')
    else: #nepareiza virziena izvade
        print('Kļūda, virziena vērtība 1 vai 2')

else:
    print('Kļūda, konversijas izvēle 1-4!')
    

    
