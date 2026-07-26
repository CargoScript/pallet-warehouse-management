#Programmbeginn
#Lagerverzeichnis: Klasse A= Verpackung, Klasse B= Tausch, Klasse C= Defekt
Lager = {
    "PL-EUR-01": {
        "name": "Euro-Palette (Holz) [1.2m x 0.8m]",
        "meldebestand": {"A": 136, "B": 100},
        "klassen": {"A": 500, "B": 300, "C": 50}
    },
    "PL-IND-02": {
        "name": "Industriepalette (Holz) [1.2m x1.0m]",
        "meldebestand": {"A": 136, "B": 80},
        "klassen": {"A": 200, "B":180, "C": 50}
    },
    "PL-GIB-03": {
        "name": "Gitterbox (Stahl) [1.2m x 0.8m]",
        "meldebestand": {"A": 34, "B": 20},
        "klassen": {"A": 150, "B":90, "C": 10}
    },
    "PL-DIS-04": {
        "name": "Displaypalette (Kunststoff) [0.8m x 0.6m]",
        "meldebestand":{"A": 20, "B": 10},
        "klassen": {"A": 100, "B": 45, "C": 5}
    }
}
#Lagerprogramm
while True:
    print("\n---CargoScript Lagerprogramm---")
    print("1 = Lagerbestand anzeigen")
    print("2 = Wareneingang buchen")
    print("3 = Warenausgang buchen")
    print("4 = Programm beenden")
    auswahl = input("Bitte Option wählen:")

    if auswahl == "1":
        print("\n--- Aktueller Lagerbestand---")
        for artikelnummer, details in Lager.items():
            gesamtbestand = sum(details["klassen"].values())

            print(f"\nArtikelnummer: {artikelnummer} | Typ: {details['name']}")
            print(f"  ->Gesamtbestand: {gesamtbestand} Stück (Meldebestand: {details['meldebestand']})")
            print(f"  |_ Davon Klasse A (Verpackung/Neu): {details['klassen']['A']} Stück")
            print(f"  |_ Davon Klasse B (Tausch/Benutzt): {details['klassen']['B']} Stück")
            print(f"  |_ Davon Klasse C (Defekt): {details['klassen']['C']} Stück")

        if details['klassen']['A'] <= details['meldebestand']['A']:
            print("Achtung! Meldebestand unterschritten! Bitte Nachbestellen!")
        if details['klassen']['B'] <= details['meldebestand']['B']:
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
                    print(" Bitte entsorgen")
                print(f"\n Erfolg, der Artikelnummer {artikelnummer} wurden {menge} Paletten der Qualitätsklasse {klasse} zugebucht")
            else:
                print("Fehler! ungültige Qualitätsklasse")
        else:
            print("Fehler! Ungültige Artikelnummer")

#Warenausgang

    elif auswahl == "3":
        print("Warenausgang buchen")
        artikelnummer = input("Bitte Artikelnummer angeben (z.B. PL-EUR-01): ").strip().upper()

        if artikelnummer in Lager:
            klasse = input("Welche Qualitätsklasse soll ausgebucht werden (A/ B/ C): ").strip().upper()

            if klasse in ["A", "B", "C"]:
                menge = int(input("Wie viele Paletten sollen ausgebucht werden? "))

# 1. Prüfen, ob überhaupt genug Paletten dieser Klasse da sind
                if menge > Lager[artikelnummer]["klassen"][klasse]:
                    print(f"Fehler! Nicht genügend Paletten der Klasse {klasse} vorhanden (Aktuell: {Lager[artikelnummer]['klassen'][klasse]} Stück).")
                else:
# 2. Menge abziehen
                    Lager[artikelnummer]["klassen"][klasse] -= menge
                    aktueller_bestand = Lager[artikelnummer]["klassen"][klasse]
                    print(f"Es wurden {menge} Paletten ({artikelnummer}, Klasse {klasse}) erfolgreich ausgebucht.")

# 3. Meldebestand-Prüfung für A und B
                    if klasse in ["A", "B"]:
                        ziel_meldebestand = Lager[artikelnummer]["meldebestand"][klasse]

                        if aktueller_bestand <= ziel_meldebestand:
                            verwendungszweck = "Verpackung" if klasse == "A" else "Tausch"
                            print(f"\nACHTUNG: Meldebestand für Klasse {klasse} ({verwendungszweck}) erreicht oder unterschritten!")
                            print(f"Aktueller Bestand Klasse {klasse}: {aktueller_bestand} Stück (Meldebestand: {ziel_meldebestand} Stück).")
                            print(f"Bitte Nachbestellung/Beschaffung für Klasse {klasse} veranlassen!")

            else:
                print("Fehler! Ungültige Qualitätsklasse.")
        else:
            print("Fehler! Ungültige Artikelnummer.")



#Programmende
    elif auswahl == "4":
        print("Vielen Dank für die Nutzung der Software ")
        break