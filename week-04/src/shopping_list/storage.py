import json, os

PRICES_FILE = "prices.json"

def normalize_key(name: str) -> str:
    '''
    Normalizē produkta nosaukumu cenu datubāzes atslēgai:
    - noņem liekās atstarpes
    - padara visus burtus mazus (lower)
    '''
    return ' '.join(name.split()).lower()

def load_prices() -> dict[str, float]:
    '''
    Nolasa cenu datubāzi no prices.json.

    Returns:
        dict[str, float]: preces nosaukums -> cena par vienību.
        Ja fails neeksistē vai bojāts, atgriez {}.
    '''

    if not os.path.exists(PRICES_FILE):
        return {}
    try:
        with open(PRICES_FILE, 'r', encoding='utf-8') as f:
            raw = json.load(f)
    except json.JSONDecodeError:
        print('Kļūda: prices.json ir bojāts. Tiks izmantota tukša cenu datubāze.')
        return {}
    normalized = {}
    for k, v in raw.items():
        normalized[normalize_key(k)] = round(float(v), 2)
    return normalized

def save_prices(prices: dict[str, float]) -> None:
    '''
    Saglabā cenu datubāzi prices.json.

    Args:
        prices (dict[str, float]): preces nosaukums -> cena par vienību

    Returns:
        None
    '''
    
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)


def get_price(name: str) -> float | None:
    '''
    Atgriež cenu no cenu datubāzes.

    Args:
        name (str): preces nosaukums

    Returns:
        float | None: cena, ja ir, pretējā gadījumā None
    '''
    
    prices = load_prices()
    return prices.get(normalize_key(name))


def set_price(name: str, price: float) -> None:
    '''
    Saglabā vai atjaunina cenu cenu datubāzē.

    Args:
        name (str): preces nosaukums
        price (float): cena par vienību

    Returns:
        None
    '''
    
    prices = load_prices()
    prices[normalize_key(name)] = round(float(price), 2)
    save_prices(prices)


SHOPPING_FILE = 'shopping.json'

def load_list() -> list[dict[str, float]]:
    '''
    Nolasa iepirkumu sarakstu no JSON faila.

    Returns:
        list[dict[str, float]]:
            Saraksts ar produktiem formātā:
            {'name': str, 'price': float}
            Ja fails neeksistē vai bojāts, atgriež [].
    '''
    
    if not os.path.exists(SHOPPING_FILE):
        return []
    try:
        with open(SHOPPING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print('Kļūda: shopping.json ir bojāts. Tiks izmantots tukšs saraksts.')
        return []


def save_list(items: list[dict[str, float]]) -> None:
    '''
    Saglabā iepirkumu sarakstu JSON failā.

    Args:
        items (list[dict[str, float]]):
            Produktu saraksts.

    Returns:
        None
    '''
    with open(SHOPPING_FILE, 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)