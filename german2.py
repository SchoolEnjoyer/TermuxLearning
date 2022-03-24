import random
import os
from time import sleep

def start():
    var = random.choice("1234567890")

    if var == "1":
        print(var + " Przykład")
        print("Iść")
        input("1 forma: ")
        input("3 forma: ")
        print("gehen / gegangen")
        input()
        os.system("cls")
    elif var == "2":
        print(var + " Przykład")
        print("Wygrywać")
        input("1 forma: ")
        input("3 forma: ")     
        print("gewinnen / gewonnen")
        input()
        os.system("cls")     
    elif var == "3":
        print(var + " Przykład")
        print("Podlewać")
        input("1 forma: ")
        input("3 forma: ")
        print("gießen / gegossen")
        input()
        os.system("cls")          
    elif var == "4":
        print(var + " Przykład")
        print("Mieć")
        input("1 forma: ")
        input("3 forma: ")
        print("haben / gehabt")
        input()
        os.system("cls")          
    elif var == "5":
        print(var + " Przykład")
        print("Pomagać")
        input("1 forma: ")
        input("3 forma: ")
        print("helfen / geholfen")
        input()
        os.system("cls")          
    elif var == "6":
        print(var + " Przykład")
        print("Przychodzić")
        input("1 forma: ")
        input("3 forma: ")
        print("kommen / gekommen")
        input()
        os.system("cls")          
    elif var == "7":
        print(var + " Przykład")
        print("Biegać")
        input("1 forma: ")
        input("3 forma: ")
        print("laufen / gelaufen")
        input()
        os.system("cls")          
    elif var == "8":
        print(var + " Przykład") 
        print("Czytać")
        input("1 forma: ")
        input("3 forma: ")
        print("lesen / gelesen")
        input()
        os.system("cls")                 
    elif var == "9":
        print(var + " Przykład") 
        print("Leżeć")
        input("1 forma: ")
        input("3 forma: ")
        print("liegen / gelegen")
        input()
        os.system("cls")                 
    elif var == "0":
        print(var + " Przykład") 
        print("Brać / Wziąść")
        input("1 forma: ")
        input("3 forma: ")
        print("nehmen / genommen")
        input()
        os.system("cls")          


while True:
    start()