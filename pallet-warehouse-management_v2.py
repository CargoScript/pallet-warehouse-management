class Palette:
    def __init__(
        self,
        article_number,
        name,
        min_stock_a,
        min_stock_b,
        max_stock_c,
        stock_a=0,
        stock_b=0,
        stock_c=0,
    ):
        self.article_number = article_number
        self.name = name
        self.min_stock_a = min_stock_a
        self.min_stock_b = min_stock_b
        self.max_stock_c = max_stock_c

        self.stock_a = stock_a
        self.stock_b = stock_b
        self.stock_c = stock_c


# Erstellen der Europalette
euro_pallet = Palette(
    article_number="PL-EUR-01",
    name="Europalette (Holz) [1.2m x 0.8m]",
    min_stock_a=330,  # Mindestbestand 10 Volladungen
    min_stock_b=165,  # Mindestbestand 5 Volladungen
    max_stock_c=100,  # Limit für Defekt
    stock_a=700,  # Aktueller Bestand
    stock_b=700,  # Aktueller Bestand
    stock_c=80,  # Aktueller Bestand
)

# Erstellen der Industriepalette
industry_pallet = Palette(
    article_number="PL-IND-02",
    name="Industriepalette (Holz) [1.2m x 1.0m]",
    min_stock_a=250,  # Mindestbestand 10
    min_stock_b=125,  # Mindestbestand 5
    max_stock_c=50,  # Limit für Defekt
    stock_a=0,  # Aktueller Bestand
    stock_b=0,  # Aktueller Bestand
    stock_c=0,  # Aktueller Bestand
)

# Erstellen der Gitterbox
gitterbox = Palette(
    article_number="PL-GIB-03",
    name="Gitterbox (Metall) [1.2m x 0.8m]",
    min_stock_a=330,  # Mindestbestand 10
    min_stock_b=165,  # Mindestbestand 5
    max_stock_c=50,  # Limit für Defekt
    stock_a=0,  # Aktueller Bestand
    stock_b=0,  # Aktueller Bestand
    stock_c=0,  # Aktueller Bestand
)

# Erstellen der Displaypalette
display_pallet = Palette(
    article_number="PL-DIS-04",
    name="Displaypalette (PVC) [0.8m x 0.6m]",
    min_stock_a=660,  # Mindestbestand 10
    min_stock_b=330,  # Mindestbestand 5
    max_stock_c=100,  # Limit für Defekt
    stock_a=0,  # Aktueller Bestand
    stock_b=0,  # Aktueller Bestand
    stock_c=0,  # Aktueller Bestand
)

palletes = [euro_pallet, industry_pallet, gitterbox, display_pallet]


while True:
    print("\n--- Lagerverwaltung ---")
    print("1. Bestand anzeigen")
    print("2. Einbuchen")
    print("3. Ausbuchen")
    print("4. Programm Beenden")

    choice = input("Bitte wählen sie eine Option von (1-4): ")

    if choice == "1":
        print("\n--- Aktueller Bestand ---")
        for p in palletes:
            print(f"\nArtikel: {p.name} ({p.article_number})")
            print(f" -> Klasse A: {p.stock_a} (Mindest: {p.min_stock_a})")
            print(f" -> Klasse B: {p.stock_b} (Mindest: {p.min_stock_b})")
            print(f" -> Klasse C: {p.stock_c} (Maximal: {p.max_stock_c})")

    elif choice == "2":
        print("\n--- Einbuchen ---")
        print("Welche Palette soll eingebucht werden?")

        for index, p in enumerate(palletes, start=1):
            print(f"{index}. {p.name} ({p.article_number})")

        try:
            palette_choice = int(input("Bitte wähle die Nummer der Palette: ")) - 1

            if 0 <= palette_choice < len(palletes):
                selected_palette = palletes[palette_choice]
                print(f"Ausgewählt: {selected_palette.name}")

                quality_class = input(
                    "Welche Qualitätsklasse soll eingebucht werden? (a / b / c): "
                ).strip().lower()
                amount = int(input("Welche Menge soll eingebucht werden: "))

                if amount <= 0:
                    print("Die Menge muss größer 0 sein.")
                    continue

                if quality_class == "a":
                    selected_palette.stock_a += amount
                    print(
                        f"Erfolgreich eingebucht! Neuer Bestand Klasse A: {selected_palette.stock_a}"
                    )
                elif quality_class == "b":
                    selected_palette.stock_b += amount
                    print(
                        f"Erfolgreich eingebucht! Neuer Bestand Klasse B: {selected_palette.stock_b}"
                    )
                elif quality_class == "c":
                    selected_palette.stock_c += amount
                    print(
                        f"Erfolgreich eingebucht! Neuer Bestand Klasse C: {selected_palette.stock_c}"
                    )
                    if selected_palette.stock_c > selected_palette.max_stock_c:
                        print(
                            "Achtung! Der Maximalbestand wird überschritten, bitte Abholung veranlassen!"
                        )
                        print(
                            f"Erlaubt: max. {selected_palette.max_stock_c} | Aktuell: {selected_palette.stock_c}"
                        )
                else:
                    print("Ungültige Qualitätsklasse! Bitte nur 'a', 'b' oder 'c'.")
            else:
                print("Ungültige Paletten-Nummer.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")

    elif choice == "3":
        print("\n--- Ausbuchen ---")
        print("Welche Palette soll ausgebucht werden?")

        for index, p in enumerate(palletes, start=1):
            print(f"{index}. {p.name} ({p.article_number})")

        try:
            palette_choice = int(input("Bitte wähle die Nummer der Palette: ")) - 1

            if 0 <= palette_choice < len(palletes):
                selected_palette = palletes[palette_choice]
                print(f"Ausgewählt: {selected_palette.name}")

                quality_class = input(
                    "Welche Qualitätsklasse soll ausgebucht werden? (a / b / c): "
                ).strip().lower()
                amount = int(input("Welche Menge soll ausgebucht werden: "))

                if amount <= 0:
                    print("Die Menge muss größer 0 sein.")
                    continue

                if quality_class == "a":
                    if amount <= selected_palette.stock_a:
                        selected_palette.stock_a -= amount
                        print(
                            f"Erfolgreich ausgebucht! Neuer Bestand Klasse A: {selected_palette.stock_a}"
                        )
                        if selected_palette.stock_a < selected_palette.min_stock_a:
                            print(
                                "Achtung! Der Minimalbestand wird unterschritten, bitte Paletten bestellen!"
                            )
                            print(
                                f"Erlaubt: min. {selected_palette.min_stock_a} | Aktuell: {selected_palette.stock_a}"
                            )
                    else:
                        print(
                            f"Fehler: Nicht genügend Bestand in Klasse A, Ausbuchen nicht möglich! (Aktuell: {selected_palette.stock_a})"
                        )

                elif quality_class == "b":
                    if amount <= selected_palette.stock_b:
                        selected_palette.stock_b -= amount
                        print(
                            f"Erfolgreich ausgebucht! Neuer Bestand Klasse B: {selected_palette.stock_b}"
                        )
                        if selected_palette.stock_b < selected_palette.min_stock_b:
                            print(
                                "Achtung! Der Minimalbestand wird unterschritten, bitte Paletten bestellen!"
                            )
                            print(
                                f"Erlaubt: min. {selected_palette.min_stock_b} | Aktuell: {selected_palette.stock_b}"
                            )
                    else:
                        print(
                            f"Fehler: Nicht genügend Bestand in Klasse B, Ausbuchen nicht möglich ! (Aktuell: {selected_palette.stock_b})"
                        )

                elif quality_class == "c":
                    if amount <= selected_palette.stock_c:
                        selected_palette.stock_c -= amount
                        print(
                            f"Erfolgreich ausgebucht! Neuer Bestand Klasse C: {selected_palette.stock_c}"
                        )
                    else:
                        print(
                            f"Fehler: Nicht genügend Bestand in Klasse C! (Aktuell: {selected_palette.stock_c})"
                        )
                else:
                    print("Ungültige Qualitätsklasse! Bitte nur 'a', 'b' oder 'c'.")
            else:
                print("Ungültige Paletten-Nummer.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")

    elif choice == "4":
        print("\n--- Programm Beenden ---")
        break

    else:
        print("\nUngültige Eingabe. Bitte wählen sie eine Option von (1-4): ")
