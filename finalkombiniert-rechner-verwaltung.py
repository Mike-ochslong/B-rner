class Person:
    def __init__(self, name, alter, geschlecht, ziel, gewicht, körpergröße, aktivitätsfaktor):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht
        self.ziel = ziel
        self.gewicht = gewicht
        self.körpergröße = körpergröße
        self.aktivitätsfaktor = aktivitätsfaktor
    
    def update_gewicht(self, neues_gewicht):
        self.gewicht = neues_gewicht
    
    def update_ziel(self, neues_ziel):
        self.ziel = neues_ziel


# Aktivitätsfaktoren
GERINGER_AKTIVITÄTSFAKTOR = 1.2
MÄSSIGER_AKTIVITÄTSFAKTOR = 1.375
MITTLERER_AKTIVITÄTSFAKTOR = 1.55
MITTELHOHER_AKTIVITÄTSFAKTOR = 1.725
HOHER_AKTIVITÄTSFAKTOR = 1.9

# BMR Berechnungsvariablen für Männer
GRUNDFAKTOR_MANN = 88.362
GEWICHT_FAKTOR_MANN = 13.397
GRÖSSE_FAKTOR_MANN = 4.799
ALTER_FAKTOR_MANN = 5.677

# BMR Berechnungsvariablen für Frauen
GRUNDFAKTOR_FRAU = 655
GEWICHT_FAKTOR_FRAU = 9.6
GRÖSSE_FAKTOR_FRAU = 1.8
ALTER_FAKTOR_FRAU = 4.7


class Rechner:          
    def __init__(self, person):
        self.person = person
    
    def BMR_Berechnen(self):
        if self.person.geschlecht == "m":
            return GRUNDFAKTOR_MANN + (GEWICHT_FAKTOR_MANN * self.person.gewicht) + (GRÖSSE_FAKTOR_MANN * self.person.körpergröße) - (ALTER_FAKTOR_MANN * self.person.alter)
        elif self.person.geschlecht == "w":
            return GRUNDFAKTOR_FRAU + (GEWICHT_FAKTOR_FRAU * self.person.gewicht) + (GRÖSSE_FAKTOR_FRAU * self.person.körpergröße) - (ALTER_FAKTOR_FRAU * self.person.alter)
        else:
            return None
    
    def Gesamtumsatz_Berechnen(self):
        BMR = self.BMR_Berechnen()
        return BMR * self.person.aktivitätsfaktor if BMR else None


class Kalorienziel:
    def __init__(self, person, zielgewicht, zeitspanne):
        self.person = person
        self.zielgewicht = zielgewicht
        self.zeitspanne = zeitspanne
    
    def Kalorienziel_berechnen(self):
        return (self.zielgewicht - self.person.gewicht) * 7000 / self.zeitspanne
    
    def Kalorienbedarf_mit_Ziel(self):
        BMR = Rechner(self.person).BMR_Berechnen()
        return BMR + self.Kalorienziel_berechnen() if BMR else None


class Verwaltung:
    def __init__(self):
        self.personen_liste = []
    
    def person_anlegen(self, name, alter, geschlecht, ziel, gewicht, körpergröße, aktivitätsfaktor):
        neue_person = Person(name, alter, geschlecht, ziel, gewicht, körpergröße, aktivitätsfaktor)
        self.personen_liste.append(neue_person)
    
    def BMR_berechnen(self, person_name):
        person = next((p for p in self.personen_liste if p.name == person_name), None)
        if person:
            return Rechner(person).BMR_Berechnen()
        return None
    
    def Gesamtumsatz_berechnen(self, person_name):
        person = next((p for p in self.personen_liste if p.name == person_name), None)
        if person:
            return Rechner(person).Gesamtumsatz_Berechnen()
        return None
    
    def Kalorienziel_berechnen(self, person_name, zielgewicht, zeitspanne):
        person = next((p for p in self.personen_liste if p.name == person_name), None)
        if person:
            return Kalorienziel(person, zielgewicht, zeitspanne).Kalorienbedarf_mit_Ziel()
        return None



verwaltung = Verwaltung()
verwaltung.person_anlegen()
