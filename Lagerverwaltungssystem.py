class Produkt:
    

    def __init__(self,id,name,preis,bestand,anzahl):#initialisierung von Produkt
        self.id = id #id des Produkts
        self.name = name #Name des Produkts
        self.preis = preis #Preis des Produkts
        self.bestand= bestand #Bestand des Produkts
        self.anzahl= anzahl #Anzahl des Produkts
        
    def __str__(self):  # Diese Methode fehlte!
        return f"ID: {self.id}, Name: {self.name}, Preis: {self.preis}, Bestand: {self.bestand}, Anzahl: {self.anzahl}"


class Produkt_verwaltung:

    def __init__(self):#initialisierung von Produkt_verwaltung
        self.liste_produkte = [] #Liste von Produkten

    def produkt_anlegen(self,n_id,n_name,n_preis,n_bestand,n_anzahl):
        """set Funktion"""
        neues_Produkt=Produkt(n_id,n_name,n_preis,n_bestand,n_anzahl)
        self.liste_produkte.append(neues_Produkt) 

    def get_all_products(self):
        output = ""
        for produkt in self.liste_produkte:
            output += str(produkt) + "\n"
        return output


    def lagerbestand_anzeigen(self):
        """get Funktion"""
        pass

    def bestand_erhöhen(self,anzahl):
        """Funktionen die nur ein pass haben nennt man Placeholder"""
        return self.bestand + anzahl
    
    def bestand_reduzieren(self,anzahl):
        """Funktionen die nur ein pass haben nennt man Placeholder"""
        return self.bestand - anzahl

produkt_parfüm= Produkt_verwaltung() #Objekt von Produkt

produkt_parfüm.produkt_anlegen(1,"tom_ford",20,10,1)#Aufruf der Funktion
produkt_parfüm.produkt_anlegen(2,"channel",30,20,1)#Aufruf der Funktion
produkt_parfüm.produkt_anlegen(3,"dior",40,30,1)#Aufruf der Funktion


print(f"get all products: \n{produkt_parfüm.get_all_products()}")#ausgabe des Objekts