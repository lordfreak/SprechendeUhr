import time

# dict mit sprechenden Stundenbezeichnungen
STUNDEN = { 0: "zwölf", 
            1: "eins",
            2: "zwei",
            3: "drei",
            4: "vier",
            5: "fünf",
            6: "sechs",
            7: "sieben",
            8: "acht",
            9: "neun",
           10: "zehn",
           11: "elf",
           12: "zwölf",
           13: "eins",
           14: "zwei",
           15: "drei",
           16: "vier",
           17: "fünf",
           18: "sechs",
           19: "sieben",
           20: "acht",
           21: "neun",
           22: "zehn",
           23: "elf",
           24: "zwölf"
          }
          
# Zeit in Sekunden zwischen den Aktualisierungen
ZEIT_AKTUALISIERUNG = 1

def hole_zeit():
    
    """
    Funktion hole_zeit holt die lokale Systemzeit
    EINGABE ---     
    AUSGABE (int) zeit.tm_hour: Stunde
            (int) zeit.tm_min: Minute
    """
    
    zeit = time.localtime()
    
    return zeit.tm_hour, zeit.tm_min
    
def zeit_zu_text(std, min):

    """
    Funktion zeit_zu_text wandelt die Zahlenwerte für
    Stunde und Minute in einen sprechenden Text um.
    EINGABE (int) std: Stunde
            (int) min: Minute
    AUSGABE (str) uhrzeit_text: Uhrzeit in sprechender Form
    """

    # Zahlenbereich prüfen
    if not 0 <= std < 24:
        raise ValueError(f"ungültiger Stundenwert: {std}")
        
    if not 0 <= min < 60:
        raise ValueError(f"ungültiger Minutenwert: {min}")
    
    # Stundentexte festlegen
    if min < 25:
        std_text = STUNDEN[std]
    else:
        std_text = STUNDEN[std + 1]
        
    if min < 2:
        vor_nach_text = ""
        
        if std == 1:
            # s am Ende abschneiden --> "ein Uhr" statt "eins Uhr"
            std_text = std_text[0:-1]
            
        std_text += " Uhr"   
    
    # Minutentexte festlegen
    elif min < 5: 
        vor_nach_text = "kurz nach"
    elif min < 10:
        vor_nach_text = "fünf nach"
    elif min < 15:
        vor_nach_text = "zehn nach"
    elif min < 20:
        vor_nach_text = "viertel nach"
    elif min < 25:
        vor_nach_text = "zwanzig nach"
    elif min < 27:
        vor_nach_text = "fünf vor halb"
    elif min < 30: 
        vor_nach_text = "kurz vor halb"
    elif min < 32:
        vor_nach_text = "halb"
    elif min < 35:
        vor_nach_text = "kurz nach"
    elif min < 40:
        vor_nach_text = "fünf nach halb"
    elif min < 45:
        vor_nach_text = "zwanzig vor"
    elif min < 50:
        vor_nach_text = "viertel vor"
    elif min < 55:
        vor_nach_text = "zehn vor"
    elif min < 58:
        vor_nach_text = "fünf vor"
    elif min >= 58:
        vor_nach_text = "kurz vor"
    
    # String für Textausgabe zusammensetzen
    uhrzeit_text = f"Es ist {vor_nach_text} {std_text}.".replace("  ", " ")
    
    return uhrzeit_text
    
letzte_ausgabe = ""    
    
while True:

    std, min = hole_zeit()
    ausgabe = zeit_zu_text(std, min)
    
    # nur bei Änderungen ausgeben
    if not letzte_ausgabe == ausgabe:
        
        letzte_ausgabe = ausgabe
        print(ausgabe)
        
    # warten    
    time.sleep(ZEIT_AKTUALISIERUNG)
    
    # TODO: Taste zum Beenden definieren
    # TODO: Terminal leeren vor Aktualisierung
