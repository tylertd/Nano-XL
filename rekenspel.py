import random

def rekenspel():
    print("Welkom bij het rekenspel!")
    print("Kies een moeilijkheidsniveau: ")
    print("1 - Makkelijk (optellen en aftrekken)")
    print("2 - Gemiddeld (optellen, aftrekken en vermenigvuldigen)")
    print("3 - Moeilijk (optellen, aftrekken, vermenigvuldigen en delen)")

    score = 0

    while True:
        gebruikersvraag = int(input("Kies je moeilijkheidsgraad(1-2-3): "))
        if gebruikersvraag == 1:
            bewerkingen = ["+", "-"]
        elif gebruikersvraag == 2:
            bewerkingen = ["+", "-", "*"]
        elif gebruikersvraag == 3:
            bewerkingen = ["+", "-", "*", "/"]
        else:
            print("Ongeldige invoer. Probeer het opnieuw.")
            return

        bewerking = random.choice(bewerkingen)

        if bewerking == "/":
            getal1 = random.randint(1, 20) * random.randint(1, 10)
            getal2 = random.randint(1, 10)
        elif gebruikersvraag == 1:
            getal1 = random.randint(1, 20)
            getal2 = random.randint(1, 20)
        elif gebruikersvraag == 2:
            getal1 = random.randint(10, 50)
            getal2 = random.randint(1, 10)
        else:
            getal1 = random.randint(20, 100)
            getal2 = random.randint(1, 20)

        if bewerking == "+":
            correct_antwoord = getal1 + getal2
        elif bewerking == "-":
            correct_antwoord = getal1 - getal2
        elif bewerking == "*":
            correct_antwoord = getal1 * getal2
        else:  # Delen
            correct_antwoord = getal1 // getal2

        try:
            gok = int(input(f"Wat is {getal1} {bewerking} {getal2}? "))
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")
            continue

        if gok == correct_antwoord:
            print("Goed gedaan! Dat is correct.")
            score += 1
        else:
            print(f"Helaas, dat is onjuist. Het correcte antwoord was {correct_antwoord}.")

        print(f"Je huidige score is: {score}")

        doorgaan = input("Wil je doorgaan? (ja/nee): ")
        if doorgaan == "ja":
            rekenspel()
        elif doorgaan == "nee":
            print("Leuk om met je gespeeld te hebben! je word nu teruggestuurd naar het hoofdmenu!")
            import Hoofdmenu_prj_nano
            Hoofdmenu_prj_nano.hoofdmenu()


    print(f"Bedankt voor het spelen! Je eindscore is: {score}")


rekenspel()

