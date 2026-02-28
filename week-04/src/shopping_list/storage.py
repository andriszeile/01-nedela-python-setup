import json, os

SHOPPING_FILE = 'shopping.json'


def load_list() -> list[dict[str, float]]:
    '''
    Nolasa iepirkumu sarakstu no JSON faila.

    Returns:
        list[dict[str, float]]:
            Saraksts ar produktiem formātā:
            {'name': str, 'price': float}

            Ja fails neeksistē, atgriež [].
    '''
    
    if not os.path.exists(SHOPPING_FILE):
        return []

    with open(SHOPPING_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


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