# -*- coding: utf-8 -*-
from NodoLista import nodoLista

class listaDoble():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def Vacio(self):
        return self.primero == None

    def AgregarFin(self, nombre):
        if(self.Vacio()):
            self.primero = self.ultimo = nodoLista(nombre)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodoLista(nombre)
            self.ultimo.anterior = aux
        self.tamano += 1

    def AgregarInicio(self, nombre):
        if (self.Vacio()):
            self.primero = self.ultimo = nodoLista(nombre)
        else:
            aux = nodoLista(nombre)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.tamano += 1

    def Recorrer(self):
        aux = self.primero
        while (aux != None):
            print(aux.nombre)
            aux = aux.siguiente

    def Eliminar(self):
        if (self.Vacio()):
            print("La lista está vacía")
        elif (self.pririmero.siguguiente == None):
            self.primimero = self.ultltimo = None
            self.tamano = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.tamano -= 1


    def size(self):
        return self.tamano