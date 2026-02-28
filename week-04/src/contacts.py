import json, os, sys

CONTACTS_FILE = 'contacts.json'

def load_contacts() -> list[dict[str, str]]:
    '''
    Nolasa kontaktus no JSON faila.

    Returns:
        list[dict[str, str]]:
            Saraksts ar kontaktiem vārdnīcu formā:
            {
                'name': str,
                'phone': str
            }

            Ja fails neeksistē, atgriež tukšu sarakstu [].

    Raises:
        json.JSONDecodeError:
            Ja JSON fails ir bojāts vai nepareizā formātā.
    '''

    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_contacts(contacts: list[dict[str, str]]) -> None:
    '''
    Saglabā kontaktu sarakstu JSON failā.

    Args:
        contacts (list[dict[str, str]]):
            Saraksts ar kontaktu vārdnīcām.

    Returns:
        None
    '''
        
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def add_contacts(name: str, phone: str) -> None:
    '''
    Pievieno jaunu kontaktu un saglabā to failā.
    Vārds tiek normalizēts:
        - noņemtas liekās atstarpes
        - vairākas atstarpes aizstātas ar vienu
        - katra vārda pirmais burts kļūst liels

    Args:
        name (str):
            Kontakta vārds un uzvārds.
        phone (str):
            Kontakta tālruņa numurs.

    Returns:
        None

    Example:
        add_contacts("laURA oZOLIŅA", "+371 22001122")
        → saglabā kā "Laura Ozoliņa"
    '''

    contacts = load_contacts()
    name = name.strip().title()
    contacts.append({'name': name, 'phone': phone})
    save_contacts(contacts)
    print(f'Pievienots: {name} ({phone})')

def list_contacts() -> None:
    '''
    Izdrukā visus saglabātos kontaktus.

    Returns:
        None
    '''

    contacts = load_contacts()
    print('Kontakti:')
    if not contacts:
        print('Nav kontaktu!')
        return
    for i, c in enumerate(contacts, start=1):
        print(f'{i}. {c.get('name', '-')} - {c.get('phone', '-')}')

def search_contacts(query: str) -> None:
    '''
    Meklē kontaktus pēc vārda daļas (nav reģistrjutīgs).

    Args:
        query (str):
            Meklējamais teksts.

    Returns:
        None

    Example:
        search_contacts("laura")
        → atrod "Laura Ozoliņa"
    '''

    contacts = load_contacts()
    q = query.strip().lower()
    found = [c for c in contacts if q in c.get('name', '').lower()]
    print(f'Atrasti {len(found)} kontakti:')
    for i, c in enumerate(found, start=1):
        print(f'{i}. {c.get('name', '-')} - {c.get('phone', '-')}')

def how_usage() -> None:
    '''
    Izdrukā programmas lietošanas instrukciju.

    Returns:
        None
    '''

    print('Lietošana:')
    print('-python contacts.py add "Vārds Uzvārds" "+371 XXXXXXXX"')
    print('-python contacts.py list')
    print('-python contacts.py search <vaicājums>')

def main(argv: list[str]) -> None:
    '''
    Programmas galvenā ieejas funkcija.

    Args:
        argv (list[str]):
            Komandrindas argumentu saraksts.

    Returns:
        None

    Raises:
        IndexError:
            Ja trūkst nepieciešamo komandrindas argumentu.
    '''
    
    if len(argv) < 2:
        how_usage()
        return
    
    cmd = argv[1].lower()

    if cmd == 'add':
        if len(argv) != 4:
            print('Kļūda, add nepieciešami 2 argumenti: "vārds uzvārds" un "tālr."')
            how_usage()
            return
        add_contacts(argv[2], argv[3])
    elif cmd == 'list':
        list_contacts()
    elif cmd == 'search':
        if len(argv) != 3:
            print('Kļūda, search vajag 1 argumentu: meklējamais teksts.')
            how_usage()
            return
        search_contacts(argv[2])
    else:
        print(f'Kļūda, nezināma komanda - {argv[1]}')
        how_usage()


if __name__ == '__main__':
    main(sys.argv)