import random
from random import randint

import self as self
import random


class Persona:
    __nombre = ""
    __edad = 0
    __dni = None
    __sexo = "m"
    __peso = 0.00
    __altura = 0.00


    def __init__(self, nombre, edad, sexo, peso, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = self.generarDNInumeros()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura


    def CalcularIMC(self, __peso, __altura):
        imc = (__peso / (__altura ** 2))
        print("IMC: ", imc)
        if imc < 18.5:
            return -1
            print("Tu peso esta por debajo de lo normal")
        elif imc > 18.5 or imc > 24.9:
            return 0
            print("Tu peso es ideal")
        elif imc > 25 or imc < 26.9:
            return 1
            print("Tu peso esta por encima de lo normal")



    def MayordeEdad(self, __edad):
        if bool(__edad < 18):
            return 1
            print("Eres menor de edad")
        if bool(__edad > 18):
            return 0
            print("Eres mayor de edad")

    def TipoSexo(sexo):
        if sexo != "M" or sexo != "H" or sexo != "m" or sexo != "h":
            return "M"

    def generarDNInumeros(self):
        numeros=0
        letra=""
        resto=0
        numeros=random.randint(00000000, 99999999)
        diccionario = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X",
                       11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L",
                       20: "C", 21: "K", 22: "E"}
        resto = (numeros%23)
        letra=diccionario[resto]
        dni=str(numeros) + letra
        return dni


    def toString(self):
        print(
            f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.generarDNInumeros()}, Sexo: {self.__sexo}, Peso: {self.__peso}, Altura: {self.__altura}")

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getDni(self):
        return self.__dni

    def getSexo(self):
        return self.__sexo

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura




print ("Introduce tu nombre: ")
nombre=input()

print ("Introduce tu edad: ")
edad=int(input())

print ("Introduce tu sexo: ")
sexo = Persona.TipoSexo(input())

print ("Introduce tu peso: ")
peso=float(input())

print ("Introduce tu altura: ")
altura=float(input())

p1=Persona(nombre, edad, sexo, peso, altura,)
print (f"Su nombre es {nombre}, tiene {edad} años, Genero: {sexo} su dni es: {p1.generarDNInumeros()}, su peso es {peso} kg, y su altura {altura} metros")
print (f"Su IMC es: {p1.CalcularIMC(p1.getAltura(), p1.getPeso())}")
print (f"Usted es: {p1.MayordeEdad(p1.getEdad())}")





