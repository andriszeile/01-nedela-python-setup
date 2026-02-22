'''
Spēles loģika minēšanas spēlei.
'''
import random


def generate_secret(low=1, high=100):
    '''
    Ģenerē slepenu nejaušu veselu skaitli intervālā [low; high].

    Args:
        low: apakšējā robeža (noklusējums 1)
        high: augšējā robeža (noklusējums 100)

    Returns:
        int: slepenais skaitlis

    Raise:
        TypeError: low un high jābūt int
        ValueError: low nedrīkst būt lielāks par high

    Example:
        >>> s = generate_secret(1, 5)
        >>> s
        3
    '''
    if not isinstance(low, int) or not isinstance(high, int):
        raise TypeError('low un high jābūt int')
    if low > high:
        raise ValueError('low nedrīkst būt lielāks par high')
    return random.randint(low, high)


def check_guess(guess, secret):
    '''
    Salīdzina minējumu ar slepeno skaitli.

    Args:
        guess: spēlētāja minējums (int)
        secret: slepenais skaitlis (int)

    Returns:
        str: "correct", "too_high" vai "too_low"

    Raise:
        TypeError: guess un secret jābūt int

    Example:
        >>> check_guess(5, 5)
        'correct'
        >>> check_guess(6, 5)
        'too_high'
        >>> check_guess(4, 5)
        'too_low'
    '''
    if not isinstance(guess, int) or not isinstance(secret, int):
        raise TypeError('guess un secret jābūt int')

    if guess == secret:
        return 'correct'
    if guess > secret:
        return 'too_high'
    return 'too_low'


def is_game_over(attempts, max_attempts=10):
    '''
    Nosaka, vai spēle (raunds) ir beigusies pēc mēģinājumu skaita.

    Args:
        attempts: jau izmantoto mēģinājumu skaits (int)
        max_attempts: maksimālais mēģinājumu skaits (noklusējums 10)

    Returns:
        bool: True, ja mēģinājumi beigušies; citādi False

    Raise:
        TypeError: attempts un max_attempts jābūt int
        ValueError: attempts nedrīkst būt negatīvs
        ValueError: max_attempts jābūt > 0

    Example:
        >>> is_game_over(0, 10)
        False
        >>> is_game_over(10, 10)
        True
    '''
    if not isinstance(attempts, int) or not isinstance(max_attempts, int):
        raise TypeError('attempts un max_attempts jābūt int')
    if attempts < 0:
        raise ValueError('attempts nedrīkst būt negatīvs')
    if max_attempts <= 0:
        raise ValueError('max_attempts jābūt > 0')

    return attempts >= max_attempts


if __name__ == '__main__':
    # f-ciju testi
    print('generate_secret(1, 5):', generate_secret(1, 5))
    print('check_guess(4, 5):', check_guess(4, 5))
    print('check_guess(5, 5):', check_guess(5, 5))
    print('check_guess(6, 5):', check_guess(6, 5))
    print('is_game_over(9, 10):', is_game_over(9, 10))
    print('is_game_over(10, 10):', is_game_over(10, 10))