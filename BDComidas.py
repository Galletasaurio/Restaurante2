import os, BBDD
import sqlite3

try:

    bbdd = 'BDComidas'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()

except sqlite3.OperationalError as e:
    print (e)





def comprobarComida(fila):
    cur.execute("select Comida from Carta where Comida= '"+fila+"'")
    l = cur.fetchall() #metemos la busqueda anterior en lç
    print(l)
    if(l != ""):
        cur.execute("select Preciounidad from Carta where Comida= '"+fila+"'")
        d = cur.fetchall()
        print(d)
        fila = (l[0][0],d[0][0])
        print(fila)
        BBDD.altacomida(fila)