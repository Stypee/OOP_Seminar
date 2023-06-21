from funkcije import graf_sve_statistike_igraca, graf_poeni_igraca, graf_asistencije_igraca
from funkcije import graf_skokovi_igraca, graf_statistika_igraca_u_jednoj_utakmici, grafovi_usporedbe_dva_igraca, prosjek_statistike_igraca
from utilities import unos_intervala

running = True

while running:
    print("-"*24)
    print("1. Graf statistike jednog igrača")
    print("2. Graf poena jednog igrača")
    print("3. Graf skokova jednog igrača")
    print("4. Graf asistencija jednog igrača")
    print("5. Graf statistike jednog igrača za jednu utakmicu")
    print("6. Graf usporedbe statistika dva igrača")
    print("7. Ispis prosjeka statistike jednog igrača")
    print("8. Zaustavi program")
    print("-"*24)

    akcija = unos_intervala(1,8)

    if akcija == 1:
        graf_sve_statistike_igraca()
    elif akcija == 2:
        graf_poeni_igraca()
    elif akcija == 3:
        graf_skokovi_igraca()
    elif akcija == 4:
        graf_asistencije_igraca()
    elif akcija == 5:
        graf_statistika_igraca_u_jednoj_utakmici()
    elif akcija == 6:
        grafovi_usporedbe_dva_igraca()
    elif akcija == 7:
        prosjek_statistike_igraca()
    elif akcija == 8:
        running = False

