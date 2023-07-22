import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

# Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
# Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está en la placa esta semana por haber ganado la inmunidad.
# Cada televidente que vota deberá ingresar:
# Nombre del votante
# Edad del votante (debe ser mayor a 13)
# Género del votante (Masculino, Femenino, Otro)
# El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:
# A. El promedio de edad de las votantes de género Femenino 
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
# C. Nombre del votante más joven qué votó a Gianni.
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que debe dejar la casa (El que tiene más votos)


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
        
        bandera = True
        lista_nombre_votante = []
        lista_edades = []
        lista_generos = []
        lista_nombre_participante = []
        
        while bandera == True:
            nombre_votante = prompt("UTN","Ingrese el nombre del votante")
            lista_nombre_votante.append(nombre_votante)

            edad_votante = int(prompt("UTN","Ingrese la dedad del votante"))
            while edad_votante < 13:
                edad_votante = int(prompt("UTN","Ingrese la dedad del votante"))
            lista_edades.append(edad_votante)

            genero_votante = prompt("UTN","Ingrese el genero del votante")
            while genero_votante != "Masculino" and genero_votante != "Femenino" and genero_votante != "Otro":
                genero_votante = prompt("UTN","Ingrese el genero del votante")
            lista_generos.append(genero_votante)
                
            nombre_participante = prompt("UTN","A quien quiere otorgar su voto?")
            while nombre_participante != "Giovanni" and nombre_participante != "Gianni" and nombre_participante != "Facundo":
                nombre_participante = prompt("UTN","A quien quiere otorgar su voto?")
            lista_nombre_participante.append(nombre_participante)

            respuesta = question("UTN","Desea continuar votando?")
            if respuesta == False:
                bandera = False
        
        acumulador_edad_femenino = 0
        contador_femenino = 0
        contador_punto_b = 0
        menor_edad_voto_gianni = None
        nombre_menor_edad_voto_gianni = "Nadie voto a Gianni"
        votos_gianni = 0
        votos_facundo = 0
        votos_giovanni = 0
        

        for gen in range(len(lista_generos)):
            if lista_generos[gen] == "Femenino":
                acumulador_edad_femenino += lista_edades[gen]
                contador_femenino += 1 
            if lista_generos[gen] == "Masculino" and (lista_edades[gen] >= 25 and lista_edades[gen] <= 40) and lista_nombre_participante[gen] != "Gianni":
                contador_punto_b += 1
            if lista_nombre_participante[gen] == "Gianni":
                votos_gianni += 1
                if menor_edad_voto_gianni == None or lista_edades[gen] < menor_edad_voto_gianni:
                    menor_edad_voto_gianni = lista_edades[gen]
                    nombre_menor_edad_voto_gianni = lista_nombre_votante[gen]
            else:
                if lista_nombre_participante[gen] == "Facundo":
                    votos_facundo += 1
                else:
                    votos_giovanni += 1


        promedio_edad_femenino = 0            
        if contador_femenino != 0:
            promedio_edad_femenino = acumulador_edad_femenino / contador_femenino

        
        suma_votos = votos_giovanni + votos_facundo + votos_gianni
        porcentaje_votos_gianni = votos_gianni * 100 / suma_votos
        porcentaje_votos_facundo = votos_facundo * 100 / suma_votos
        porcentaje_votos_giovanni = votos_giovanni * 100 / suma_votos
        
        mas_votado = None
        if votos_gianni > votos_facundo and votos_gianni > votos_giovanni:
            mas_votado = "Gianni"
        else:
            if votos_facundo > votos_gianni and votos_facundo > votos_giovanni:
                mas_votado = "Facundo"
            else:
                mas_votado = "Giovanni"
        
        alert("UTN",f"""
        El promedio de las edades de las votantes de genero 
        femenino es: {promedio_edad_femenino}
        La cantidad de personas de genero masculino entre 
        25 y 40 años que votaron a Giovanni o a Facundo es: {contador_punto_b}
        El nombre del votante mas joven que voto 
        a gianni es: {nombre_menor_edad_voto_gianni}
        El participante Gianni recibio un {porcentaje_votos_gianni}% de los votos)
        El participante Facundo recibio un {porcentaje_votos_facundo}% de los votos)
        El participante Giovanni recibio un {porcentaje_votos_giovanni}% de los votos
        El participante que debe dejar la casa es: {mas_votado}""")
              


        
                

                

        

# A. El promedio de edad de las votantes de género Femenino 
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
# C. Nombre del votante más joven qué votó a Gianni.
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que debe dejar la casa (El que tiene más votos)

        
        
            



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()