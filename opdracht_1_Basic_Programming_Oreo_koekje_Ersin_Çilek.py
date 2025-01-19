# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:26:32 2024

@author: ecgam
"""
# voedingswaarden oreo 2-pack
cal = 210
vet = 10.5
kolhy = 27
eiwit = 2


# Voedingswaarden per koekje
calorieen_per_koekje = cal / 2
koolhydraten_per_koekje = kolhy / 2
vetten_per_koekje = vet / 2
eiwitten_per_koekje = eiwit / 2


#code om aantal gegeten koekjes in te vullen.
while True:
    aantal_koekjes = input("hoeveel koekjes heb je gegeten? ")
    try:
        aantal_koekjes = int(aantal_koekjes) #Try converting the input to integer
        break # Exit loop if succesfull
    except ValueError:
        print("Ongeldige invoer. Voer een geldig getal in.") # Handle invalid input

# Totaal aantal gegeten calorieën (ChatGPT gebruikt als hulp middel)
Tot_Cal = float(aantal_koekjes * calorieen_per_koekje)
Tot_Kolhy = float(aantal_koekjes) * koolhydraten_per_koekje
Tot_Vet = float(aantal_koekjes) * vetten_per_koekje
Tot_Eiwit = float(aantal_koekjes) * eiwitten_per_koekje


if Tot_Cal < 750:
    print("Je hebt", Tot_Cal, "calorieën", Tot_Kolhy, "g koolhydraten,", Tot_Vet, "g vetten en", Tot_Eiwit, "g eiwitten op.")
else: 
    print("Je hebt", Tot_Cal, "calorieën", Tot_Kolhy, "g koolhydraten,", Tot_Vet, "g vetten en", Tot_Eiwit, "g eiwitten op.")
    print("Je hebt meer dan 750 calorieën op, stop met het eten van deze koekjes")