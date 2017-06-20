# -*- coding: utf-8 -*-
from ArbolBinario import arbolBinario
#from flask import Flask, request

#app = Flask("ejemploJunio")

#@app.route('/metodo2',methods=['POST'])
#def h():
    #parametroPython = str(request.form['p'])
    #parametroPython2 = str(request.form['pa'])
    #return "parametro = " + parametroPython, parametroPython2

#@app.route('/hola')
#def he():
    #return "hola Mundo"

#if __name__ == "__main__":
  #app.run(debug=True, host='0.0.0.0')
arbol = arbolBinario()

arbol.Agregar("william")
arbol.Agregar("rudy")
arbol.Agregar("fer")
arbol.Agregar("ricardo")
arbol.Agregar("gil")



arbol.mostrar_en_Orden(arbol.raiz)
arbol.mostrar_Pre_Orden(arbol.raiz)