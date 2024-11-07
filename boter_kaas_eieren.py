def print_bord(bord):
    print("\n")
    for row in bord:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winnaar(bord, speler):
    for i in range(3):
        if all([bord[i][j] == speler for j in range(3)]) or all([bord[j][i] == speler for j in range(3)]):
            return True
    if bord[0][0] == speler and bord[1][1] == speler and bord[2][2] == speler:
        return True
    if bord[0][2] == speler and bord[1][1] == speler and bord[2][0] == speler:
        return True
    return False


def check_gelijkspel(bord):
    return all([cel != " " for rij in bord for cel in rij])


def zet_speler(bord, speler):
    while True:
        try:
            zet = int(input(f"Speler {speler}, kies een positie (1-9): ")) - 1
            rij, kolom = zet // 3, zet % 3
            if bord[rij][kolom] == " ":
                bord[rij][kolom] = speler
                break
            else:
                print("Deze positie is al bezet. Kies een andere.")
        except (ValueError, IndexError):
            print("Ongeldige invoer. Kies een getal tussen 1 en 9.")


def speel_boter_kaas_eieren():
    print(" → Welkom bij spel: Boter, Kaas en Eieren! ← ")
    print("Dit spel is bedoeld voor 2 spelers. Veel speelplezier!")
    print("Het bord heeft de volgende posities:\n")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 \n")

    bord = [[" " for _ in range(3)] for _ in range(3)]
    huidige_speler = "X"

    while True:
        print_bord(bord)
        zet_speler(bord, huidige_speler)

        if check_winnaar(bord, huidige_speler):
            print_bord(bord)
            print(f"Gefeliciteerd! Speler {huidige_speler} heeft gewonnen!")
            opnieuw_spelen = input("Wil je opnieuw spelen? (ja/nee): ").lower()
            if opnieuw_spelen in ('ja', 'jup', 'yes', 'ja graag'):
                speel_boter_kaas_eieren()
            elif opnieuw_spelen in ('nee', 'no', 'nope', 'nee dankje'):
                print("Bedankt voor het spelen! Je wordt nu teruggestuurd naar het hoofdmenu!")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()
            else:
                print("Ongeldige invoer. Je wordt nu teruggestuurd naar het hoofdmenu!")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()
            break

        elif check_gelijkspel(bord):
            print_bord(bord)
            print("Het is een gelijkspel!")
            opnieuw_spelen = input("Wil je opnieuw spelen? (ja/nee): ").lower()
            if opnieuw_spelen in ('ja', 'jup', 'yes', 'ja graag'):
                speel_boter_kaas_eieren()
            elif opnieuw_spelen in ('nee', 'no', 'nope', 'nee dankje'):
                print("Bedankt voor het spelen! Je wordt nu teruggestuurd naar het hoofdmenu!")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()
            else:
                print("Ongeldige invoer. Je wordt nu teruggestuurd naar het hoofdmenu!")
                import Hoofdmenu_prj_nano
                Hoofdmenu_prj_nano.hoofdmenu()
            break

        huidige_speler = "O" if huidige_speler == "X" else "X"


# Start het spel
speel_boter_kaas_eieren()
