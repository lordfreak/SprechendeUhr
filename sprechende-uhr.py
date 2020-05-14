import time

HOURS = { 0: "zwölf", 
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

def get_time():
    t = time.localtime()
    return t.tm_hour, t.tm_min
    
def time_to_string(h, m):

    if m < 25:
        h_str = HOURS[h]
    else:
        h_str = HOURS[h+1]
        
    if m < 2:
        before_after = ""
        
        if h == 1:
            h_str = h_str[0:-1]
            
        h_str += " Uhr"   
    
    elif m < 5: 
        before_after = "kurz nach"
    elif m < 10:
        before_after = "fünf nach"
    elif m < 15:
        before_after = "zehn nach"
    elif m < 20:
        before_after = "viertel nach"
    elif m < 25:
        before_after = "zwanzig nach"
    elif m < 27:
        before_after = "fünf vor halb"
    elif m < 30: 
        before_after = "kurz vor halb"
    elif m < 32:
        before_after = "halb"
    elif m < 35:
        before_after = "kurz nach"
    elif m < 40:
        before_after = "fünf nach halb"
    elif m < 45:
        before_after = "zwanzig vor"
    elif m < 50:
        before_after = "viertel vor"
    elif m < 55:
        before_after = "zehn vor"
    elif m < 58:
        before_after = "fünf vor"
    elif m >= 58:
        before_after = "kurz vor"

    else:
        pass
        
    return f"Es ist {before_after} {h_str}.".replace("  ", " ")
    
output_old = ""    
    
while True:
    hour, min = get_time()
    output = time_to_string(hour, min)
    if not output_old == output:
        output_old = output
        print(output)
    time.sleep(1)
