class Person:
    # Constructor to initialize the instance variables
    def __init__(self, name, alter, geschlecht, ziel_zu_oder_abnehmen , gewicht, körpergröße):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht  
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


class Verwaltung:
    def __innit__(self):
    

    def person_anlegen (self, name, alter, geschlecht, ziel_zu_oder_abnehmen , gewicht, körpergröße):
        Person(self, name, alter, geschlecht, ziel_zu_oder_abnehmen , gewicht, körpergröße)



# Creating an instance of the Person class
#person1 = Person("John Doe", 30)

# Calling the display_info method to show person's details
#person1.display_info()

# Updating the age of the person
#person1.updat_gewicht(31)

# Displaying the updated details
#person1.display_info()
