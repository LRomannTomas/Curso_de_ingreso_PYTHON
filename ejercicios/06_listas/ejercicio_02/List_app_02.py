import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift.
Para ello, se solicitará al usuario la siguiente información al momento de comprar cada entrada:

Nombre del comprador
Edad (no menor a 16)
Género (Masculino, Femenino, Otro)
Tipo de entrada (General, Campo delantero, Platea)
Medio de pago (Crédito, Efectivo, Débito) 
Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, el medio de pago y su precio correspondiente.

Lista de precios: 
General: $16000
Campo: $25000
Platea: $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 


Al finalizar la venta de entradas, los organizadores quieren obtener la siguiente información:

A. Cantidad total de dinero recaudado por las ventas de entradas.
B. Cantidad de entradas vendidas para cada tipo.
C. Promedio de edad de las personas que compraron ubicación en Platea.
D. Nombre de la persona de mayor edad que compró una entrada de platea.
E. Porcentaje de entradas vendidas de tipo "general"
F. Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
G. Tipo de entradas más vendidas

1. Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo delantero".
2. Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
3. Calcula el número total de entradas compradas por personas mayores de 30 años y su precio promedio.
4. Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
5. Cual es el total de descuentos que aplicó la empresa
6. Cuál es el total de descuentos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito.
7. Encuentra el nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito.
8. Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
9. Calcula el monto total recaudado por la venta de entradas de tipo "General" y pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = []
        self.nombres = [
        "Juan", "María", "Luis", "Ana", "Carlos", "Jose", "Pedro", "Sofía", "Miguel", "Valentina",
        "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina", "Jorge", "Camila", "Ricardo", "Isabella",
        "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela", "Gustavo", "Carolina", "Emilio", "Antonella",
        "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina", "Raul", "Rocio", "Javier", "Marina",
        "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena", "Oscar", "Pilar", "Hugo", "Juana","Guillermo", 
        "Natalia", "Francisco", "Constanza", "Hector", "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
        "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia", "Camilo", "Teresa", "Samuel", "Rosa",
        "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano", "Silvia", "Nicolas", "Alicia",
        "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo", "Beatriz", "Elias", "Rita",
        "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes", "Gerardo", "Manuela", "Feliciano", "Marta"
    ]
        # Lista de edades (mayores o iguales a 16)
        self.edades = [
        25, 33, 20, 29, 50, 40, 22, 28, 35, 18,
        26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
        29, 17, 28, 34, 20, 25, 22, 33, 40, 16,
        19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
        35, 20, 23, 39, 30, 27, 22, 36, 28, 32,
        31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
        29, 22, 36, 30, 19, 25, 21, 38, 34, 17,
        32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
        31, 35, 24, 19, 28, 30, 26, 37, 33, 21,
        25, 29, 16, 38, 40, 50, 27, 30, 32, 24
    ]

    # Lista de géneros (Masculino, Femenino u Otro)
        self.generos = [
        "Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Masculino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
    ]
        
    # Lista de tipo de entrada (General, Campo delantero, Platea)
        self.tipo_entrada = [
        "General", "Campo delantero", "Platea", "General", "Platea", "General", "General", "Platea", "Campo delantero", "General",
        "Campo delantero", "Platea", "General", "General", "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "General", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero"
    ]

    # Lista de medio de pago (Credito, Debito, Efectivo)
        self.medio_pago = [
        "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito"
    ]


    # Lista de precios correspondientes a cada tipo de entrada
        self.precios = [16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000
    ]







    def btn_cargar_on_click(self):
         
        nombre = prompt("Nombre","Ingrese su nombre: ")


        edad = int(prompt("Edad","Ingrese su edad: "))
        while edad < 16:
            edad = int(prompt("Edad","Ingrese su edad: "))
            

        genero = prompt("Genero","Ingrese su genero: ")
        while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
            genero = prompt("Gener","Ingrese su genero: ")


        entrada = prompt("Entrada","Que tipo de entrada tenes?: ")
        while entrada != "General" and entrada != "Campo delantero" and entrada != "Platea":
            entrada = prompt("Entrada","Que tipo de entrada tenes?: ")


        medio_de_pago = prompt("Medio de pago","Que medio de pago desea utilizar?: ")
        while medio_de_pago != "Credito" and medio_de_pago != "Efectivo" and medio_de_pago != "Debito":
            medio_de_pago = prompt("Medio de pago","Que medio de pago desea utilizar?: ")
        

        for i in range(len(self.medio_pago)):
            descuento = 0
            if self.medio_pago[i] == "Credito":
                descuento = 0.2
            else:
                if self.medio_pago[i] == "Debito":
                    descuento = 0.15
            self.precios[i] = self.precios[i] - (self.precios[i] * descuento)
        

    def btn_mostrar_on_click(self):
        dinero_total = 0
        cant_general = 0
        cant_campo_delantero = 0
        cant_platea = 0
        edades_platea = 0
        mayor_edad_platea = None
        nombres_mayor_edad_platea = ""
        contador_general = 0
        mayor_masculino_general = None
        nombre_mayor_masculino_general = ""
        mensaje = ""

        for i in range(len(self.precios)):
            contador_general += 1
            dinero_total += self.precios[i]
            
            
            if self.tipo_entrada[i] == "General":
                cant_general += 1
                if self.generos[i] == "Masculino" and (mayor_masculino_general == None or self.edades[i] > mayor_masculino_general):
                    mayor_masculino_general = self.edades[i]
            else:
                if self.tipo_entrada[i] == "Campo delantero":
                    cant_campo_delantero += 1
                else:
                    cant_platea += 1
                    edades_platea += self.edades[i]
                    if mayor_edad_platea == None or self.edades[i] > mayor_edad_platea:
                        mayor_edad_platea = self.edades[i]

        mensaje += f"-El total recaudado de las ventas es: ${dinero_total}\n"
        mensaje += f"-La cantidad de entradas vendidas fue:\n"          
        mensaje += f"\t-> Entradas Platea: {cant_platea}\n"
        mensaje += f"\t-> Entradas General: {cant_general}\n"
        mensaje += f"\t-> Entradas Campo delantero: {cant_campo_delantero}\n"

        for i in range(len(self.edades)):
            if self.edades[i] == mayor_masculino_general and self.generos[i] == "Masculino" and self.tipo_entrada[i] == "General":
                nombre_mayor_masculino_general += f" |{self.nombres[i]}|"
            if self.edades[i] == mayor_edad_platea and self.tipo_entrada[i] == "Platea":
                nombres_mayor_edad_platea += f" |{self.nombres[i]}|"
            

        mensaje_promedio = ""
        if cant_platea != 0:
            promedio_edades_platea = edades_platea / cant_platea
            mensaje_promedio = f"-El promedio de las edades de las personas que compraron Platea es: {promedio_edades_platea:.2f}\n"
        else:
            mensaje_promedio = "-Ninguna persona compro una entrada Platea\n"

        mensaje += mensaje_promedio
        mensaje += f"-El/los nombre/s de la persona mayor en la Platea es/son:\n"
        mensaje += f"\t -> Nombres:{nombres_mayor_edad_platea}\n"

        porcentaje_entradas_general = cant_general * 100 / contador_general
        mensaje += f"-El porcentaje de las entradas vendidas para General es {porcentaje_entradas_general}\n"

        mensaje_entrada_mas_vendida = ""

        if cant_platea > cant_general and cant_platea > cant_campo_delantero:
            mensaje_entrada_mas_vendida += "-El tipo de entrada mas vendido es la entrada Platea\n"
        else:
            if cant_general > cant_campo_delantero:
                mensaje_entrada_mas_vendida += "-El tipo de entrada mas vendido es la entrada General\n"
            else:
                mensaje_entrada_mas_vendida += "-El tipo de entrada mas vendido es la entrada Campo delantero\n"
        
        mensaje += mensaje_entrada_mas_vendida

        # for i in range(len(self.medio_pago)):
        #     descuento = 0
        #     if self.medio_pago[i] == "Credito":
        #         descuento = 0.2
        #     else:
        #         if self.medio_pago[i] == "Debito":
        #             descuento = 0.15
        #     self.precios[i] = self.precios[i] - (self.precios[i] * descuento)
        #     dinero_total += self.precios[i]

        #Punto 1
        cant_masculinos_campo = 0
        cant_femeninos_campo = 0
        cant_otro_campo = 0
        mayor_genero_campo = None

        for i in range(len(self.tipo_entrada)):
            if self.tipo_entrada[i] == "Campo delantero":
                match self.generos[i]:
                    case "Masculino":
                        cant_masculinos_campo += 1
                    case "Femenino":
                        cant_femeninos_campo += 1
                    case _:
                        cant_otro_campo += 1


        if cant_masculinos_campo > cant_femeninos_campo and cant_masculinos_campo > cant_otro_campo:
            mayor_genero_campo = "-El genero que mas compro entradas para Campo delantero fue: Masculino\n"
        else:
            if cant_femeninos_campo > cant_otro_campo:
                mayor_genero_campo = "-El genero que mas compro entradas para Campo delantero fue: Femenino\n"
            else:
                mayor_genero_campo = "-El genero que mas compro entradas para Campo delantero fue: Otro\n"

        mensaje += mayor_genero_campo

        #Punto 2
        cant_general_credito = 0
        edades_general_credito = 0
        for i in range(len(self.tipo_entrada)):
            if self.tipo_entrada[i] == "General" and self.medio_pago[i] == "Credito":
                cant_general_credito += 1
                edades_general_credito += self.edades[i]
        mensaje += f"-La cantidad de personas que compraron entrada General con tarjeta de credito es {cant_general_credito}\n"
        
        if cant_general_credito != 0:
            promedio_general_credito = f"-El promedio de las edades de las personas que compraron entrada general con tarjeta de credito es: {(edades_general_credito / cant_general_credito):.2f}\n"
        else:
            promedio_general_credito = "-Nadie compro una entrada General con tarjeta de credito!\n"
        
        mensaje += promedio_general_credito

        #Punto 3
        cant_entradas_30 = 0
        dinero_total_entradas_30 = 0
        for i in range(len(self.edades)):
            if self.edades[i] > 30:
                cant_entradas_30 += 1
                dinero_total_entradas_30 += self.precios[i]
        
        promedio_total_entradas_30 = 0
        if cant_entradas_30 != 0:
            promedio_total_entradas_30 = f"-El promedio del dinero total gastado por las personas mayores a 30 años es: {(dinero_total_entradas_30 / cant_entradas_30):.2f}\n"
        else:
            promedio_total_entradas_30 = "-No ingresaron personas mayores a 29 años!\n"

        cant_entradas_30 = f"-La cantidad de entradas compradas por personas mayores a 30 años es: {cant_entradas_30}\n"
        mensaje += cant_entradas_30
        mensaje += promedio_total_entradas_30

        #Punto 4
        cant_platea_debito = 0
        for i in range(len(self.tipo_entrada)):
            if self.tipo_entrada[i] == "Platea" and self.medio_pago[i] == "Debito":
                cant_platea_debito += 1
        porcentaje_platea_debito = f"-El porcentaje de las personas que compraron una entrada para Platea con tarjeta de debito es: {(cant_platea_debito * 100 / contador_general)}%\n"
        mensaje += porcentaje_platea_debito

        #Punto 5
        total_precios_descuento = 0

        for i in range(len(self.medio_pago)):
            if self.medio_pago[i] == "Credito":
                total_precios_descuento += self.precios[i] * 0.2
            else:
                if self.medio_pago[i] == "Debito":
                    total_precios_descuento += self.precios[i] * 0.15

        mensaje += f"-El total de descuentos en pesos que aplicó la empresa es: {total_precios_descuento:.2f}\n"

        #Punto 6
        total_descuento_credito = 0
        for i in range(len(self.medio_pago)):
            if self.medio_pago[i] == "Credito":
                total_descuento_credito += (self.precios[i] * 0.2)
        
        mensaje += f"-El total de descuentos en pesos aplicados a tarjeta de credito es: {total_descuento_credito}\n"
        
        #Punto 7
        maximo_general_debito = None
        for i in range(len(self.tipo_entrada)):
            if self.tipo_entrada[i] == "General" and self.medio_pago[i] == "Debito":
                if maximo_general_debito == None or self.precios [i] > maximo_general_debito:
                    maximo_general_debito = self.precios[i]
                    
        nombres_general_debito = ""
        edades_general_debito = ""
        
        for i in range(len(self.tipo_entrada)):
            if self.tipo_entrada[i] == "General" and self.medio_pago[i] == "Debito":
                if self.precios[i] == maximo_general_debito:
                    nombres_general_debito += f"\t-> nombre/s: {self.nombres[i]}\n"
                    edades_general_debito += f"\t-> edad/es: {self.edades[i]}\n"
        
        mensaje += "-Las personas que mas pagaron por una entrada General con tarjeta de credito son:\n"
        mensaje += f"{nombres_general_debito}{edades_general_debito}"

        #Punto 8
        cant_platea_edad_prima = 0
        for indice in range(len(self.tipo_entrada)):
            divisores = 0
            if self.tipo_entrada[indice] == "Platea":
                for i in range(1,self.edades[indice] + 1):
                    if self.edades[indice] % i == 0:
                        divisores += 1
                if divisores == 2:
                    cant_platea_edad_prima += 1
        mensaje += f"-La cantidad de personas que compraron entrada en Platea y su edad es un numero primo es: {cant_platea_edad_prima} \n"
        
    
        #Punto 9
        total_general_tarjeta = 0
        
        for i in range(len(self.tipo_entrada)):
            if self.tipo_entrada[i] == "General":
                if self.medio_pago[i] == "Credito" and (self.edades[i] % 5 == 0):
                    total_general_tarjeta += self.precios[i] * 0.8
            
        mensaje += f"-El monto total de la venta de entradas General pagadas con tarjeta de credito por personas cuyas edades son múltiplos de 5 es: {total_general_tarjeta}"

        alert("mensaje",mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()