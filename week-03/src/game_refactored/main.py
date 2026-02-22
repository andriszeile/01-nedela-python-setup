'''
Minēšanas spēles galvenā daļa.
'''

from game_logic import generate_secret, check_guess, is_game_over
from ui import get_player_guess, show_hint, show_game_over, ask_play_again

def play_round():
    '''Spēles raunda palaišana.'''
    secret = generate_secret()
    attempts = 0

    print('Spēle uzmini skatili!')
    print('Esmu iedomājies skatili no 1 līdz 100.')
    print('Tev ir 10 mēģinājumi to uzminēt!')

    while not is_game_over(attempts):
        guess = get_player_guess()
        if guess is None:
            continue
        attempts += 1
        result = check_guess(guess, secret)
        if result == 'correct':
            show_game_over(secret, attempts, won=True)
            return
        show_hint(result)
    show_game_over(secret, attempts, won=False)

if __name__ == '__main__':
    while True:
        play_round()
        if not ask_play_again():
            print('Paldies par spēli!')
            break