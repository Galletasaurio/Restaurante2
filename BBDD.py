import os
import sqlite3


try:
    bbdd = 'BaseDatos'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()

except sqlite3.OperationalError as e:
    print (e)


def cerrarconexion():
    try:
        conex.close()
        print ("Cerrando base de datos")

    except sqlite3.OperationalError as e:
        print (e)


def usuario(patata, username, password):
    try:

        if username != "" and password != "":
            cur.execute("select Pass  from Camarero where Nombre = '" + username + "';")
            l=cur.fetchall()
            print(l)
            cc=l[0][0]
            print("pass   ",password,"  passbd ",cc)
            try:
                print("llego a bbdd.usuario")
                if(password == cc):
                    patata = 1
                    conex.commit()
                    return patata
            except sqlite3.OperationalError as e:
                print(e)
        else:
            print ("falta dni")
    except sqlite3.OperationalError as e:
       print(e)
       conex.rollback()


def busqueda(username, password):
    try:
        cur.execute("select Nombre,pass  from Camarero where Nombre = '"+username+"' and Pass = '"+password+"';")
        conex.commit()
    except sqlite3.OperationalError as e:
        print (e)


def cargarlistcom(listServiciouni, idd):
    cur.execute("SELECT NombreServ,Cantidad FROM LineaFactura where IdFactura= '"+str(idd)+"'")
    lista = cur.fetchall()
    for row in lista:
        listServiciouni.append(row)


#ALTAS COMIDA!!!

def altacomida(fila):
    try:
        #cur.execute("select IdFactura from Factura where= '"+idfact+"'")
        print("llego hasta alta comida")
        print(fila)
        cur.execute("insert into LineaFactura(IdFactura,IdServicio,Cantidad,NombreServ) values(?,?,?,?)",fila)
        print("insertado")
        conex.commit()
    except sqlite3.OperationalError as e:
        print (e)


def idlinea(idfact, alim):
    try:
        cur.execute("select IdVenta from LineaFactura where IdFactura= "+str(idfact)+" and NombreServ= '"+alim+"'")
        l  = cur.fetchall()
        cc = l[0][0]
        conex.commit()
        return cc

    except sqlite3.OperationalError as e:
        print (e)



def cargacomida (treecomida,lista, idfact):
    print('llega a la carga en la tabla')
    cur.execute("SELECT NombreServ,Cantidad FROM LineaFactura where IdFactura= '"+str(idfact)+"'")
    rows = cur.fetchall()
    print("se pinta el rows")
    print(rows)
    lista.clear()
    print('ha pasado el select y el rows')
    for row in rows:
        print(row)
        altacomidavisu(treecomida, lista, row)


def comprobarComida(alim):
    cur.execute("select IdServicio from Servicios where Servicio= '"+alim+"'")
    l = cur.fetchall() #metemos la busqueda anterior en lç
    print("ahora se pinta l")
    print (l)
    cc = l[0]
    conex.commit()
    print(cc)
    return cc

#Visualizacion de la comida en la tabla
def altacomidavisu(treecomida, listServiciouni, fila):
    listServiciouni.append(fila) #PUEDE QUE HAYA QUE QUITAR EL 1
    treecomida.show()

def cargacomidatabla(listServiciouni):
    cur.execute("SELECT NombreServ, Cantidad FROM LineaFactura")
    lista = cur.fetchall()
    lista.clear()
    for row in lista:
        listServiciouni.append(row)


#ALTA FACTURA

def altafactura(fila):
    try:

        cur.execute("insert into Factura(Dnicli, IdCamarero, Idmesa, fecha, Pagada) values(?,?,?,?,?)",fila)
        conex.commit()
    except sqlite3.OperationalError as e:
        print (e)

def idfact(fila):
    try:
        cur.execute("select IdFactura from Factura where Pagada= '"+str(fila[1])+"' and idmesa= '"+str(fila[0])+"'")
        l = cur.fetchall()
        print(l)
        cc=l[0][0]
        print(cc)
        conex.commit()
        return cc

    except sqlite3.OperationalError as e:
        print (e)

def contra(username, password):
    try:

        if username != "" and password != "":
            cur.execute("select IdCamarero  from Camarero where (Nombre= '" + username + "') and (Pass='"+password+"');")
            l=cur.fetchall()
            print(l)
            cc=l[0][0]
            conex.commit()
            return cc

    except sqlite3.OperationalError as e:
       print(e)
       conex.rollback()

#MESA OCUPADA
def mesaoc(idm):
        try:
            cur.execute("update Mesa set Ocupada='" + str(1) +"' where IdMesa= '"+str(idm)+"'")
            conex.commit()
        except sqlite3.OperationalError as e:
            print(e)


def mesaid(idm):
    try:
        cur.execute("select Ocupada from Mesa where IdMesa= '"+idm+"'")
        l = cur.fetchall()
        cc = l[0][0]
        print(l)
        return cc
    except sqlite3.OperationalError as e:
        print(e)

