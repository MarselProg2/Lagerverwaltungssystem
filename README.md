# Lagerverwaltungssystem
 Das Lagerverwaltungssystem ist eine einfache Anwendung zur Verwaltung von Produkten in einem Lager. Es ermöglicht das Anlegen neuer Produkte, das Verwalten des Bestands und das Abrufen von Produktinformationen. 

# Lagerverwaltungssystem

## Übersicht
Das Lagerverwaltungssystem ist eine einfache Anwendung zur Verwaltung von Produkten in einem Lager. Es ermöglicht das Anlegen neuer Produkte, das Verwalten des Bestands und das Abrufen von Produktinformationen.

## Funktionen

### Kernfunktionalitäten
- **Produkte anlegen**: Neue Produkte können mit einer eindeutigen ID, Namen, Preis und initialem Bestand im System erfasst werden
- **Bestand verwalten**: Der Bestand vorhandener Produkte kann erhöht oder verringert werden, um Zu- und Abgänge zu dokumentieren
- **Produktinformationen abrufen**: Detaillierte Informationen zu einzelnen Produkten können jederzeit eingesehen werden
- **Lagerbestand anzeigen**: Eine Übersicht aller im System erfassten Produkte mit aktuellem Bestand kann generiert werden

## Technische Umsetzung

### Objektorientiertes Design
Das System basiert auf folgenden OOP-Konzepten:

- **Klassen**: Die zentrale Klasse `Produkt` bildet die Grundlage für die Verwaltung einzelner Artikel
- **Attribute**: Jedes Produkt-Objekt verfügt über die Eigenschaften:
  - id (eindeutige Identifikation)
  - name (Produktbezeichnung)
  - preis (Verkaufspreis)
  - bestand (aktuelle Stückzahl)
- **Methoden**: Implementierte Funktionen zur:
  - Bestandsänderung
  - Anzeige von Produktinformationen
  - Aktualisierung von Produktdaten

### Technische Anforderungen
- Entwicklung in Python oder einer anderen objektorientierten Programmiersprache
- Initiale Datenhaltung über Listen/Dictionaries
- Modularer Aufbau für spätere Erweiterungen

## Verwendung

### Grundlegende Operationen
1. **Produkt anlegen**
   - Erfassen der Produktdaten (ID, Name, Preis)
   - Setzen des initialen Bestands

2. **Bestandsverwaltung**
   - Erhöhen des Produktbestands bei Wareneingang
   - Verringern des Bestands bei Warenausgang

3. **Informationsabfrage**
   - Einzelne Produktdetails abrufen
   - Gesamtübersicht aller Produkte anzeigen

## Erweiterungsmöglichkeiten

### Geplante Funktionalitäten
->
1. **Datenpersistenz**
   - Integration einer Datenbank
   - Dateibasierte Speicherung

2. **Benutzeroberfläche**
   - Entwicklung einer grafischen Benutzeroberfläche
   - Intuitive Bedienung für Endanwender

3. **Benutzerverwaltung**
   - Implementierung verschiedener Benutzerrollen
   - Rechteverwaltung für unterschiedliche Funktionen
   - Zugriffsprotokollierung
