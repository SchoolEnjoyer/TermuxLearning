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
        print(Fore.YELLOW + "Wstawać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("aufstehen / aufgestanden")
        input()
        os.system("clear")   
    elif var == "2":
        print(var + " Przykład")
        print(Fore.YELLOW + "Wydawać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")     
        print("ausgeben / ausgegeben")
        input()
        os.system("clear")      
    elif var == "3":
        print(var + " Przykład")
        print(Fore.YELLOW + "Otrzymać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("bekommen / bekommen")
        input()
        os.system("clear")           
    elif var == "4":
        print(var + " Przykład")
        print(Fore.YELLOW + "Zostać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("bleiben / geblieben")
        input()
        os.system("clear")        
    elif var == "5":
        print(var + " Przykład")
        print(Fore.YELLOW + "Myśleć" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("denken / gedacht")
        input()
        os.system("clear")           
    elif var == "6":
        print(var + " Przykład")
        print(Fore.YELLOW + "Jeść" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("essen / gegessen")
        input()
        os.system("clear")           
    elif var == "7":
        print(var + " Przykład")
        print(Fore.YELLOW + "Jechać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("fahren / gefahren")
        input()
        os.system("clear")           
    elif var == "8":
        print(var + " Przykład") 
        print(Fore.YELLOW + "Oglądać TV" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("fernsehen / ferngesehen")
        input()
        os.system("clear")                 
    elif var == "9":
        print(var + " Przykład") 
        print(Fore.YELLOW + "Znaleźć" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("finden / gefunden")
        input()
        os.system("clear")                  
    elif var == "0":
        print("10" + " Przykład") 
        print(Fore.YELLOW + "Dawać" + Fore.WHITE)
        input("1 forma: ")
        input("3 forma: ")
        print("geben / gegeben")
        input()
        os.system("clear")          


while True:
    start()
