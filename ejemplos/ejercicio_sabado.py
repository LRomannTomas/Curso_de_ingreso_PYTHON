import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_mostrar_on_click(self):
         
        cant_excursiones = int(prompt("UTN","Cuantas excursiones quiere realizar?"))
        contador = 0
        precio_max = None
        precio_min = None
        suma_importes = 0
        caminata = 0
        vehiculo = 0
        
        while cant_excursiones > contador:
            contador += 1
            if contador > 11:
                break
            importe = int(prompt("UTN",f"Cual es el importe de la excursion numero {contador}?: "))
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




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()