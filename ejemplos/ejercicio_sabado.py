import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

# Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


# 1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

# 2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
# medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

# 3- Validar todos los datos.

# 4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.

# 5- Una vez ingresada la cantidad se debe pedir por cada excursión 
# el importe y el tipo de excursión (caminata  o vehículo). 
# informar cual es el precio más caro, el más barato y el promedio

# 6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour ", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_mostrar_on_click(self):
        
        nombre = prompt("UTN","Ingrese su nombre: ")
        while nombre == None or nombre.isalpha() == False or (len(nombre) < 3) or nombre == "":
            nombre = prompt("UTN","Ingrese un nombre valido: ")
        
        
        edad = prompt("UTN","Ingrese su edad: ")
        while edad == None or edad.isdigit() == False:
             edad = prompt("UTN","Ingrese una edad que sea valida: ")

        edad = int(edad)
        while edad > 150:
            edad = prompt("UTN","Ingrese una edad que sea valida: ")
            while edad == None or edad.isdigit() == False:
                edad = prompt("UTN","Ingrese una edad que sea valida: ")
            else:
                edad = int(edad)
                 

        genero = prompt("UTN","Ingrese su genero Masculino, Femenino, u Otro: ")
        while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
            genero = prompt("UTN","Ingrese su genero Masculino, Femenino, u Otro: ")

        alert("Datos",f"Usted es {nombre}, tiene {edad} años de edad y su genero es {genero}")

    
        altura = prompt("UTN","Ingrese su altura (En centimetros): ")
        while altura == None or altura.isdigit() == False:
            altura = prompt("UTN","Ingrese una altura que sea valida (En centimetros): ")

        altura = int(altura)
        while altura < 40 or altura > 300:
            altura = prompt("UTN","Ingrese una altura que sea valida (En centimetros): ")
            while altura == None or altura.isdigit() == False:
                altura = prompt("UTN","Ingrese una altura que sea valida (En centimetros): ")
            else:
                altura = int(altura)

        if altura < 140:
            alert("Mensaje","Es bajo")
        elif altura <= 170:
            alert("Mensaje","Es mediano")
        elif altura <= 190:
            alert("Mensaje","Es alto")
        else:
            alert("Mensaje","Es muy alto")
        
        cant_excursiones = prompt("UTN","Cuantas excursiones quiere realizar?")
        while cant_excursiones == None or cant_excursiones.isdigit() == False:
            cant_excursiones = prompt("UTN","Cuantas excursiones quiere realizar? (Ingrese un valor numerico)")
        
        cant_excursiones = int(cant_excursiones)
        while cant_excursiones > 11 or cant_excursiones < 0:
            cant_excursiones = prompt("UTN","Cuantas excursiones quiere realizar? (El maximo es 11)")
            while cant_excursiones == None or cant_excursiones.isdigit() == False:
                cant_excursiones = prompt("UTN","Cuantas excursiones quiere realizar? (Ingrese un valor numerico porfavor)")
            else:
                cant_excursiones =int(cant_excursiones)

        while cant_excursiones > 11:
            cant_excursiones = int(prompt("UTN","Cuantas excursiones quiere realizar? (El maximo es 11)"))

        contador = 0
        precio_max = None
        precio_min = None
        suma_importes = 0
        caminata = 0
        vehiculo = 0
        
        while cant_excursiones > contador:
            contador += 1
            importe = prompt("UTN",f"Cual es el importe de la excursion numero {contador}?: ")
            while importe == None or importe.isdigit() == False:
                importe = prompt("UTN",f"Cual es el importe de la excursion numero {contador}? (Ingrese un valor numerico): ")
            importe = float(importe)

            tipo_excursion = prompt("UTN","Que tipo de excursion es? (caminata o vehiculo)")
            while tipo_excursion != "caminata" and tipo_excursion != "vehiculo":
                tipo_excursion = prompt("UTN","Que tipo de excursion es? (caminata o vehiculo)")
            if tipo_excursion == "caminata":
                    caminata += 1
            if tipo_excursion == "vehiculo":
                    vehiculo += 1

            if precio_max == None or importe > precio_max:
                precio_max = importe
            if precio_min == None or importe < precio_min:
                precio_min = importe 

            suma_importes += importe

        promedio = suma_importes / cant_excursiones
        alert("UTN",f"El precio mas caro es {precio_max}")
        alert("UTN",f"El precio mas barato es {precio_min}")
        alert("UTN",f"El promedio de los precios es {promedio}")

        if caminata > vehiculo:
            alert("UTN","El tipo de excursion mas seleccionado fue caminata")
        elif vehiculo > caminata:
            alert("UTN","El tipo de excursion mas seleccionado fue vehiculo")
        else:
            alert("UTN","Las excursiones se seleccionaron la misma cantidad de veces")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()