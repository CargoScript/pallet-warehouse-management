#Programmbeginn
#Lagerverzeichnis
Lager = {
    "PL-EUR-01": {
        "name": "Euro-Palette (Holz) [1.2m x 0.8m]",
        "meldebestand":136,
        "klassen": {"A": 500, "B": 300, "C": 50}
    },
    "PL-IND-02": {
        "name": "Industriepalette (Holz) [1.2m x1.0m]",
        "meldebestand":136,
        "klassen": {"A": 200, "B":180, "C": 50}
    },
    "PL-GIB-03": {
        "name": "Gitterbox (Stahl) [1.2m x 0.8m]",
        "meldebestand":34,
        "klassen": {"A": 150, "B":90, "C": 10}
    },
    "PL-DIS-04": {
        "name": "Displaypalette (Kunststoff) [0.8m x 0.6m]",
        "meldebestand":20,
        "klassen": {"A": 100, "B": 45, "C": 5}
    }
}
#Lagerprogramm
while True:
    print("/n---CargoScript Lagerprogramm---")
    print("1 = Lagerbestand anzeigen")
    print("2 = Wareneingang buchen")
    print("3 = Warenausgang buchen")
    print("4 = Programm beenden")
    auswahl = input("Bitte wähle eine Option:")

    if auswahl == "1":
        print("\n--- Aktueller Lagerbestand---")
        for artikelnummer, details in Lager.items():
            gesamtbestand = sum(details["klassen"].values())

            print(f"/nArtikelnummer: {artikelnummer} | Typ: {details['name']}")
            print(f"  ->Gesamtbestand: {gesamtbestand} Stück (Meldebestand: {details['meldebestand']})")
            print(f"  |_ Davon Klasse A (Neu): {details['klassen']['A']} Stück")
            print(f"  |_ Davon Klasse B (Gebraucht): {details['klassen']['B']} Stück")
            print(f"  |_ Davon Klasse C (Defekt): {details['klassen']['C']} Stück")

        if gesamtbestand <= details['meldebestand']:
            print("Achtung! Meldebestand unterschritten! Bitte Nachbestellen!")
#Wareneingang

    elif auswahl == "2":
        print("Wareneingang buchen")
        artikelnummer = input("Bitte Artikelnummer angeben (z.B. PL-EUR-01):")
        if artikelnummer in Lager:
            klasse = input("Welche Qualitätsklasse wird angeliefert(A/ B/ C/): ").strip().upper()
            if klasse in ["A", "B", "C"]:
                menge = int(input("Wie viele Paletten werden angeliefert? (Stückzahl):"))
                Lager[artikelnummer]["klassen"][klasse] += menge
                if klasse == "C" and Lager[artikelnummer]["klassen"]["C"] > 50:
                    print(f"\n Achtung zu viele deffekte Paletten im Lager({Lager[artikelnummer]['klassen']['C']} Stück)!")
                    print("Bitte entsorgen")
                print(f"/n Erfolg, der Artikelnummer {artikelnummer} wurden {menge} Paletten der Qualitätsklasse {klasse} zugebucht")
            else:
                print("Fehler! ungültige Qualitätsklasse")
        else:
            print("Fehler! Ungültige Artikelnummer")

#Warenausgang

    elif auswahl == "3":
        print("Warenausgang buchen")
        artikelnummer = input("Bitte Artikelnummer angeben (z.B. PL-EUR-01):")
        if artikelnummer in Lager:
            klasse = input("Welche Qualitätsklasse soll ausgebucht werden (A/ B/ C): ").strip().upper()
            if klasse in ["A", "B", "C"]:
                menge = int(input("Wie viele Paletten sollen ausgebucht werden?"))

                Lager[artikelnummer]["klassen"][klasse] -= menge
                print(f"Es wurden {menge} Paletten mit der Artikelnummer{artikelnummer} aus der Qualitätsklasse {klasse} ausgebucht")
                gute_paletten = Lager[artikelnummer]["klassen"]["A"] + Lager[artikelnummer]["klassen"]["B"]
                if gute_paletten <= Lager[artikelnummer]["meldebestand"]:
                    print(f"\" Achtung! Meldestand erreicht bitte Paletten bestellen!")
                    print(f" Wir haben zu wenig Paletten auf Lager ({gute_paletten} Stück)!")
            else:
                print("Fehler! Ungültige Qualitätsklasse" )

        else:print(" Fehler! Ungültige Artikelnummer")

#Programmende
    elif auswahl == "4":
        print("Vielen Dank für die Nutzung der Software ")
        break