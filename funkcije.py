import sqlite3
import matplotlib.pyplot as plt

from utilities import izbor_igrac, izbor_utakmica, unos_razliticih_igraca


#Funkcija za crtanje grafa svih statistika jednog igrača
def graf_sve_statistike_igraca():
    igrac_id = izbor_igrac()

    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime, broj_dresa, pozicija, poeni, skokovi, asistencije
                  FROM igrac
                  LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                  WHERE igrac_id = {igrac_id} ''')

    statistike = c.fetchall()

    conn.close()

    podatci = statistike[0]
    poeni = [statistika[4] for statistika in statistike]
    skokovi = [statistika[5] for statistika in statistike]
    asistencije = [statistika[6] for statistika in statistike]

    utakmice = range(1, len(statistike) + 1)

    plt.plot(utakmice, poeni, label='Poeni')
    plt.plot(utakmice, skokovi, label='Skokovi')
    plt.plot(utakmice, asistencije, label='Asistencije')

    plt.xlabel('Utakmica')
    plt.ylabel('Statistika')
    plt.title(f'{podatci[0]} {podatci[1]} - {podatci[2]} - {podatci[3]}')

    plt.legend()
    plt.grid()
    plt.show()

#Funkcija za crtanje grafa poena jednog igrača
def graf_poeni_igraca():
    igrac_id = izbor_igrac()

    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime, broj_dresa, pozicija, poeni
                  FROM igrac
                  LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                  WHERE igrac_id = {igrac_id} ''')

    statistike = c.fetchall()

    conn.close()

    podatci = statistike[0]
    poeni = [statistika[4] for statistika in statistike]

    utakmice = range(1, len(statistike) + 1)

    plt.bar(utakmice, poeni, color='blue', label='Poeni')

    plt.xlabel('Utakmica')
    plt.ylabel('Poeni')
    plt.title(f'{podatci[0]} {podatci[1]} - {podatci[2]} - {podatci[3]}')

    plt.grid()
    plt.show()

#Funkcija za crtanje grafa skokova jednog igrača
def graf_skokovi_igraca():
    igrac_id = izbor_igrac()

    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime, broj_dresa, pozicija, skokovi
                  FROM igrac
                  LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                  WHERE igrac_id = {igrac_id} ''')

    statistike = c.fetchall()

    conn.close()

    podatci = statistike[0]
    skokovi = [statistika[4] for statistika in statistike]

    utakmice = range(1, len(statistike) + 1)

    plt.bar(utakmice, skokovi, color='red', label='Poeni')

    plt.xlabel('Utakmica')
    plt.ylabel('Skokovi')
    plt.title(f'{podatci[0]} {podatci[1]} - {podatci[2]} - {podatci[3]}')

    plt.grid()
    plt.show()

#Funkcija za crtanje grafa asistencija jednog igrača
def graf_asistencije_igraca():
    igrac_id = izbor_igrac()

    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime, broj_dresa, pozicija, asistencije
                  FROM igrac
                  LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                  WHERE igrac_id = {igrac_id} ''')

    statistike = c.fetchall()

    conn.close()

    podatci = statistike[0]
    asistencije = [statistika[4] for statistika in statistike]

    utakmice = range(1, len(statistike) + 1)

    plt.bar(utakmice, asistencije, color='green', label='Poeni')

    plt.xlabel('Utakmica')
    plt.ylabel('Asistencije')
    plt.title(f'{podatci[0]} {podatci[1]} - {podatci[2]} - {podatci[3]}')

    plt.grid()
    plt.show()

#Funkcija za izračun prosjeka statistike svih utakmica
def prosjek_statistike_igraca():
    igrac_id = izbor_igrac()

    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime, ekipa, broj_dresa, pozicija, AVG(poeni), AVG(skokovi), AVG(asistencije)
                  FROM igrac
                  LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                  WHERE igrac_id = {igrac_id} ''')

    upit = c.fetchall()

    conn.close()

    podatci = upit[0]

    print(f'{podatci[0]} {podatci[1]} igrac {podatci[2]}-a s brojem dresa {podatci[3]}\n'
          f'koji igra na poziciji {podatci[4]} je u NBA Playoff 2023 na prosjeku od\n'
         f'{podatci[5]} poena, {podatci[6]} skokova i {podatci[7]} asistencija.')

#Funckija za crtanje grafa statistike igrača u jednoj utakmici
def graf_statistika_igraca_u_jednoj_utakmici():
    igrac_id = izbor_igrac()
    utakmica_id = izbor_utakmica()

    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime, broj_dresa, pozicija,poeni, skokovi, asistencije
                  FROM igrac
                  LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                  LEFT JOIN utakmica ON utakmica.id = statistika.utakmica_id
                  WHERE igrac_id = {igrac_id} AND utakmica_id = {utakmica_id} ''')

    statistike = c.fetchall()

    conn.close()

    podatci = statistike[0]
    statistika = [podatci[4], podatci[5], podatci[6]]
    x = [0, 1, 2]

    plt.bar(x, statistika, width=0.2, color ='black', label=f'1.Poeni\n2.Skokovi\n3.Asistencije' )

    plt.xlabel(f'{utakmica_id}. utakmica')
    plt.ylabel('Statistike')
    plt.title(f'{podatci[0]} {podatci[1]} - {podatci[2]} - {podatci[3]}')

    ax = plt.gca()
    ax.axes.xaxis.set_ticklabels([])
    plt.legend()
    plt.grid()
    plt.show()

def grafovi_usporedbe_dva_igraca():
    print('Izaberi 1. igrača')
    igrac_1 = izbor_igrac()

    print('Izaberi 2. igrača')
    igrac_2 = unos_razliticih_igraca(igrac_1)

    conn = sqlite3.connect('nba_playoff_DB.db')
    c = conn.cursor()

    c.execute(f'''SELECT ime, prezime,SUM(poeni), SUM(skokovi), SUM(asistencije)
                      FROM igrac
                      LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                      WHERE igrac_id = {igrac_1} ''')

    statistike_1 = c.fetchall()

    c.execute(f'''SELECT ime, prezime,SUM(poeni), SUM(skokovi), SUM(asistencije)
                      FROM igrac
                      LEFT JOIN statistika ON statistika.igrac_id = igrac.id
                      WHERE igrac_id = {igrac_2} ''')

    statistike_2 = c.fetchall()

    conn.close()

    podatci_1 = statistike_1[0]
    podatci_2 = statistike_2[0]

    poeni = [podatci_1[2], podatci_2[2]]
    skokovi = [podatci_1[3], podatci_2[3]]
    asistencije = [podatci_1[4], podatci_2[4]]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle(f'{podatci_1[0]} {podatci_1[1]}(plavo) vs {podatci_2[0]} {podatci_2[1]}(narancasto)')

    ax1.pie(poeni, radius=1, labels=poeni,  autopct='%1.1f%%', textprops=dict(color="black"))
    ax1.set_title('Poeni')

    ax2.pie(skokovi, radius=1, labels=skokovi, autopct='%1.1f%%', textprops=dict(color="black"))
    ax2.set_title('Skokovi')

    ax3.pie(asistencije, radius=1, labels=asistencije, autopct='%1.1f%%', textprops=dict(color="black"))
    ax3.set_title('Asistencije')

    plt.show()
