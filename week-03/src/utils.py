'''
Utilītu bibliotēka (virknes, skaitļi, saraksti).
"Tīras" (pure) funkcijas ar validāciju un docstring.
'''
#palīgfunkcijas
def _validate_string(text):
    '''
    Pārbauda vai text ir virkne

    Args:
        text: pārbaudāmais tekts

    Returns:
        None
    
    Raises:
        TypeError: ja text nav str
    '''
    if not isinstance(text, str):
        raise TypeError('text jābūt virknei')


def _validate_number(x):
    '''
    Pārbauda vai x ir skaitlis

    Args:
        x: pārbaudāmā vērtība

    Returns:
        None
    
    Raises:
        TypeError: ja x nav int vai float
    '''
    if not isinstance(x, (int, float)):
        raise TypeError('Vērtībai jābūt skaitlim')
    

#virknes
def capitalize(text):
    '''
    Ievadītā teksta sākumburtu pārveido par lielo.
    
    Args:
        text: ievades teksts
    
    Returns:
        str: teksts ar lielo sākumburtu.

    Example:
    >>> capitalize('labdien')
    'Labdien'
    '''
    _validate_string(text)
    return text[:1].upper() + text[1:]


def truncate(text, max_len=20):
    '''
    Saīsina tekstu līdz max_len simboliem.

    Args:
        text: ievades teksts
        max_len: maksimālais garums (noklusējums 20)

    Returns:
        str: saīsināts teksts

    Raises:
        TypeError: max_len jābūt int
        ValueError: max_len jābūt >= 0

    Example:
        >>> truncate("Sveika pasaule", 8)
        'Sveik...'
    '''
    _validate_string(text)

    if not isinstance(max_len, int):
        raise TypeError('max_len jābūt int')
    if max_len < 0:
        raise ValueError('max_len jābūt >= 0')

    if len(text) <= max_len:
        return text

    if max_len <= 3:
        return '.' * max_len

    return text[:max_len - 3] + '...'


def count_words(text):
    """
    Saskaita vārdus tekstā.

    Args:
        text: ievades teksts

    Returns:
        int: vārdu skaits

    Example:
        >>> count_words("Šis ir tests")
        3
    """
    _validate_string(text)

    return len(text.split())


# Skaitļi
def clamp(num, low, high):
    '''
    Ierobežo skaitli diapazonā [low; high].

    Args:
        num: skaitlis
        low: minimums
        high: maksimums

    Returns:
        int/float: ierobežotā vērtība

    Raise:
        ValueError: low jābūt <= high

    Example:
        >>> clamp(15, 0, 10)
        10
    '''
    _validate_number(num)
    _validate_number(low)
    _validate_number(high)

    if low > high:
        raise ValueError('low jābūt <= high')

    return max(low, min(num, high))


def is_prime(num):
    '''
    Pārbauda, vai skaitlis ir pirmskaitlis.

    Args:
        num: vesels skaitlis

    Returns:
        bool: True, ja pirmskaitlis

    Raise:
        TypeError: num jābūt int

    Example:
        >>> is_prime(7)
        True
    '''
    if not isinstance(num, int):
        raise TypeError('num jābūt int')

    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def factorial(n):
    '''
    Aprēķina faktoriālu n!.

    Args:
        n: vesels skaitlis >= 0

    Returns:
        int: n!
    
    Raise:
        TypeError: n jābūt int
        ValueError: n jābūt >= 0

    Example:
        >>> factorial(5)
        120
    '''
    if not isinstance(n, int):
        raise TypeError('n jābūt int')
    if n < 0:
        raise ValueError('n jābūt >= 0')

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


# Saraksti / kolekcijas
def total(numbers):
    '''
    Aprēķina saraksta summu.

    Args:
        numbers: skaitļu kolekcija

    Returns:
        int/float: summa

    Example:
        >>> total([1, 2, 3])
        6
    '''
    s = 0

    for x in numbers:
        _validate_number(x)
        s += x

    return s


def average(numbers, default=None):
    '''
    Aprēķina vidējo aritmētisko.

    Args:
        numbers: skaitļu kolekcija
        default: vērtība tukšam sarakstam

    Returns:
        float/int: vidējā vērtība

    Raise:
        ValueError: Tukšs saraksts

    Example:
        >>> average([2, 4, 6])
        4.0
    '''
    s = 0
    count = 0

    for x in numbers:
        _validate_number(x)
        s += x
        count += 1

    if count == 0:
        if default is None:
            raise ValueError('Tukšs saraksts')
        return default

    return s / count


def total_args(*numbers):
    '''
    Aprēķina summu no mainīga skaita skaitļu (*args).

    Args:
        *numbers: skaitļi

    Returns:
        int/float: summa

    Example:
        >>> total_args(1, 2, 3)
        6
    '''
    s = 0

    for x in numbers:
        _validate_number(x)
        s += x

    return s


# Demonstrācija

if __name__ == "__main__":
    print(capitalize('labas dienas'))
    print(truncate('Šis ir garais teksts apgriešanai', 10))
    print(count_words('Šos vārdus skaita'))

    print(clamp(15, 0, 10))
    print(is_prime(17))
    print(factorial(6))

    print(total([1, 2, 3]))
    print(average([10, 20, 30]))
    print(total_args(5, 10, 15))