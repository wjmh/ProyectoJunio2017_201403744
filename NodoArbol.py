# -*- coding: utf-8 -*-
class nodoArbol:
    def __init__(self, nombre=None, password=None, login=False, padre=None, es_raiz=False, es_der=False, es_izq=False):
        self.nombre = nombre
        self.password = password
        self.login = login
        self.izq = None
        self.der = None
        self.padre = padre
        self.es_raiz = es_raiz
        self.es_izq = es_izq
        self.es_der = es_der
        self.apunt_lista = None

    def __str__(self):
        return "%s %s %s" %(self.nombre, self.password, self.login)