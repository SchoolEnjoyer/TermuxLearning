import colorama
import random
import os
from time import sleep

colorama.init()

from colorama import Fore

os.system("clear")   

def start():
    var = random.choice("1234567890")

    if var == "1":
        print(var + " Przykład")
        print(Fore.YELLOW + "Iść" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("gehen / gegangen")
        input()
        os.system("clear")   
    elif var == "2":
        print(var + " Przykład")
        print(Fore.YELLOW + "Wygrywać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")     
        print("gewinnen / gewonnen")
        input()
        os.system("clear")      
    elif var == "3":
        print(var + " Przykład")
        print(Fore.YELLOW + "Podlewać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("gießen / gegossen")
        input()
        os.system("clear")           
    elif var == "4":
        print(var + " Przykład")
        print(Fore.YELLOW + "Mieć" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("haben / gehabt")
        input()
        os.system("clear")        
    elif var == "5":
        print(var + " Przykład")
        print(Fore.YELLOW + "Pomagać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("helfen / geholfen")
        input()
        os.system("clear")           
    elif var == "6":
        print(var + " Przykład")
        print(Fore.YELLOW + "Przychodzić" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("kommen / gekommen")
        input()
        os.system("clear")           
    elif var == "7":
        print(var + " Przykład")
        print(Fore.YELLOW + "Biegać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("laufen / gelaufen")
        input()
        os.system("clear")           
    elif var == "8":
        print(var + " Przykład") 
        print(Fore.YELLOW + "Czytać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("lesen / gelesen")
        input()
        os.system("clear")                 
    elif var == "9":
        print(var + " Przykład") 
        print(Fore.YELLOW + "Leżeć" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("liegen / gelegen")
        input()
        os.system("clear")                  
    elif var == "0":
        print(var + " Przykład") 
        print(Fore.YELLOW + "Brać / Wziąść" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("nehmen / genommen")
        input()
        os.system("clear")          


while True:
    start()
