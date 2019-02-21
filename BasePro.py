import os
import sqlite3

try:

    bbdd = 'BasePro'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()

except sqlite3.OperationalError as e:
    print (e)

def cargarcmbprov(listprovincias):
    cur.execute("SELECT provincia FROM Provincias")
    lista = cur.fetchall()
    for row in lista:
        listprovincias.append(row)

def cargarcmbmunicipios(self, listado):
    listado = cur.municipios(self.item[0])


def selprov(self, widget):
    index = self.cmbprovincia.get_active()
    model = self.cmbprovincia.get_model()
    self.item = model[index]
    self.listmuni.clear()
    self.cargarcmbmunicipios()


def municipios(ciudad, prov):
    try:
        cur.execute("select municipio from municipios where provincia_id= '"+str(prov+1)+"'")
        ciudad.clear()
        listado = cur.fetchall()
        for row in listado:
            ciudad.append(row)

    except sqlite3.OperationalError as e:
        print (e)
        print("hubo un error en municipios")
        conex.rollback