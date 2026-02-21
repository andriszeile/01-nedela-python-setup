import random #gadījuma skatļu modulis

print('Spēle uzmini skatili!')

#ārējais cikls iespējai spēlēt vēlreiz
while True:
    #iedomājas skaitli
    secret = random.randint(1,100)
    attempts = 0
    max_attempts = 10
    print('Esmu iedomājies skatili no 1 līdz 100.')
    print('Tev ir 10 mēģinājumi to uzminēt!')

    #minēšanas cikls
    while True:
        guess_input = input('Tavs minējums: ')
        #pārbauda vai ir skaitlis
        try:
            guess_validated = int(guess_input)
        except ValueError:
            print('Kļūda, jāievada vesels skaitlis!')
            continue
        attempts += 1
        #salīdzināšana
        if guess_validated < secret:
            print('Par mazu.')
        elif guess_validated > secret:
            print('Par lielu.')
        else:
            print(f'Apsveicu, uzminēji! Izmantoji {attempts} mēģinājumus.')
            break

        #beidz ja beidzās mēģinājumi
        # var == bet >= drošāk
        if attempts >= max_attempts:
            print(f'Mēģinājumi beidzās! Pareizā atbilde bija {secret}.')
            break

    #vai spēlēt vēlreiz
    again = input('Vai gribi spēlēt vēlreiz? (j/n): ').lower()
    if again != 'j':
        print('Paldies par spēli!')
        break