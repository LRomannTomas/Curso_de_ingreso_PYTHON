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
        x_mas_votado = None
        nombre_mas_votado = ""
        x_menos_votado = None
        nombre_menos_votado = ""
        bandera = True
        suma_edades = 0
        contador = 0
        acumulador_votos = 0
        while bandera == True:
            contador += 1
            nombre = prompt("UTN","Ingrese su nombre: ")
            while nombre == None or nombre == "" or nombre.isalpha() == False or len(nombre) < 3:
                nombre = prompt("UTN","Ingrese un nombre valido: ")
            
            edad = int(prompt("UTN","Ingrese la edad: "))
            while edad < 25:
                edad = int(prompt("UTN","Ingrese la edad (mayor a 25): "))
            suma_edades += edad

            votos = int(prompt("UTN","Cantidad de votos recibidos: "))
            while votos < 0:
                votos = int(prompt("UTN","Cantidad de votos recibidos (Ingrese un valor valido): "))

            acumulador_votos += votos

            while True:
                if x_mas_votado == None or votos > x_mas_votado:
                    x_mas_votado = votos
                    nombre_mas_votado = nombre
                if x_menos_votado == None or votos < x_menos_votado:
                    x_menos_votado = votos
                    nombre_menos_votado = nombre
                break

            
            salida = question("Pregunta","Desea continuar?")
            if salida == False:
                break
        
        promedio_edades = suma_edades / contador
        print(f"""
              El candidato mas votado fue: {nombre_mas_votado}
              El candidato menos votado fue: {nombre_menos_votado}
              El promedio de las edades de los candidatos es: {promedio_edades}
              La cantidad de votos totales es: {acumulador_votos}""")
                
                
            

            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
