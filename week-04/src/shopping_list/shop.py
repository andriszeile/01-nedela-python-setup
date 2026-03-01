import sys
from storage import load_list, save_list, get_price, set_price
from utils import calc_line_total, calc_grand_total, count_units

def how_usage() -> None:
    '''
    Izdrukā programmas lietošanas instrukciju.
    '''
    print('Lietošana:')
    print('python shop.py add <Nosaukums> <Cena>')
    print('python shop.py list')
    print('python shop.py total')
    print('python shop.py clear')

def parse_positive_float(value: str) -> float:
    '''
    Pārvērš tekstu par pozitīvu float (cenu).

    Raises:
        ValueError:
            Cenai jābūt skaitlim (piem., 1.25).
            Cenai jābūt pozitīvai (> 0).
    '''

    try:
        x = float(value)
    except ValueError:
        raise ValueError('Cenai jābūt skaitlim (piem., 1.25).')
    if x <= 0:
        raise ValueError('Cenai jābūt pozitīvai (> 0).')
    return round(x, 2)

def resolve_price_interactive(name: str) -> float:
    '''
    Nosaka cenu:
      - ja cena atrodas prices.json: piedāvā [A]kceptēt / [M]ainīt
      - ja nav: prasa ievadīt cenu un saglabā datubāzē

    Returns:
        float: cena par vienību
    '''

    existing = get_price(name)
    if existing is not None:
        print(f'Atrasta cena: {existing:.2f} EUR/gab.')
        choice = input('[A]kceptēt / [M]ainīt? > ').strip().lower()
        if choice == 'm':
            while True:
                try:
                    new_price = parse_positive_float(input('Jaunā cena: > ').strip())
                    break
                except ValueError as e:
                    print(f'Kļūda: {e}')
            set_price(name, new_price)
            print(f'Cena atjaunināta: {name} -> {new_price:.2f} EUR')
            return new_price
        # fefaults: akceptē (arī, ja ievada ko citu)
        return float(existing)
    print('Cena nav zināma.')
    while True:
        try:
            price = parse_positive_float(input('Ievadi cenu: ').strip())
            break
        except ValueError as e:
            print(f'Kļūda: {e}')
    set_price(name, price)
    print(f'Cena saglabāta: {name} ({price:.2f} EUR)')
    return price

def cmd_add(argv: list[str]) -> None:
    '''
    Pievieno produktu ar daudzumu un cenu par vienību.

    Args:
        argv (list[str]):
            Komandrindas argumenti.
            argv[2] - produkta nosaukums (str)
            argv[3] - daudzums (int, >0)
            argv[4] - daudzums (float, > 0)

    Returns:
        None
    
    Raises:
        ValueError:
            Kļūda, daudzums ir vesels pozitīvs skaitlis.
            Kļūda: cena jābūt pozitīvam skaitlim.
    '''

    if len(argv) not in (4, 5):
        print('Kļūda: add sintakse: add <Nosaukums> <daudzums> [cena].')
        return
    name = " ".join(argv[2].split()).capitalize()
    try:
        qty = int(argv[3])
        if qty <=0:
            raise ValueError
    except ValueError:
        print('Kļūda, daudzums ir vesels pozitīvs skaitlis.')
        return
    if len(argv)==5:
        try:
            price = parse_positive_float(argv[4])
        except ValueError as e:
            print(f'Kļūda: {e}')
            return
        set_price(name, price) #atceras cenu db
    else:
        price = resolve_price_interactive(name)
    items = load_list()
    item = {
        'name': name,
        'qty': qty,
        'price': round(price, 2)
    }
    items.append(item)
    save_list(items)
    line_total = calc_line_total(item)
    print(f'Pievienots: {name} * {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR')

def cmd_list() -> None:
    '''
    Izdrukā visu iepirkumu sarakstu ar:
        - daudzumu
        - cenu par vienību
        - rindas kopējo summu
    '''
    
    items = load_list()
    print("Iepirkumu saraksts:")
    if not items:
        print('saraksts tukšs')
        return
    for i, item in enumerate(items, start=1):
        line_total = calc_line_total(item)
        print(
            f'  {i}. {item["name"]} * {item['qty']} — '
            f'{item["price"]:.2f} EUR/gab. - '
            f'{line_total:.2f} EUR'
            )

def cmd_total() -> None:
    '''
    Aprēķina kopējo un izdrukā kopējo:
        - summu
        - vienību skaitu
        - produktu skaitu
    '''

    items = load_list()
    total = calc_grand_total(items)
    units = count_units(items)
    print(f'Kopā: {total:.2f} EUR, ({units} vienības, {len(items)} produkti)')

def cmd_clear() -> None:
    '''
    Notīra iepirkumu sarakstu.
    '''

    save_list([])
    print('Saraksts notīrīts.')


def main(argv: list[str]) -> None:
    '''
    Programmas galvenā ieejas funkcija.
    '''

    if len(argv) < 2:
        how_usage()
        return
    cmd = argv[1].lower()
    if cmd == 'add':
        cmd_add(argv)
    elif cmd == 'list':
        cmd_list()
    elif cmd == 'total':
        cmd_total()
    elif cmd == 'clear':
        cmd_clear()
    else:
        print('Nezināma komanda.')
        how_usage()


if __name__ == '__main__':
    main(sys.argv)