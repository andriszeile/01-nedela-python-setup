def calc_line_total(item: dict) -> float:
    '''
    Aprēķina vienas rindas summu (daudzums × cena).

    Args:
        item (dict):
            Produkta dati ar atslēgām:
            - qty (int)
            - price (float)

    Returns:
        float: Rindas kopsumma.
    '''
    
    return round(item['qty'] * item['price'], 2)


def calc_grand_total(items: list[dict]) -> float:
    '''
    Aprēķina visu produktu kopējo summu.

    Args:
        items (list[dict]): Produktu saraksts.

    Returns:
        float: Kopējā summa.
    '''
    
    return round(sum(calc_line_total(i) for i in items), 2)


def count_units(items: list[dict]) -> int:
    '''
    Saskaita kopējo vienību skaitu.

    Args:
        items (list[dict]): Produktu saraksts.

    Returns:
        int: Kopējais daudzums.
    '''
    
    return sum(i['qty'] for i in items)