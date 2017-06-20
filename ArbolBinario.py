# -*- coding: utf-8 -*-
from NodoArbol import nodoArbol

class arbolBinario():

    def __init__(self):
        self.raiz = None

    def Vacio(self):
        if(self.raiz == None):
            return True
        else:
            return False


    def Agregar(self, nombre):
        if (self.Vacio()):
            self.raiz = nodoArbol(nombre = nombre, raiz = True)
        else:
            NodoArbol = self.__getElemento(nombre)
            if (self.ConvertirAscii(nombre) <= NodoArbol.nombre):
                NodoArbol.izq = nodoArbol(nombre = nombre, padre = NodoArbol, izq = True)
            else:
                NodoArbol.der = nodoArbol(nombre = nombre, padre = NodoArbol, der = True)

    def __getElemento(self, nombre):
        aux = self.raiz
        while (aux != None):
            temp = aux
            if (self.ConvertirAscii(nombre) <= aux.nombre):
                aux = aux.izq
            else:
                aux = aux.der
        return temp


    def mostrar_en_Orden(self, elemento):
        if (elemento != None):
            self.mostrar_en_Orden(elemento.izq)
            print (elemento)
            self.mostrar_en_Orden(elemento.der)

    def mostrar_Pre_Orden(self, elemento):
        if (elemento != None):
            print(elemento)
            self.mostrar_en_Orden(elemento.izq)
            self.mostrar_en_Orden(elemento.der)

    def mostrar_Post_Orden(self, elemento):
        if (elemento != None):
            self.mostrar_en_Orden(elemento.izq)
            self.mostrar_en_Orden(elemento.der)
            print (elemento)

    def ConvertirAscii(self, nombre):
        [ord(c) for c in nombre]
        return c

