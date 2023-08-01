import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

# Se programo un evento exclusivo para Argentina "Lollapalooza ARG" se requiere registrar los datos de las personas que ingresan, para ello es necesario:

# Nacionalidad (Argentina)
# Nombre (Como figura en el DNI)
# Apellido (Como figura en el DNI)
# Edad (Entre 13 y 70 años)
# Cantidad de dias que ingresera al evento ("1","2","3")
# Los dias que ingresa al evento ("Viernes","Sabado","Domingo")

# Informar:
# 1) El nombre de la persona con apellido mas largo
# 2) Cantidad de personas menores de edad
# 3) Nombre/s de la/s persona/s que compro una entrada para los dias "Viernes" y "Domingo" 
# 4) Nombre y edad de la persona mas adulta que compro una entrada para el dia "Sabado"
# 5) Promedio de las personas que tienen entre 20 y 35 años
# 6) Calcular cual fue el dia al que mas gente acudio


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.nombres = []
        self.apellidos = []
        self.edades = []
        self.cantidad_dias = []
        self.dias = [] 


    def btn_mostrar_on_click(self):
        pass


    def btn_cargar_on_click(self):
        pass





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()