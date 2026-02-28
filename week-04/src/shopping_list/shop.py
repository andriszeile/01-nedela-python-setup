import sys
from storage import load_list, save_list
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

def cmd_add(argv: list[str]) -> None:
    '''
    Pievieno produktu ar daudzumu un cenu par vienību.

    Args:
        argv (list[str]):
            Komandrindas argumenti.
            argv[2] - produkta nosaukums (str)
            argv[3] - daudums (int, >0)
            argv[4] - daudzums (float, > 0)

    Returns:
        None
    
    Raises:
        ValueError:
            Kļūda, daudzums ir vesels pozitīvs skaitlis.
            Kļūda: cena jābūt pozitīvam skaitlim.
    '''

    if len(argv) != 5:
        print('Kļūda: add nepieciešami 3 argumenti — nosaukums, daudzums un cena.')
        return
    name = ' '.join(argv[2].strip()).capitalize()
    try:
        qty = int(argv[3])
        if qty <=0:
            raise ValueError
    except ValueError:
        print('Kļūda, daudzums ir vesels pozitīvs skaitlis.')
        return
    try:
        price = float(argv[4])
        if price <= 0:
            raise ValueError
    except ValueError:
        print('Kļūda: cena jābūt pozitīvam skaitlim.')
        return
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
    Izdrukā visu iepirkumu sarakstu.
    '''
    
    items = load_list()
    print("Iepirkumu saraksts:")
    if not items:
        print('saraksts tukšs')
        return
    for i, item in enumerate(items, start=1):
        print(f'  {i}. {item["name"]} — {item["price"]:.2f} EUR')

def cmd_total() -> None:
    '''
    Aprēķina kopējo iepirkumu summu.
    '''

    items = load_list()
    total = sum(item['price'] for item in items)
    print(f'Kopā: {total:.2f} EUR ({len(items)} produkti)')

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