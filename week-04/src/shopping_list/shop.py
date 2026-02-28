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
    Pievieno produktu iepirkumu sarakstam.

    Args:
        argv (list[str]):
            Komandrindas argumenti.

    Returns:
        None
    '''

    if len(argv) != 4:
        print('Kļūda: add nepieciešami 2 argumenti — nosaukums un cena.')
        return
    name = argv[2].strip().capitalize()
    try:
        price = float(argv[3])
    except ValueError:
        print('Kļūda: cena jābūt skaitlim.')
        return
    items = load_list()
    items.append({'name': name, 'price': round(price, 2)})
    save_list(items)
    print(f'Pievienots: {name} ({price:.2f} EUR)')

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