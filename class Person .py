class Person:
    # Diese Klasse speichert die Eigenschaften und Ziele einer Person
    def __init__(self, name, alter, geschlecht, ziel, gewicht, körpergröße, aktivitätsfaktor):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht
        self.ziel = ziel
        self.gewicht = gewicht
        self.körpergröße = körpergröße
        self.aktivitätsfaktor = aktivitätsfaktor

    def update_gewicht(self, neues_gewicht):
        # Aktualisiert das Gewicht der Person
        self.gewicht = neues_gewicht

    def update_ziel(self, neues_ziel):
        # Aktualisiert das Ziel der Person
        self.ziel = neues_ziel


class Rechner:
    # Diese Klasse berechnet den Grund- und Gesamtumsatz einer Person
    def __init__(self, person):
        self.person = person

    def BMR_Berechnen(self):
        # Berechnet den Grundumsatz basierend auf Geschlecht, Gewicht, Größe und Alter
        if self.person.geschlecht == "m":
            return 88.362 + (13.397 * self.person.gewicht) + (4.799 * self.person.körpergröße) - (5.677 * self.person.alter)
        elif self.person.geschlecht == "w":
            return 655 + (9.6 * self.person.gewicht) + (1.8 * self.person.körpergröße) - (4.7 * self.person.alter)
            return None

    def Gesamtumsatz_Berechnen(self):
        # Berechnet den Gesamtumsatz basierend auf dem Grundumsatz und Aktivitätsfaktor
        BMR = self.BMR_Berechnen()
        return BMR * self.person.aktivitätsfaktor if BMR else None


class Kalorienziel:
    # Diese Klasse berechnet das Kalorienziel basierend auf dem Zielgewicht und der Zeitspanne
    def __init__(self, person, zielgewicht, zeitspanne):
        self.person = person
        self.zielgewicht = zielgewicht
        self.zeitspanne = zeitspanne

    def Kalorienziel_berechnen(self):
        # Berechnet das tägliche Kaloriendefizit oder -überschuss
        return (self.zielgewicht - self.person.gewicht) * 7000 / self.zeitspanne

    def Kalorienbedarf_mit_Ziel(self):
        # Berechnet den täglichen Kalorienbedarf, um das Ziel zu erreichen
        BMR = Rechner(self.person).BMR_Berechnen()
        return BMR + self.Kalorienziel_berechnen() if BMR else None


class Verwaltung:
    # Diese Klasse dient als zentrale Steuerung und verwaltet Benutzereingaben
    def __init__(self):
        self.personen_liste = []
        self.mahlzeit = Mahlzeit()

    def person_anlegen(self):
        # Legt eine neue Person mit Benutzereingabe an
        name = input("Name: ")
        alter = int(input("Alter: "))
        geschlecht = input("Geschlecht (m/w): ")
        ziel = input("Ziel: ")
        gewicht = float(input("Gewicht (kg): "))
        körpergröße = float(input("Körpergröße (cm): "))
        aktivitätsfaktor = float(input("Aktivitätsfaktor: "))
        neue_person = Person(name, alter, geschlecht, ziel, gewicht, körpergröße, aktivitätsfaktor)
        self.personen_liste.append(neue_person)

    def BMR_berechnen(self, person_name):
        # Berechnet den BMR einer bestimmten Person
        person = next((p for p in self.personen_liste if p.name == person_name), None)
        if person:
            return Rechner(person).BMR_Berechnen()
        return None

    def Gesamtumsatz_berechnen(self, person_name):
        # Berechnet den Gesamtumsatz einer bestimmten Person
        person = next((p for p in self.personen_liste if p.name == person_name), None)
        if person:
            return Rechner(person).Gesamtumsatz_Berechnen()
        return None

    def kalorien_ändern(self):
        # Ändert die Kalorienzahl und addiert sie zur bestehenden Summe
        kalorien = int(input("Kalorien hinzufügen: "))
        self.mahlzeit.kalorien_ändern(kalorien)

    def fette_ändern(self):
        # Ändert die Fettmenge und addiert sie zur bestehenden Summe
        fette = int(input("Fette hinzufügen: "))
        self.mahlzeit.fette_ändern(fette)

    def gesättigte_ändern(self):
        # Ändert die gesättigten Fette und addiert sie zur bestehenden Summe
        gesättigte = int(input("Gesättigte Fette hinzufügen: "))
        self.mahlzeit.gesättigte_ändern(gesättigte)

    def kohlenhydrate_ändern(self):
        # Ändert die Kohlenhydratmenge und addiert sie zur bestehenden Summe
        kohlenhydrate = int(input("Kohlenhydrate hinzufügen: "))
        self.mahlzeit.kohlenhydrate_ändern(kohlenhydrate)

    def eiweiß_ändern(self):
        # Ändert die Eiweißmenge und addiert sie zur bestehenden Summe
        eiweiß = int(input("Eiweiß hinzufügen: "))
        self.mahlzeit.eiweiß_ändern(eiweiß)


class Mahlzeit:
    # Diese Klasse repräsentiert eine Mahlzeit und deren Nährwerte
    def __init__(self, kalorien=0, fette=0, gesättigte=0, kohlenhydrate=0, eiweiß=0):
        self.kalorien = kalorien
        self.fette = fette
        self.gesättigte = gesättigte
        self.kohlenhydrate = kohlenhydrate
        self.eiweiß = eiweiß


# Menü für Benutzereingaben
verwaltung = Verwaltung()
while True:
    print("1: Neue Person anlegen")
    print("2: BMR berechnen")
    print("3: Gesamtumsatz berechnen")
    print("4: Kalorien hinzufügen")
    print("5: Fette hinzufügen")
    auswahl = input("Auswahl: ")

    if auswahl == "1":
        verwaltung.person_anlegen()
    elif auswahl == "2":
        name = input("Name der Person: ")
        print(f"BMR: {verwaltung.BMR_berechnen(name)}")
    elif auswahl == "3":
        name = input("Name der Person: ")
        print(f"Gesamtumsatz: {verwaltung.Gesamtumsatz_berechnen(name)}")
    elif auswahl == "4":
        verwaltung.kalorien_ändern()
    elif auswahl == "5":
        verwaltung.fette_ändern()
    else:
        print("Ungültige Auswahl")

        else:
