#--------------1--------------------------
def myPutStr(word):

    if isinstance(word, (int, float)):
        return "et pourquoi pas 42 ?"
    
    return str(word)

print(myPutStr("Hello"))
print(myPutStr(22))

#--------------2--------------------------

def computeSurfaceM2(pieces):
    surface_totale = 0
    for longueur, largeur in pieces:
        surface_totale += longueur * largeur
    return surface_totale

pieces = [ (5, 4),  (3, 3),  (2, 2) ]

surface_totale = computeSurfaceM2(pieces)
print(f"Votre surface totale est de {surface_totale} m².")

#--------------3--------------------------

age=int(input("Donnez votre age : "))
def detectMyAgeByNight(age):
    if age >= 18:
        return f'Vous pouvez entrer vous êtes majeur vous avez {age} ans'
    return f"Vous ne pouvez pas entrer vous n'êtes pas majeur vous avez {age} ans"

print(detectMyAgeByNight(age))

#--------------4--------------------------

 
#--------------5--------------------------

import datetime
import time

def horloge():
    while True:
        now = datetime.datetime.now()
        heure_minute = now.strftime("%H:%M:%S")
        print("\r" + heure_minute, end="", flush=True)
        time.sleep(1)


horloge()
#--------------6--------------------------

def is_palindrome(s):
    
    s = s.lower()
    
    s = s.replace(" ", "")
    
    return s == s[::-1]


print(is_palindrome("radar"))  
print(is_palindrome("hello"))  
#--------------7--------------------------
def validMyInternationalPhone(phone_number):
   
    phone_number = ''.join(filter(str.isdigit, phone_number))
    
    
    if phone_number.startswith("33") and len(phone_number) == 11:
        print("Code pays Français")
        return True
    elif phone_number.startswith("1") and len(phone_number) == 11:
        print("Code pays Américain")
        return True
    else:
        print("Code pays non pris en charge")
        return False


print(validMyInternationalPhone("+33123456789"))  
print(validMyInternationalPhone("+11234567890"))  
print(validMyInternationalPhone("+441234567890")) 
  
#--------------8--------------------------
def fibonacci(n, a=1, b=1, seq=None):
    if seq is None:
        seq = [a, b]
    if len(seq) >= n:
        return seq[:n]
    seq.append(seq[-1] + seq[-2])
    return fibonacci(n, a, b, seq)


print(fibonacci(5))
print(fibonacci(10)) 
print(fibonacci(0))  
print(fibonacci(1))  