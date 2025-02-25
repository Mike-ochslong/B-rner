class Person:
    # Constructor to initialize the instance variables
    def __init__(self, name, alter, geschlecht_m_oder_w, ziel_zu_oder_abnehmen , gewicht, körpergröße):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht_m_oder_w 
        self.ziel = ziel_zu_oder_abnehmen   
        self.gewicht = gewicht
        self.körpergröße = körpergröße


    # Method to display the person's details
    def display_info(self):
        print(f"Name: {self.name}, alter: {self.alter}, geschlecht: {self.geschlecht}, ziel_zu_oder_abnehmen: {self.ziel}, gewicht: {self.gewicht}, körpergröße: {self.körpergröße} ")
    
    # Method to update the person's gewicht
    def update_gewicht(self, new_gewicht):
        self.gewicht = new_gewicht
    
    # Method to update the person's ziel
    def update_ziel(self, new_ziel):
        self.ziel = new_ziel

#geschlecht = input(str("Geben sie Ihr geschlecht an. (m/w)"))
#groeße = int(input("Geben sie ihre Größe in cm an."))
#alter = int(input("Geben sie ihr Alter an."))
#gewicht = int(input("Geben sie ihr Gewicht an."))

#Aktivitätsfakoren
geringer_aktivitätsfaktor = 1.2
mittlerer_aktivitätsfaktor = 1.55
hoher_aktivitätsfaktor = 1.9

#Berechnungsfaktoren Mann
Grundfaktorm = 88.362
Gewicht_faktorm = 13.397
groeße_faktorm = 4.799
Alter_faktorm = 5.677
#Faktoren Frau
Grundfaktorw = 655
Gewicht_faktorw = 9.6
groeße_faktorw = 1.8
Alter_faktorw = 4.7

class Rechner:
    def init(self, gewicht, groeße, alter):
        self.gewicht = gewicht
        self.groeße = groeße
        self.alter = alter
    def BMR_Berechnen_mann(self):
        # Berechnung des BMR für Männer
        BMRm = Grundfaktorm + (Gewicht_faktorm * self.gewicht) + (
            groeße_faktorm * self.groeße) - (Alter_faktorm * self.alter)
        return BMRm

    def BMR_Berechnen_frau(self):
        # Berechnung des BMR für Frauen
        BMRw = Grundfaktorw + (Gewicht_faktorw * self.gewicht) + (
            groeße_faktorw * self.groeße) - (Alter_faktorw * self.alter)
        return BMRw

class Verwaltung:
    def __init__(self):
        # Liste zum Speichern von Personen
        self.personen_liste = []
    
    def person_anlegen(self, name, alter, geschlecht, ziel, gewicht, körpergröße):
        # Erstellt eine neue Person und fügt sie der Liste hinzu
        neue_person = Person(name, alter, geschlecht, ziel, gewicht, körpergröße)
        self.personen_liste.append(neue_person)
        print(f"Person {name} wurde hinzugefügt.")
    
    def BMR_berechnen(self, person_name, aktivitätsfaktor):
        # Sucht die Person in der Liste
        person = next((p for p in self.personen_liste if p.name == person_name), None)
        
        if person:
            # Erstellt ein Rechner-Objekt für die Berechnung
            rechner = Rechner(person.gewicht, person.körpergröße, person.alter)
            
            # Berechnung je nach Geschlecht
            if person.geschlecht == "m":
                bmr = rechner.BMR_Berechnen_mann()
            elif person.geschlecht == "w":
                bmr = rechner.BMR_Berechnen_frau()
            else:
                print("Ungültiges Geschlecht.")
                return
            
            # Gesamtumsatz berechnen
            gesamtumsatz = bmr * aktivitätsfaktor
            print(f"BMR für {person.name}: {bmr:.2f} kcal")
            print(f"Gesamtumsatz mit Aktivitätsfaktor {aktivitätsfaktor}: {gesamtumsatz:.2f} kcal")
        else:
            print("Person nicht gefunden.")
    
    def personen_anzeigen(self):
        # Zeigt alle gespeicherten Personen an
        if not self.personen_liste:
            print("Keine Personen vorhanden.")
        else:
            for person in self.personen_liste:
                person.display_info()





    





# Creating an instance of the Person class
#person1 = Person("John Doe", 30)

# Calling the display_info method to show person's details
#person1.display_info()

# Updating the age of the person
#person1.updat_gewicht(31)

# Displaying the updated details
#person1.display_info()

class Verwaltung:
    def __init__(self):
        # Liste zum Speichern von Personen
        self.personen_liste = []
    
    def person_anlegen(self):
        # Benutzerfreundliche Eingabe über das Terminal
        name = input("Geben Sie den Namen ein: ")
        alter = int(input("Geben Sie das Alter ein: "))
        geschlecht = input("Geben Sie das Geschlecht ein (m/w): ")
        ziel = input("Geben Sie das Ziel ein (zunehmen/abnehmen): ")
        gewicht = float(input("Geben Sie das Gewicht in kg ein: "))
        körpergröße = int(input("Geben Sie die Körpergröße in cm ein: "))
        
        # Erstellt eine neue Person und fügt sie der Liste hinzu
        neue_person = Person(name, alter, geschlecht, ziel, gewicht, körpergröße)
        self.personen_liste.append(neue_person)
        print(f"Person {name} wurde hinzugefügt.")
    
    def BMR_berechnen(self, person_name, aktivitätsfaktor):
        # Sucht die Person in der Liste
        person = next((p for p in self.personen_liste if p.name == person_name), None)
        
        if person:
            # Erstellt ein Rechner-Objekt für die Berechnung
            rechner = Rechner(person.gewicht, person.körpergröße, person.alter)
            
            # Berechnung je nach Geschlecht
            if person.geschlecht == "m":
                bmr = rechner.BMR_Berechnen_mann()
            elif person.geschlecht == "w":
                bmr = rechner.BMR_Berechnen_frau()
            else:
                print("Ungültiges Geschlecht.")
                return
            
            # Gesamtumsatz berechnen
            gesamtumsatz = bmr * aktivitätsfaktor
            print(f"BMR für {person.name}: {bmr:.2f} kcal")
            print(f"Gesamtumsatz mit Aktivitätsfaktor {aktivitätsfaktor}: {gesamtumsatz:.2f} kcal")
        else:
            print("Person nicht gefunden.")
    
    def personen_anzeigen(self):
        # Zeigt alle gespeicherten Personen an
        if not self.personen_liste:
            print("Keine Personen vorhanden.")
        else:
            for person in self.personen_liste:
                person.display_info()

# Beispiel für die Nutzung:
verwaltung = Verwaltung()
verwaltung.person_anlegen()
verwaltung.personen_anzeigen()
verwaltung.BMR_berechnen(input("Geben Sie den Namen der Person zur BMR-Berechnung ein: "), mittlerer_aktivitätsfaktor)
