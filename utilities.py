import sqlite3

def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u intervalu od {min} do {max}: "))

            if broj<min or broj>max:
                raise Exception('Broj nije u intervalu!')

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj

def izbor_igrac():
    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime FROM igrac''')

    izbor = c.fetchall()

    print('Popis igrača:')
    for i, informacije in enumerate(izbor, start=1):
        print(f'\t{i}. {informacije[0]} {informacije[1]}')

    igrac_id = unos_intervala(1, len(izbor))

    conn.close()

    return igrac_id

def izbor_utakmica():
    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT domaca_ekipa, gostujuca_ekipa, datum FROM utakmica''')

    izbor = c.fetchall()

    print('Popis utakmica:')
    for i, informacije in enumerate(izbor, start=1):
        print(f'\t{i}. {informacije[0]} - {informacije[1]}   {informacije[2]}')

    utakmica_id = unos_intervala(1, len(izbor))

    return utakmica_id

def unos_razliticih_igraca(igrac_1):
    while True:
        try:
            igrac_2 = izbor_igrac()

            if igrac_2 == igrac_1:
                raise Exception('Izabrali ste istog igrača!')

        except ValueError:
            print('Unijeli ste znak, a ne broj!')

        except Exception as e:
            print(e)

        else:
            return igrac_2
