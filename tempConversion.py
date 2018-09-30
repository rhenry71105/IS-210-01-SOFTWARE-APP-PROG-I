#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
#

def welcomeMessage():
    global user_choice
    print("""\
        Welcome To Temprature Conversion Menu
[!] Please Choice an Option:
            1. Celsius to Fahrenheit
            2. Celsius to Kelvin
            3. Fahrenheit to Celsius
            4. Fahrenheit to Kelvin
            5. Kelvin to Celsius
            6. Kelvin to Fahrenheit
[*] Type 'quit' exit the program.
    """)
    user_choice = input("[!] Make a Choice: ")



def celsiusToFahrenheit():
    global temp
    print("[+] You've Choosen: \n\t\t1. Celsius to Fahrenheit")
    temp = input("[!] Enter Temprature In Celsius: ")

def celsiusToKelvin():
    global temp
    print("[+] You've Choosen: \n\t\t2. Celsius to Kelvin")
    temp = input("[!] Enter Temprature In Celsius: ")

def fahrenheitToCelsius():
    global temp
    print("[+] You've Choosen: \n\t\t3. Fahrenheit to Celsius")
    temp = input("[!] Enter Temprature In Fahrenheit: ")

def fahrenheitToKelvin():
    global temp
    print("[+] You've Choosen: \n\t\t4. Fahrenheit to Kelvin")
    temp = input("[!] Enter Temprature In Fahrenheit: ")

def kelvinToCelsius():
    global temp
    print("[+] You've Choosen: \n\t\t5. Kelvin To Celsius")
    temp = input("[!] Enter Temprature In Kelvin: ")

def CelsiusToKelvin():
    global temp
    print("[+] You've Choosen: \n\t\t5. Celsius To Kelvin")
    temp = input("[!] Enter Temprature In Celsius: ")

def makeConversion():
    if user_choice == 1:
        celsiusToFahrenheit()
        tempCalculation = (1.8 * temp) + 32
        print("%s Celsius is Equal To %s Fahrenheit" % (temp, tempCalculation))
    elif user_choice == 2:
        celsiusToKelvin()
        tempCalculation = (temp + 273)
        print("%s Celsius is Equal To %s Kelvin" % (temp, tempCalculation))
    elif user_choice == 3:
        fahrenheitToCelsius()
        tempCalculation = (temp - 32) *(5/9)
        print("%s Fahrenheit is Equal To %s Celsius" % (temp, tempCalculation))
    elif user_choice == 4:
        fahrenheitToKelvin()
        tempCalculation = (5/9 * (temp - 32) + 273)
        print("%s Fahrenheit is Equal To %s Kelvin" % (temp, tempCalculation))
    elif user_choice == 5:
        kelvinToCelsius()
        tempCalculation = (temp - 273)
        print("%s Kelvin is Equal To %s Celsius" % (temp, tempCalculation))
    elif user_choice == 6:
        CelsiusToKelvin()
        tempCalculation = ((temp - 273) * 1.8 ) + 32
        print("%s Celsius is Equal To %s Kelvin" % (temp, tempCalculation))
    elif user_choice == "quit":
        exit()

welcomeMessage()
makeConversion()
