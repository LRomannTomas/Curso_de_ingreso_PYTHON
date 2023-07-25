import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):    
        self.lista.clear()
        while True:
            numero = prompt("UTN","Ingrese un numero:")
            if numero == None:
                break
            numero = int(numero)
            self.lista.append(numero)

    
    def btn_mostrar_estadisticas_on_click(self):
        acumulador_negativos = 0
        contador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_ceros = 0
        minimo_negativo = None
        maximo_positivo = None
        for i in range(len(self.lista)):
            if self.lista[i] < 0:
                    acumulador_negativos += self.lista[i]
                    contador_negativos += 1
                    if minimo_negativo == None or self.lista[i] < minimo_negativo:
                        minimo_negativo = self.lista[i]
            else:
                if self.lista[i] > 0:
                    acumulador_positivos += self.lista[i]
                    contador_positivos += 1
                    if maximo_positivo == None or self.lista[i] > maximo_positivo:
                        maximo_positivo = self.lista[i]
                else:
                    contador_ceros += 1 

        promedio_negativos = 0
        if contador_negativos != 0:
            promedio_negativos = acumulador_negativos / contador_negativos
        
        alert("UTN",f"""
              La suma acumulada de los numeros negativos es: {acumulador_negativos}
              La suma acumulada de los numeros positivos es: {acumulador_positivos}
              La cantidad de numeros positivos es: {contador_positivos}
              La cantidad de numeros negativos es: {contador_negativos}
              La cantidad de ceros es: {contador_ceros}
              El menor numero negativo ingresado es: {minimo_negativo}
              El mayor numero positivo ingresado es: {maximo_positivo}
              El promedio de los numeros negativos es: {promedio_negativos:.2f}""")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
