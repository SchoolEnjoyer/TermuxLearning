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
        print(Fore.YELLOW + "Spać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("schlafen / geschlafen")
        input()
        os.system("clear")   
    elif var == "2":
        print(var + " Przykład")
        print(Fore.YELLOW + "Pisać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")     
        print("schreiben / geschrieben")
        input()
        os.system("clear")      
    elif var == "3":
        print(var + " Przykład")
        print(Fore.YELLOW + "Pływać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("schwimmen /  geschwommen")
        input()
        os.system("clear")           
    elif var == "4":
        print(var + " Przykład")
        print(Fore.YELLOW + "Patrzeć" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("sehen /  gesehen")
        input()
        os.system("clear")        
    elif var == "5":
        print(var + " Przykład")
        print(Fore.YELLOW + "Być" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("sein / gewesen")
        input()
        os.system("clear")           
    elif var == "6":
        print(var + " Przykład")
        print(Fore.YELLOW + "Śpiewać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("singen / gesungen")
        input()
        os.system("clear")           
    elif var == "7":
        print(var + " Przykład")
        print(Fore.YELLOW + "Siedzieć" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("sitzen / gesessen")
        input()
        os.system("clear")           
    elif var == "8":
        print(var + " Przykład") 
        print(Fore.YELLOW + "Skakać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("springen / gesprungen")
        input()
        os.system("clear")                 
    elif var == "9":
        print(var + " Przykład") 
        print(Fore.YELLOW + "Stać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("stehen / gestanden")
        input()
        os.system("clear")                  
    elif var == "0":
        print("10" + " Przykład") 
        print(Fore.YELLOW + "Nosić" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("tragen / getragen")
        input()
        os.system("clear")          


while True:
    start()
