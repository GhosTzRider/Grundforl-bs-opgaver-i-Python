from random import random, randint
from turtledemo.penrose import start

korrekt_tal = randint (1, 100)
Antal_gaet = 0
gÃ¦ttet_rigtigt = False
igen = True

while igen:
    while not gÃ¦ttet_rigtigt:
        # Her for man brugeren til og gÃ¦tte et tal
        gÃ¦t = int(input("GÃ¦t et tal mellem 1 og 100: "))

        Antal_gaet += 1

        while Antal_gaet > 9:
            print('Du har ikke flere gÃ¦t tilbage')
            gÃ¦ttet_rigtigt = True
            break

        # Tjekker om gÃ¦ttet er korrekt
        if gÃ¦t == korrekt_tal:
            print("Flot â rigtig gÃ¦ttet!")
            print(' Du brugte ' + str(Antal_gaet) + ' gÃ¦t')
            gÃ¦ttet_rigtigt = True

        # Tjekker om gÃ¦ttet er uden for de tal vi har bedt om
        elif gÃ¦t < 1 or gÃ¦t > 100:
            print("Uden for det angivne interval pÃ¥ 1-100")
        else:
            # Beregn forskellen mellem tallet og gÃ¦ttet
            forskel = abs(korrekt_tal - gÃ¦t)

            # Tjekker forskellen og giver feedback
            if forskel > 50:
                print("Meget langt forbi")
            elif 20 <= forskel <= 49:
                print("Du er ikke helt ved siden af")
            else:
                print("Tampen brÃ¦nder!") 