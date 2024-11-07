import random


def steen_papier_schaar(speler_score=0, computer_score=0, eerste_keer=True):
    opties = ['steen', 'papier', 'schaar']
    bot_opties = random.choice(opties)

    if eerste_keer:
        print("Welkom bij het spel: Steen, papier, schaar!")
        print("Je speelt nu tegen de computer. Zodra jij of de computer 3 punten heeft behaald eindigt het spel.")

    speler_keuze = input("Steen, papier, schaar: ").lower()

    if speler_keuze not in opties:
        print("Ongeldige keuze. Probeer het opnieuw.")
        return steen_papier_schaar(speler_score, computer_score, eerste_keer=False)

    print(f"De computer koos: {bot_opties}")

    if speler_keuze == bot_opties:
        print("Gelijkspel!")
    elif (speler_keuze == "steen" and bot_opties == "schaar") or \
            (speler_keuze == "papier" and bot_opties == "steen") or \
            (speler_keuze == "schaar" and bot_opties == "papier"):
        print("Je wint deze ronde!")
        speler_score += 1
    else:
        print("De computer wint deze ronde!")
        computer_score += 1

    print(f"Score - Speler: {speler_score} | Computer: {computer_score}")

    if speler_score == 3:
        print("Gefeliciteerd! Je hebt gewonnen met 3 punten!")
    elif computer_score == 3:
        print("De computer heeft gewonnen met 3 punten! Probeer het nog eens.")
    else:
        return steen_papier_schaar(speler_score, computer_score, eerste_keer=False)

    opnieuw_spelen = input("Wil je het nog een keer proberen? ").lower()
    ja_variaties = ['ja', 'yes', 'yeah', 'jup', 'j', 'jaa', 'jazeker', 'yep', 'y', 'si', 'yup']
    nee_variaties = ['nee', 'no', 'nope', 'nah', 'ne', 'nop', 'niet', 'niet nu', 'n', 'absoluut niet']

    if opnieuw_spelen in ja_variaties:
        return steen_papier_schaar(0, 0,
                                   eerste_keer=True)
    elif opnieuw_spelen in nee_variaties:
        print("Bedankt voor het spelen!")
        print("Je word nu teruggestuurd naar het hoofdmenu!")
        import Hoofdmenu_prj_nano
        Hoofdmenu_prj_nano.hoofdmenu()
    else:
        print("Ongeldige invoer. Probeer het opnieuw.")
        return


steen_papier_schaar()
