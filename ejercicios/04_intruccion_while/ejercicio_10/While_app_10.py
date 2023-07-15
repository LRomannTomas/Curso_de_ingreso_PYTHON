import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        cantidad_positivos = 0
        suma_positivos = 0
        cantidad_negativos = 0
        suma_negativos = 0
        cantidad_ceros = 0
        diferencia = 0

        while True:
            numero = prompt("UTN","Ingrese un numero: ")
            if numero == None:
                break
            numero = int(numero)
            if numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
            elif numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            else:
                cantidad_ceros += 1
        
        if cantidad_positivos > cantidad_negativos:
            diferencia = cantidad_positivos - cantidad_negativos
        if cantidad_negativos > cantidad_positivos:
            diferencia = cantidad_negativos - cantidad_positivos

        alert("UTN",f"""
            La suma de los numeros positivos es {suma_positivos}
            La suma de los numeros negativos es {suma_negativos}
            La cantidad de numeros positivos ingresados es {cantidad_positivos}
            La cantidad de numeros negativos ingresados es {cantidad_negativos}
            La cantidad de ceros ingresados es {cantidad_ceros}
            La diferencia entre la cantidad de numeros + y - es {diferencia}""")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
