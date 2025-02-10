def gem_kontaktoplysninger():
    filnavn = "kontaktoplysninger.txt"

    # Indtastning af oplysninger
    navn = input("Indtast dit navn: ")
    telefonnummer = input("Indtast dit telefonnummer: ")
    email = input("Indtast din emailadresse: ")

    # Gemmer oplysninger i tekstfilen
    with open(filnavn, "a") as fil:
        fil.write(f"Navn: {navn}\n")
        fil.write(f"Telefonnummer: {telefonnummer}\n")
        fil.write(f"Email: {email}\n")
        fil.write("-" * 30 + "\n")

    print("Dine oplysninger er gemt!")


def vis_kontaktoplysninger():
    filnavn = "kontaktoplysninger.txt"

    try:
        # LÃ¦ser oplysninger fra tekstfilen
        with open(filnavn, "r") as fil:
            indhold = fil.read()
            if indhold:
                print("\nGemte kontaktoplysninger:")
                print(indhold)
            else:
                print("\nIngen kontaktoplysninger fundet.")
    except FileNotFoundError:
        print("\nFilen med kontaktoplysninger eksisterer ikke endnu.")


def hovedmenu():
    while True:
        print("\n--- Kontaktoplysninger ---")
        print("1. Indtast kontaktoplysninger")
        print("2. Vis gemte kontaktoplysninger")
        print("3. Afslut")

        valg = input("VÃ¦lg en mulighed (1-3): ")

        if valg == "1":
            gem_kontaktoplysninger()
        elif valg == "2":
            vis_kontaktoplysninger()
        elif valg == "3":
            print("Farvel!")
            break
        else:
            print("Ugyldigt valg. PrÃ¸v igen.")


# KÃ¸r programmet
hovedmenu()