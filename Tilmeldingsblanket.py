def main():
    file_name = "Tilmeldings_blanket.txt"

    while True:
        print("\nVelkommen til tilmeldingsprogrammet!")
        print("1. Tilmeld dig")
        print("2. Vis gemte tilmeldingsblanketter")
        print("3. Afslut")

        try:
            choice = input("VÃ¦lg en mulighed (1/2/3): ")
        except OSError as e:
            print(f"Inputfejl: {e}. Kan ikke lÃ¦se valg.")
            return

        if choice == "1":
            indtast_oplysninger(file_name)
        elif choice == "2":
            vis_oplysninger(file_name)
        elif choice == "3":
            print("Farvel!")
            break
        else:
            print("Ugyldigt valg. PrÃ¸v igen.")

def indtast_oplysninger(file_name):
    print("\nTilmeld dig:")
    try:
        navn = input("Navn: ")
        alder = input("Alder: ")
        email = input("Email: ")
        telefon = input("Telefonnummer: ")

    except OSError as e:
        print(f"Inputfejl: {e}. Kan ikke lÃ¦se oplysninger.")
        return

    try:
        with open(file_name, "a") as file:
            file.write(f"Navn: {navn}\n")
            file.write(f"Alder: {alder}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Telefonnummer: {telefon}\n")
            file.write("-" * 20 + "\n")

        print("Oplysningerne er gemt!")
    except OSError as e:
        print(f"Filfejl: {e}. Kan ikke gemme oplysninger.")

def vis_oplysninger(file_name):
    try:
        with open(file_name, "r") as file:
            print("\nGemte tilmeldingsblanketter:")
            print(file.read())
    except FileNotFoundError:
        print("Der er ingen gemte oplysninger endnu.")
    except OSError as e:
        print(f"Filfejl: {e}. Kan ikke lÃ¦se oplysninger.")

# KÃ¸r programmet
if __name__ == "__main__":
    main()