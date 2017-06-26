# -*- coding: utf-8 -*-
from ArbolBinario import arbolBinario

from flask import Flask, request

app = Flask("ejemploJunio")

@app.route('/metodo2',methods=['POST'])
def h():
    parametroPython = str(request.form['p'])
    parametroPython2 = str(request.form['pa'])
    return "parametro = " + parametroPython + parametroPython2

@app.route('/hola')
def he():
    return "hola Mundo"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

arbol = arbolBinario()
#arbol.Agregar("boris")
#arbol.Agregar("kevin")
#arbol.Agregar("alan")
#arbol.Agregar("leo")
#arbol.Agregar("fer")




#arbol.mostrar_en_orden(arbol.raiz)
#print("\n")
arbol.mostrar_post_orden(arbol.raiz)
#print("\n")
#arbol.mostrar_pre_orden(arbol.raiz)