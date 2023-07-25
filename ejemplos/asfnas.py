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

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour ", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_mostrar_on_click(self):
       '''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        respuesta = "s"
        
        votos_maximo = 0
        bandera_max = False

        votos_minimo = 0
        bandera_min = False

        acumulador_edad = 0
        contador_edad = 0

        acumulador_votos = 0

        while respuesta == "s":

            nombre = prompt("UTN", "Ingrese el nombre del candidato")
            while len(nombre) < 3 or nombre.isalpha() == False:
                nombre = prompt("Error", "Ingrese el nombre del candidato")

            edad = int(prompt("UTN", "Ingrese la edad del candidato"))
            while edad < 24:
                edad = int(prompt("Error", "Su candidato no puede tener menos de 25"))
            
            votos = int(prompt("UTN", "Ingrese la cantidad de votos"))
            while votos < 0:
                votos = int(prompt("Error", "La cantidad de votos debe de ser mayor 0"))
                
            ############################################
            # a. nombre del candidato con más votos
            if votos > votos_maximo or bandera_maximo == False:
                votos_maximo = votos
                nombre_maximo = nombre
                bandera_maximo = True
            ###########################################
            # b. nombre y edad del candidato con menos votos
            if votos < votos_minimo or bandera_minimo == False:
                votos_minimo = votos
                nombre_minimo = nombre
                edad_minimo = edad
                bandera_minimo = True

            if edad > 0:
                acumulador_edad += edad
                contador_edad += 1
            
            acumulador_votos += votos
            respuesta = prompt("UTN", "Desea seguir?")

        ##########################################
        # c. el promedio de edades de los candidatos
        promedio_edad = acumulador_edad / contador_edad 
        ##########################################
        print("UTN", f"A- El nombre del candidato con mas votos es {nombre_maximo} con: {votos_maximo}.")
        print("UTN", f"B- El candidato con menos votos es {nombre_minimo} de una edad de {edad_minimo} con {votos_minimo} votos.")
        print("UTN", f"C- El promedio de la edades de los candidatos es de: {promedio_edad}")
        print("UTN", f"D- El total de votos emitidos es de {acumulador_votos}")
        
        



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
    #< > 




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()