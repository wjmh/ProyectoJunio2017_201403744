# -*- coding: utf-8 -*-
class nodoArbol():

    def __init__(self, nombre = None, password = None, login = None,padre = None, raiz = False, der = False, izq = False):
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.password = password
        self.login = login
        self.padre = padre
        self.raiz = raiz
        self.izq = izq
        self.der = der
