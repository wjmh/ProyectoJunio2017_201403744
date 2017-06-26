# -*- coding: utf-8 -*-
from NodoArbol import nodoArbol
class arbolBinario:

    def __init__(self):
        self.raiz = None


    def Vacio(self):
        if (self.raiz == None):
            return True
        else:
            return False

    def Agregar(self, nombre):
        if (self.Vacio()):
            self.raiz = nodoArbol(nombre = nombre, es_raiz = True)
        else:
            NodoArbol = self.getPos(nombre)
            if (self.ConvertirAscii(nombre) <= self.ConvertirAscii(NodoArbol.nombre)):
                NodoArbol.izq = nodoArbol(nombre = nombre, padre = NodoArbol, es_izq = True)
            else:
                NodoArbol.der = nodoArbol(nombre = nombre, padre = NodoArbol, es_der = True)

    def getPos(self, nombre):
        aux = self.raiz
        while aux:
            temp = aux
            if (self.ConvertirAscii(nombre) <= self.ConvertirAscii(aux.nombre)):
                aux = aux.izq
            else:
                aux = aux.der
        return temp

    def ConvertirAscii(self, string):
        elemento = []
        elemento = string
        for c in elemento[0]:
            return ord(c)

    def mostrar_en_orden(self, nodoArbol):
        if nodoArbol:
            self.mostrar_en_orden(nodoArbol.izq)
            print(nodoArbol.nombre)
            self.mostrar_en_orden(nodoArbol.der)

    def mostrar_pre_orden(self, NodoArbol):
        if NodoArbol:
            print(NodoArbol.nombre)
            self.mostrar_pre_orden(NodoArbol.izq)
            self.mostrar_pre_orden(NodoArbol.der)

    def mostrar_post_orden(self, NodoArbol):
        if NodoArbol:
            self.mostrar_post_orden(NodoArbol.izq)
            self.mostrar_post_orden(NodoArbol.der)
            print(NodoArbol.nombre)

    def Buscar(self, NodoArbol, nombre):
        if NodoArbol == None:
            return None
        else:
            if NodoArbol.nombre == nombre:
                return NodoArbol
            elif nombre <= NodoArbol.nombre:
                return self.Buscar(NodoArbol.izq, nombre)
            else:
                return self.Buscar(NodoArbol.der, nombre)
