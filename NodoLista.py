# -*- coding: utf-8 -*-
class nodoLista():

    def __init__(self, nombre = None, tirosR = None, tirosA = None, tirosF = None, ganar = False, dano = None):
        self.nombre = nombre
        self.tirosR = tirosR
        self.tirosA = tirosA
        self.tirosF = tirosF
        self.ganar = None
        self.dano = dano
        self.ganar = ganar
        self.siguiente = None
        self.anterior = None