# -*- coding: utf-8 -*-
from ArbolBinario import arbolBinario
from flask import Flask, flash, redirect, render_template, request, url_for
from NodoArbol import nodoArbol
nodo = nodoArbol()
arbol = arbolBinario()
arbol.Agregar("boris")
#arbol.Agregar("kevin")
#arbol.Agregar("alan")
#arbol.Agregar("leo")
#arbol.Agregar("fer")
#arbol.mostrar_en_orden(arbol.raiz)
#print("\n")
#arbol.mostrar_post_orden(arbol.raiz)
#print("\n")
#arbol.mostrar_pre_orden(arbol.raiz)


app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None

   if request.method == 'POST':
      if request.form['username'] != arbol.raiz.nombre or \
         request.form['password'] != "123":
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index'))
			
   return render_template('login.html', error = error)

if __name__ == "__main__":
   app.run(host = '0.0.0.0', port = 80, debug = True)






