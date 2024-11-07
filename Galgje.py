import random
import string
from words import words




def get_valid_word(words):
    word = random.choice(words)  # kiest iets randoms van de lijst
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.lower()


def galgje():
    print(" → Welkom bij spel: Galgje! ← ")
    print("* Het woord is al voor u uitgekozen. U heeft standaard 6 levens. Zodra de levens op zijn, heeft u verloren... *")

    word = get_valid_word(words)
    word_letters = set(word)  # leters in het woord die geraden moeten worden
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  # wat de speler al geraden heeft
    lives = 6  # aantal levens van de speler


    # de input van de speler:
    while len(word_letters) > 0 and lives > 0:
        # laat zien welke letters al ene keer gebruikt zijn
        print('Je hebt deze letters al eens gebruikt: ', ' '.join(used_letters))

        # t hoeveel levens nog over zijn
        print(f'Je hebt nog {lives} levens over.')

        # huidige status van het woord (geraden letters en streepjes voor nog niet geraden letters)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Huidig woord: ', ' '.join(word_list))

        # vraag de speler om een letter te raden
        user_letter = input("Gok een letter: ").lower()

        # controleren of de ingevoerde letter geldig is
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Goed geraden! '{user_letter}' zit in het woord.")
            else:
                lives -= 1  # een leven verliezen bij een verkeerde gok
                print(f"Fout! '{user_letter}' zit niet in het woord.")

        elif user_letter in used_letters:
            print("Je hebt die letter al gebruikt. Probeer een andere.")

        else:
            print("Onbekend karakter. Probeer het opnieuw met een letter uit het alfabet.")

    # einde van het spel
    if lives == 0:
        print(f"Je hebt geen levens meer. Het woord was '{word}'. Je hebt verloren!")
        extra_leven = (input("Wil je nog een keer spelen met een ander woord (ja/nee): "))
        if extra_leven in ('ja', 'jup', 'yes', 'ja graag'):
            galgje()
        elif extra_leven in ['nee', 'no', 'nope', 'nee dankje']:
            print("Snap ik, het is ook een heel lastig spel. Je word teruggestuurd naar het hoofdmenu!")
            import Hoofdmenu_prj_nano
            Hoofdmenu_prj_nano.hoofdmenu()
        else:
            print("Onbekende invoer, je word teruggestuurd naar het hoofdmenu!")
            import Hoofdmenu_prj_nano
            Hoofdmenu_prj_nano.hoofdmenu()


    else:
        print(f"Gefeliciteerd! Je hebt het woord '{word}' geraden.")
        extra_leven2 = input("Wil je nog een keer spelen: ")
        if extra_leven2 in ('ja', 'jup', 'yes', 'ja graag'):
            galgje()
        elif extra_leven2 in ['nee', 'no', 'nope', 'nee dankje']:
            print("Fijne dag verder!")
        else:
            print("Ongeldige invoer. Je word teruggestuurd naar het hoofdmenu!")
            import Hoofdmenu_prj_nano
            Hoofdmenu_prj_nano.hoofdmenu()



# Start het spel
galgje()

