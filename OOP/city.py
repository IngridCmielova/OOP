class Mesto:
    def __init__(self, nazev_mesta, nazev_regionu, nazev_zeme, pocet_obyvatel, psc, smerove_cislo_oblasti):
        self.nazev_mesta = nazev_mesta
        self.nazev_regionu = nazev_regionu
        self.nazev_zeme = nazev_zeme
        self.pocet_obyvatel = pocet_obyvatel
        self.psc = psc
        self.smerove_cislo_oblasti = smerove_cislo_oblasti

    # Metody pro vstup dat
    def set_nazev_mesta(self, nazev_mesta):
        self.nazev_mesta = nazev_mesta

    def set_nazev_regionu(self, nazev_regionu):
        self.nazev_regionu = nazev_regionu

    def set_nazev_zeme(self, nazev_zeme):
        self.nazev_zeme = nazev_zeme

    def set_pocet_obyvatel(self, pocet_obyvatel):
        self.pocet_obyvatel = pocet_obyvatel

    def set_psc(self, psc):
        self.psc = psc

    def set_smerove_cislo_oblasti(self, smerove_cislo_oblasti):
        self.smerove_cislo_oblasti = smerove_cislo_oblasti

    # Metody pro výstup dat
    def get_nazev_mesta(self):
        return self.nazev_mesta

    def get_nazev_regionu(self):
        return self.nazev_regionu

    def get_nazev_zeme(self):
        return self.nazev_zeme

    def get_pocet_obyvatel(self):
        return self.pocet_obyvatel

    def get_psc(self):
        return self.psc

    def get_smerove_cislo_oblasti(self):
        return self.smerove_cislo_oblasti

    # Metoda pro výpis všech dat
    def vypis_udaje(self):
        print(f"Název města: {self.nazev_mesta}")
        print(f"Název regionu: {self.nazev_regionu}")
        print(f"Název země: {self.nazev_zeme}")
        print(f"Počet obyvatel: {self.pocet_obyvatel}")
        print(f"PSČ: {self.psc}")
        print(f"Směrové číslo oblasti: {self.smerove_cislo_oblasti}")

# Příklad použití třídy
mesto1 = Mesto("Praha", "Praha", "Česká republika", 1300000, "11000", "+420")
mesto2 = Mesto("Brno", "Jihomoravský kraj", "Česká republika", 380000, "60200", "+420")
mesto3 = Mesto("Ostrava", "Moravskoslezský kraj", "Česká republika", 290000, "70200", "+420")

# Výpis dat o městech
print("Údaje o městě 1:")
mesto1.vypis_udaje()

print("\nÚdaje o městě 2:")
mesto2.vypis_udaje()

print("\nÚdaje o městě 3:")
mesto3.vypis_udaje()

# Změna počtu obyvatel pro město 2
mesto2.set_pocet_obyvatel(385000)
print("\nAktualizovaný počet obyvatel pro město 2:")
print(mesto2.get_pocet_obyvatel())