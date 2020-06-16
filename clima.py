class Clima:
    def __init__(self):
        self.codigo= []
        self.ciudad = []
        self.temperatura_minima = []
        self.temperatura_maxima = []
        self.zona= []
        self.estado =[]

    def menu(self):
        opciones = """
        1.- Registar Departamento
        2.- Mostar todos los departamentos
        3.- Escriba la categoria deseada (LLANO-VALLE-ALTIPLANO)
        4.- Salir
        """
        print(opciones)
        seleccionar = int(input("Selecione una opcion: \n"))
        if (seleccionar == 1):
            print(self.agregarClima())
            self.menu()
        elif (seleccionar == 2):
            print(self.mostrarClima())
            print(self.volverMenu())
        elif (seleccionar == 3):
            print(self.climaBuscar())
            print(self.volverMenu())
        elif (seleccionar == 4):
            print("Transacciones realizadas exitosamente")
        else:
            print("selecione un a opcion del menu")
            self.menu()

    def agregarClima(self):
        codigo = input("Agrege el Codigo para el departamento: \n")
        ciudad = input("Digite la ciudad : \n")
        temperatura_minima = input("Temperatura minima: \n")
        temperatura_maxima = input("Temperatura maxima: \n")
        zona = input("Digite la zona: \n")
        print(self.guardarClima(codigo, ciudad, temperatura_minima, temperatura_maxima, zona))
        agregarOtro = input("Desea agregar otro departamento? y/n \n")
        if (agregarOtro == 'y' or agregarOtro == 'Y'):
            self.agregarClima()
        return "Se Agrego exitosamente"

    def guardarClima(self, codigo, ciudad, temperaturaMinima, temperaturaMaxima, zona):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.temperatura_minima.append(temperaturaMinima)
        self.temperatura_maxima.append(temperaturaMaxima)
        self.zona.append(zona)
        self.estado.append(1)
        return "Departamento {} agregado correctamente".format(codigo)

    def volverMenu(self):
        eleccion = input("Desea volver al menu: y/n  \n")
        if (eleccion == 'y' or eleccion == 'Y'):
            self.menu()
        return("-----Transacciones terminadas--------")


    def mostrarClima(self):
        if (self.codigo):
            for posicion in range(len(self.zona)):
                self.descripcion(posicion)
            return "Departamento cargado correctamente"
        else:
            return "Todavia no hay datos registrados"

    def descripcion(self, posicion):
        print("****DEPARTAMENTO {} ****".format(self.codigo[posicion]))
        print("ciudad {}".format(self.ciudad[posicion]))
        print("Temperatura minima  {}".format(self.temperatura_minima[posicion]))
        print("Temperatura maxima {}".format(self.temperatura_maxima[posicion]))
        print("zona {}".format(self.zona[posicion]))
        print("********************************************")
        pass

    def climaBuscar(self):
        zona=(input("Escriba la categoria deseada : \n"))
        return self.buscarCategoria(zona)

    def buscarCategoria(self, zona):
        encontrado = False
        for i in range(len(self.codigo)):
            if (self.zona[i] == zona):
                encontrado = True
                self.descripcion(i)
        if encontrado == False:
            print("No se escontraron resultados con la categoria {} ".format(zona))
        pass

clima = Clima()
clima.guardarClima("SANTA CRUZ", 1, 15, 29, "Llano")

clima.guardarClima("BENI", 2, 17, 31, "Llano")

clima.guardarClima("PANDO", 3, 18, 30, "Llano")

clima.guardarClima("LA PAZ", 4, 1, 13, "Altiplano")

clima.guardarClima("ORURO", 5, 2, 15, "Altiplano")

clima.guardarClima("POTOSI", 6, 2, 14, "Altiplano")

clima.guardarClima("CBBA", 7, 5, 18, "Valle")

clima.guardarClima("SUCRE", 8, 9, 23, "Valle")

clima.guardarClima("TARIJA", 9, 10, 25, "Valle")
clima.menu()