'''
ievades/izvades funkcijas minēšanas spēlei.
'''

from validators import is_int


def get_player_guess():
    '''
    Pieprasa spēlētāja minējumu un validē ievadi.

    Returns:
        int | None: skaitlis, ja ievade derīga; None, ja nederīga
    '''
    guess_input = input('Tavs minējums: ')#.strip()

    if not is_int(guess_input):
        print('Kļūda, jāievada vesels skaitlis!')
        return None

    return int(guess_input)


def show_hint(result):
    '''
    Parāda padomu, balstoties uz ievadīto minējumu.

    Args:
        result: 'too_low' vai 'too_high'

    Returns:
        None
    '''
    if result == 'too_low':
        print('Par mazu.')
    elif result == 'too_high':
        print('Par lielu.')
    else:
        #ka kaut kas aizgāja greizi
        print('Nezināms rezultāts.')


def show_game_over(secret, attempts, won):
    '''
    Parāda spēles beigu ziņojumu.

    Args:
        secret: slepenais skaitlis (int)
        attempts: mēģinājumu skaits (int)
        won: vai uzvarēja (bool)

    Returns:
        None
    '''
    if won:
        print(f'Apsveicu, uzminēji! Izmantoji {attempts} mēģinājumus.')
    else:
        print(f'Mēģinājumi beidzās! Pareizā atbilde bija {secret}.')


def ask_play_again():
    '''
    Pajautā, vai spēlēt vēlreiz.

    Returns:
        bool: True, ja lietotājs ievada 'j'; citādi False
    '''
    again = input('Vai gribi spēlēt vēlreiz? (j/n): ').strip().lower()
    return again == 'j'


if __name__ == '__main__':
    #f-ciju testi
    print('UI tests: ievadi skaitli vai ko citu.')
    g = get_player_guess()
    print('Saņemts:', g)

    print('Minējuma tests:')
    show_hint('too_low')
    show_hint('too_high')

    print('Spēles beigu tests:')
    show_game_over(secret=42, attempts=3, won=True)
    show_game_over(secret=42, attempts=10, won=False)

    print('Vai gribi spēlēt vēlreiz tests:')
    print('Rezultāts:', ask_play_again())