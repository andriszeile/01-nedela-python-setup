'''
Veselu skaitļu validācijas funkcija.
'''
def is_int(text):
    '''
    Pārbauda, vai text var pārvērst par veselu skaitli (int).

    Args:
        text: ievade kā virkne

    Returns:
        bool: True, ja var pārvērst par int; citādi False

    Example:
        >>> is_int('123')
        True
        >>> is_int('-5')
        True
        >>> is_int('12.3')
        False
        >>> is_int('abc')
        False
    '''
    if not isinstance(text, str):
        return False
    try:
        int(text)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    #f-cijas testi
    print('is_int tests:')
    print(is_int('123'), '-> True')
    print(is_int('-5'), '-> True')
    print(is_int('12.3'), '-> False')
    print(is_int('abc'), '-> False')
    print(is_int(''), '-> False')