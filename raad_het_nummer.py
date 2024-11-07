import random

def raad_het_getal():

    warm_welkom = print( " → Welkom bij spel: Raad het nummer! ← ")

    maximale_getal = int(input("Voer het maximale getal in waaruit de machine kan kiezen: "))

    # aantal pogingen
    aantal_pogingen = int(input("Hoe vaak wil je kunnen raden? "))

    # Kies een willekeurig getal
    te_raden_getal = random.randint(1, maximale_getal)

    print(f"Je hebt {aantal_pogingen} pogingen om het getal te kunnen raden tussen 1 en {maximale_getal}.")

    # Nu gebruik ik een for-loop voor het aantal pogingen dat mogelijk is
    for poging in range(1, aantal_pogingen + 1):

        # hierbij laat ik de speler vragen voor een gok
        gok = int(input(f"Poging {poging}: Raad het getal: "))

        if gok == te_raden_getal:
            print(f"Gefeliciteerd! Je hebt het getal {te_raden_getal} geraden in {poging} pogingen!")
            opnieuw_spelen = input("wil je dit spel opnieuw spelen? ")
            if opnieuw_spelen in ('ja', 'jup', 'yes', 'ja graag'):
                raad_het_getal()

            elif opnieuw_spelen in ('nee', 'no', 'nope', 'nee dankje'):
                print("Bedankt voor het spelen! Je word nu teruggestuurd naar het hoofdmenu!")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()

            else:
                print("Ongeldige invoer. Je word nu teruggestuurd naar het hoofdmenu!")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()

        elif gok < te_raden_getal:
            print("Te laag!")

        elif gok == '':
            print("Ongeldige invoer.")
        else:
            print("Te hoog!")

        # Feedback
        if poging == aantal_pogingen:
            print(f"Helaas, je hebt geen pogingen meer over. Het getal was {te_raden_getal}.")
            opnieuw = input("Wil je het nog een keer proberen: ")
            if opnieuw in ('ja', 'jup', 'yes', 'ja graag'):
                raad_het_getal()
            elif opnieuw in ['nee', 'no', 'nope', 'nee dankje']:
                print("Snap ik, fijn om met je gespeeld te hebben. Je word teruggestuurd naar het hoofdmenu!")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()
            else:
                print("Ongeldige invoer. Je word teruggestuurd naar het hoofdmenu.")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()


# Voert het spel uit
raad_het_getal()


