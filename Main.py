import gi
import MetodosAMas
import sqlite3
import BasePro, BBDD, BDComidas
import time

from gi.overrides import Gdk
gi.require_version('Gtk','3.0')
from gi.repository import Gtk



class programa():
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('restaurante.glade')





     #OBJETOS
        self.vtnprincipal = b.get_object('vtnprincipal')
        self.btnEntrar = b.get_object('btnEntrar')
        self.txtCamarero = b.get_object('txtCamarero')
        self.txtContra = b.get_object('txtContra')
        self.vtnMesas = b.get_object('vtnMesas')
        #VENTANA PARA SELECCIONAR EL MENU Y MAS
        self.vtnSeleccion = b.get_object('vtnSeleccion')
        self.cbbedidas = b.get_object('cbbedidas')
        self.cbentrantes = b.get_object('cbentrantes')
        self.cbplato = b.get_object('cbplato')
        self.cbpostre = b.get_object('cbpostre')
        self.treecomida = b.get_object('treecomida')
        self.listServiciouni = b.get_object('listServiciouni')
        #VENTANA PARA SELECCIONAR LA MESA
        self.btnmesa1 = b.get_object('btnmesa1')
        self.btnmesa2 = b.get_object('btnmesa2')
        self.btnmesa3 = b.get_object('btnmesa3')
        self.btnmesa4 = b.get_object('btnmesa4')
        self.btnmesa5 = b.get_object('btnmesa5')
        self.btnmesa6 = b.get_object('btnmesa6')
        self.btnmesa7 = b.get_object('btnmesa7')
        self.btnmesa8 = b.get_object('btnmesa8')
        #DATOS Y VENTANA DEL CLIENTE
        self.lbldni = b.get_object('lbldni')
        self.lblapellidos = b.get_object('lblapellidos')
        self.lblnombre = b.get_object('lblnombre')
        self.lbldireccion = b.get_object('lbldireccion')
        self.lblprovincia = b.get_object('lblprovincia')
        self.lblciudad = b.get_object('lblciudad')
        self.btnEscribir = b.get_object('btnEscribir')
        self.txtdni = b.get_object('txtdni')
        self.txtapellidos = b.get_object('txtapellidos')
        self.txtnombre = b.get_object('txtnombre')
        self.txtdireccion = b.get_object('txtdireccion')
        self.txtprovincia = b.get_object('txtprovincia')
        self.txtciudad = b.get_object('txtciudad')
        self.btnAnhadiruser = b.get_object('btnAnhadiruser')
        #VENTANA PARA ANYADIR DATOS
        self.vtnDatos = b.get_object('vtnDatos')
        self.cmbciu = b.get_object('cmbciu')
        self.cmbpro = b.get_object('cmbpro')
        self.listprovincias = b.get_object('listprovincias')
        self.listciudad = b.get_object('listciudad')
        #VENTANA DE INFORMACION
        self.infofactura = b.get_object('infofactura')
        self.infocamarero = b.get_object('infocamarero')
        self.infomesa = b.get_object('infomesa')
        self.infofecha = b.get_object('infofecha')
        #VENTANA EMERGENTES
        self.vtnemer = b.get_object('vtnemer')



        dic={'on_vtnprincipal_destoy': self.salir,
             'on_btnEscribir_clicked':self.abrirCliente,
             'on_btnAnhadiruser_clicked':self.abrirVentanaDatos,
             'on_cmbpro_changed': self.localidades,
             'on_btnEntrar_clicked': self.entrarCamarero,
             'on_btnmesa1_clicked': self.mesa1,
             'on_btnmesa2_clicked': self.mesa2,
             'on_btnmesa3_clicked': self.mesa3,
             'on_btnmesa4_clicked': self.mesa4,
             'on_btnmesa5_clicked': self.mesa5,
             'on_btnmesa6_clicked': self.mesa6,
             'on_btnmesa7_clicked': self.mesa7,
             'on_btnmesa8_clicked': self.mesa8,
             'on_pass_clicked': self.hide,
             'on_pass_released': self.nohide,
             'on_btnAnhadir_clicked': self.comidas,

             }

        b.connect_signals(dic)
        self.vtnprincipal.show()
        self.vtnSeleccion.maximize()
        BasePro.cargarcmbprov(self.listprovincias)
        #BasePro.cargarcmbprov2(self.listciudad)
        self.vtnprincipal.connect('delete-event', lambda w, e: w.hide() or True)
        self.vtnMesas.connect('delete-event', lambda w, e: w.hide() or True)
        self.vtnSeleccion.connect('delete-event', lambda w, e: w.hide() or True)
        self.vtnDatos.connect('delete-event', lambda w, e: w.hide() or True)
        self.vtnprincipal.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, .7, 9, 1))


    def salir(self, widget):
        Gtk.main_quit()


    def abrirCliente(self,widget):
        self.vtnDatos.show()

    def abrirVentanaDatos(self,widget):
        self.vtnDatos.show()

    def hide(self,widget):
            self.txtContra.set_visibility(True)

    def nohide(self,widget):
            self.txtContra.set_visibility(False)


    def entrarCamarero(self,widget):
        try:
            patata = 0
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            patata = BBDD.usuario(patata, username, password)
            if patata == 1:
                self.vtnMesas.show()
        except sqlite3.OperationalError as e:
            print("error")

    def mesacamarero(self):
        self.vtnemer.show()



    def mesa1(self,widget):

        idm = 1
        result = BBDD.mesaid(str(idm))
        if(result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni= '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni,cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamarero(self)

    def mesa2(self,widget):
        idm = 2
        result = BBDD.mesaid(str(idm))
        if (result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni = '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni, cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamamero(self)

    def mesa3(self,widget):
        idm = 3
        result = BBDD.mesaid(str(idm))
        if (result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni = '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni, cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamamero()

    def mesa4(self,widget):
        idm = 4
        result = BBDD.mesaid(str(idm))
        if (result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni = '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni, cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamamero()

    def mesa5(self,widget):
        idm = 5
        result = BBDD.mesaid(str(idm))
        if (result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni = '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni, cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamamero()

    def mesa6(self,widget):
        idm = 6
        result = BBDD.mesaid(str(idm))
        if (result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni = '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni, cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamamero()

    def mesa7(self,widget):
        idm = 7
        result = BBDD.mesaid(str(idm))
        if (result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni = '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni, cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamamero()

    def mesa8(self,widget):
        idm = 8
        result = BBDD.mesaid(str(idm))
        if (result == 0):
            username = self.txtCamarero.get_text()
            password = self.txtContra.get_text()

            username = username.capitalize()

            dni = '00000000A'
            fecha = time.strftime("%H:%M:%S")
            cc = BBDD.contra(username, password)
            print(cc)
            pagada = 0
            fila = (dni, cc, idm, fecha, pagada)
            BBDD.altafactura(fila)
            print("pasó el alta de factura")
            BBDD.mesaoc(idm)
            self.vtnSeleccion.show()
            self.infofecha.set_text(fecha)
            self.infocamarero.set_text(str(cc))
            self.infomesa.set_text(str(idm))
            fila2 = (idm, pagada)
            idfact = BBDD.idfact(fila2)
            self.infofactura.set_text(str(idfact))
        else:
            self.mesacamamero()


   # def insertarDatosCliente(self,widget):
    #    dni = self.txtdni.get_text()
    #    apellidos = self.txtapellidos.get_text()
    #   nombre = self.txtnombre.get_text()
    #    direccion =self.txtdireccion.get_text()
    #    provincia = self.txtprovincia.get_text()
    #    ciudad = self.txtciudad.get_text()
    #
    #    b = MetodosAMas.validar1(dni)
    #
    #   if dni != "" and apellidos != :


    def localidades(self,widget):
        var = self.cmbpro.get_active()
        BasePro.municipios(self.listciudad,var)


    def comidas(self,widget):
        if self.cbbedidas.get_active_text() == "NADA":
            self.bebidas = "NADA"
        elif self.cbbedidas.get_active_text() == "Agua":
            self.bebidas = "Agua"
        elif self.cbbedidas.get_active_text() == "Vino":
            self.bebidas = "Vino"
        elif self.cbbedidas.get_active_text() == "CocaCola":
            self.bebidas = "CocaCola"
        elif self.cbbedidas.get_active_text() == "Kas":
            self.bebidas = "Kas"
        elif self.cbbedidas.get_active_text() == "Sidra":
            self.bebidas = "Sidra"
        elif self.cbbedidas.get_active_text() == "Pocima de la casa":
            self.bebidas = "Pocima de la casa"

        if (self.bebidas != "NADA"):
            alim = self.bebidas
            co = BBDD.comprobarComida(alim)
            print (co)
            idfact = self.infofactura.get_text()
            print("ahora se pinta el id")
            print(idfact)
            cant = 1

            self.fila = (str(idfact),str(co), cant, alim)
            print(self.fila)
            BBDD.altacomida(self.fila)
            BBDD.cargacomida(self.treecomida, self.listServiciouni, idfact)
            BBDD.cargacomidatabla(self.listServiciouni)

        if self.cbentrantes.get_active_text() == "NADA":
            self.entrantes = "NADA"
        elif self.cbentrantes.get_active_text() == "Croquetas":
            self.entrantes = "Croquetas"
        elif self.cbentrantes.get_active_text() == "Calamares":
            self.entrantes = "Calamares"
        elif self.cbentrantes.get_active_text() == "Empanadillas":
            self.entrantes = "Empanadillas"
        elif self.cbentrantes.get_active_text() == "Choricitos":
            self.entrantes = "Choricitos"
        elif self.cbentrantes.get_active_text() == "Pantumaca":
            self.entrantes = "Pantumaca"

        if (self.entrantes != "NADA"):
            alim = self.entrantes
            co = BBDD.comprobarComida(alim)
            print(co)
            idfact = self.infofactura.get_text()
            print("ahora se pinta el id")
            print(idfact)
            cant = 1

            self.fila = (str(idfact), str(co), cant, alim)
            print(self.fila)
            BBDD.altacomida(self.fila)
            BBDD.cargacomida(self.treecomida, self.listServiciouni, idfact)
            BBDD.cargacomidatabla(self.listServiciouni)

        if self.cbplato.get_active_text() == "NADA":
            self.plato = "NADA"
        elif self.cbplato.get_active_text() == "Spaguettis":
            self.plato = "Spaguettis"
        elif self.cbplato.get_active_text() == "Macarrones":
            self.plato = "Macarrones"
        elif self.cbplato.get_active_text() == "Pizza 3 vientos":
            self.plato = "Pizza 3 vientos"
        elif self.cbplato.get_active_text() == "Jamon Asado con queso":
            self.plato = "Jamon Asado con queso"
        elif self.cbplato.get_active_text() == "Pollo al pil pil":
            self.plato = "Pollo al pil pil"
        elif self.cbplato.get_active_text() == "El gran choripan":
            self.plato = "El gran choripan"
        elif self.cbplato.get_active_text() == "Shakshuka con chorizo o merguez":
            self.plato = "Shakshuka con chorizo o merguez"
        elif self.cbplato.get_active_text() == "Chuletas de cerdo con manzanas a la provenzal":
            self.plato = "Chuletas de cerdo con manzanas a la provenzal"
        elif self.cbplato.get_active_text() == "Mejillones al vino blanco":
            self.plato = "Mejillones al vino blanco"
        elif self.cbplato.get_active_text() == "Pescado marinado en salsa de naranja agria":
            self.plato = "Pescado marinado en salsa de naranja agria"
        elif self.cbplato.get_active_text() == "Carne al Secreto":
            self.plato = "Carne al Secreto"

        if (self.plato != "NADA"):
            alim = self.plato
            co = BBDD.comprobarComida(alim)
            print(co)
            idfact = self.infofactura.get_text()
            print("ahora se pinta el id")
            print(idfact)
            cant = 1

            self.fila = (str(idfact), str(co), cant, alim)
            print(self.fila)
            BBDD.altacomida(self.fila)
            BBDD.cargacomida(self.treecomida, self.listServiciouni, idfact)
            BBDD.cargacomidatabla(self.listServiciouni)

        if self.cbpostre.get_active_text() == "NADA":
            self.postre = "NADA"
        elif self.cbpostre.get_active_text() == "Galletas Chocofun":
            self.postre = "Galletas Chocofun"
        elif self.cbpostre.get_active_text() == "Tarta de queso":
            self.postre = "Tarta de queso"
        elif self.cbpostre.get_active_text() == "Tarta de Abuela":
            self.postre = "Tarta de Abuela"
        elif self.cbpostre.get_active_text() == "Muerte por chocolate":
            self.postre = "Muerte por chocolate"
        elif self.cbpostre.get_active_text() == "Helado":
            self.postre = "Helado"
        elif self.cbpostre.get_active_text() == "Bizcocho vegano de almendra":
            self.postre = "Bizcocho vegano de almendra"

        if(self.postre != "NADA"):
            alim = self.postre
            co = BBDD.comprobarComida(alim)
            print(co)
            idfact = self.infofactura.get_text()
            print("ahora se pinta el id")
            print(idfact)
            cant = 1

            self.fila = (str(idfact), str(co), cant, alim)
            print(self.fila)
            BBDD.altacomida(self.fila)
            BBDD.cargacomida(self.treecomida, self.listServiciouni, idfact)
            BBDD.cargacomidatabla(self.listServiciouni)

        #datos.modificarreparaciones(self.factura, self.fila)
        #BBDD.cargacomida(self.treecomida, self.listServiciouni)
        #self.limpiarrepa()

#aquí lanzamos el programa
if __name__=='__main__':
    main = programa()
    Gtk.main()