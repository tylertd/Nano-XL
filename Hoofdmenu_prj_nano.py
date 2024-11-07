def hoofdmenu():
    while True:
        print("⫘⫘⫘⫘⫘⫘ 𝐖𝐞𝐥𝐤𝐨𝐦 𝐛𝐢𝐣 𝐀𝐩𝐩-𝐬𝐭𝐨𝐫𝐞 𝐏𝐲𝐀𝐩𝐩𝐬! ⫘⫘⫘⫘⫘⫘")
        print("Kies uw gewenste applicatie:")
        print("Optie 1: Raad het getal")
        print("Optie 2: Galgje")
        print("Optie 3: Steen, papier, schaar")
        print("Optie 4: Boter, kaas & eieren (multiplayer) ")
        print("Optie 5: Rekenspel")
        print("Optie 6: Verlaat de App-store. ")
        keuze = input("Voer je keuze in (1 t/m 6): ")

        if keuze == "1":
            import raad_het_nummer
            raad_het_nummer.raad_het_getal()
        elif keuze == "2":
            import Galgje
            Galgje.galgje()
        elif keuze == "3":
            import steen_papier_schaar
            steen_papier_schaar.steen_papier_schaar()
        elif keuze == '4':
            import boter_kaas_eieren
            boter_kaas_eieren.speel_boter_kaas_eieren()
        elif keuze == '5':
            import rekenspel
            rekenspel.rekenspel()
        elif keuze == '6':
            print("Leuk om met je gespeeld te hebben. Tot de volgende keer!")
            break
        else:
            print("Onbekende invoer. Probeer het opnieuw")
            return hoofdmenu()



if __name__ == "__main__":
    hoofdmenu()


