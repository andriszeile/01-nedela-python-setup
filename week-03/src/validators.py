'''
e-pasta, tālr.nr., vecuma, drošas paroles un datuma validācijas bibliotēka.

Visas funkcijas atgriež bool (True/False) un neizmet kļūdas (tikai pārbaude).
'''

def is_email(text):
    '''
    Vienkārša e-pasta validācija: satur @ un . Ir tikai viens @,
    pirms @ ir vismaz 1 simbols, pēc @ ir vismaz 1 simbols,
    domēna daļā ir punkts un tas nav sākumā/beigās

    Args:
        text: e-pasta adrese kā virkne

    Returns:
        bool: True, ja izskatās pēc e-pasta; citādi False

    Example:
        >>> is_email('anna@inbox.lv')
        True
    '''
    if not isinstance(text, str):
        return False

    text = text.strip()
    if text.count('@') != 1:
        return False

    local, domain = text.split('@')
    if local == '' or domain == '':
        return False

    if '.' not in domain:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False

    return True


def is_phone_number(text):
    '''
    Pārbauda Latvijas telefona numuru formātā: '+371 XXXXXXXX' (8 cipari).
    Sākas ar '+371 '. pēc atstarpes ir 8 simboli, kas sākas ar 2, 6, 8 vai 9.

    Args:
        text: telefona numurs kā virkne

    Returns:
        bool: True, ja atbilst formātam; citādi False

    Example:
        >>> is_phone_number('+371 26123456')
        True
    '''
    if not isinstance(text, str):
        return False

    text = text.strip()
    prefix = '+371 '
    if not text.startswith(prefix):
        return False

    rest = text[len(prefix):]
    if len(rest) != 8:
        return False
    if not rest.isdigit():
        return False
    if rest[0] not in ('2', '6', '8', '9'):
        return False

    return True


def is_valid_age(age):
    '''
    Pārbauda vecumu: vesels skaitlis no 0 līdz 150 (ieskaitot).

    Args:
        age: vecums (parasti int)

    Returns:
        bool: True, ja vecums korekts; citādi False

    Example:
        >>> is_valid_age(18)
        True
    '''
    if not isinstance(age, int):
        return False
    return 0 <= age <= 150


def is_strong_password(text):
    '''
    Pārbauda, vai parole atbilst sekojošiem kritērijiem -
    vismaz 8 simboli, satur vismaz 1 burtu un vismaz 1 ciparu.

    Args:
        text: parole kā virkne

    Returns:
        bool: True, ja parole atbilst; citādi False

    Example:
        >>> is_strong_password('abc12345')
        True
    '''
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = any(ch.isalpha() for ch in text)
    has_digit = any(ch.isdigit() for ch in text)

    return has_letter and has_digit


def is_valid_date(text):
    '''
    Pārbauda datumu YYYY-MM-DD formātā (pamata pārbaude ar mēnešu/dienu robežām).

    Args:
        text: datums kā virkne (YYYY-MM-DD)

    Returns:
        bool: True, ja datums izskatās korekts; citādi False

    Example:
        >>> is_valid_date('2026-02-21')
        True
    '''
    if not isinstance(text, str):
        return False

    text = text.strip()
    parts = text.split('-')
    if len(parts) != 3:
        return False

    y, m, d = parts
    if len(y) != 4 or len(m) != 2 or len(d) != 2:
        return False
    if not (y.isdigit() and m.isdigit() and d.isdigit()):
        return False

    year = int(y)
    month = int(m)
    day = int(d)

    if month < 1 or month > 12:
        return False

    # dienu skaits mēnesī
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        # februāris + garais gads
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap else 28

    return 1 <= day <= max_day


if __name__ == '__main__':

    print('is_email tests:')
    print(is_email('anna@inbox.lv'))
    print(is_email('anna'))
    print(is_email('anna@'))
    print(is_email('@inbox.lv'))
    print()
    print('is_phone_number tests:')
    print(is_phone_number('+371 26123456'))
    print(is_phone_number('26123456'))
    print(is_phone_number('+37126123456'))
    print(is_phone_number('+371 92345678'))
    print(is_phone_number('+371 32345678'))
    print()
    print('is_valid_age tests:')
    print(is_valid_age(0))
    print(is_valid_age(150))
    print(is_valid_age(151))
    print(is_valid_age("18"))
    print()
    print('is_strong_password tests:')
    print(is_strong_password('abc12345'))
    print(is_strong_password('abcdefgh'))
    print(is_strong_password('12345678'))
    print(is_strong_password('a1b2c3'))
    print()
    print('is_valid_date tests:')
    print(is_valid_date('2026-02-21'))
    print(is_valid_date('2026-02-29'))
    print(is_valid_date('2024-02-29'))
    print(is_valid_date('2026-13-01'))
    print(is_valid_date('2026-04-31'))