'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        
        contador = 0

        postulantes_ssr = 0

        menor_edad_jr = None
        nombre_menor_jr = ""

        cantidad_m = 0
        acumulador_edad_m = 0
        cantidad_f = 0
        acumulador_edad_f = 0
        cantidad_nb = 0
        acumulador_edad_nb = 0

        
        cant_python = 0
        cant_js = 0
        cant_asp_net = 0
        tecno_mas_elegida = ""


        for x in range(10):
        
            nombre = prompt("UTN","Ingrese el nombre: ")

            edad = int(prompt("UTN","Ingrese la edad: "))
            while edad < 18:
                edad = int(prompt("UTN","Ingrese la edad (Debe ser mayor a 17 años): "))


            genero = prompt("UTN","Ingrese el genero: (M, F o NB ")
            while genero != "M" and genero != "F" and genero != "NB":
                genero = prompt("UTN","Ingrese el genero: M, F o NB ")
        
            
            tecnologia = prompt("UTN","Ingrese la tecnologia: ")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("UTN","Ingrese la tecnologia:(PYTHON, JS o ASP.NET) ")
            
        
            puesto = prompt("UTN","Ingrese el puesto: ")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("UTN","Ingrese el puesto: (Jr, Ssr o Sr) ")


            contador += 1

            if (genero == "NB") and (tecnologia == "JS" or tecnologia == "ASP.NET") and (edad >= 25 and edad <= 40) and (puesto == "Ssr"):
                postulantes_ssr += 1
            

            if puesto == "Jr":
                if menor_edad_jr == None or edad < menor_edad_jr:
                    menor_edad_jr = edad
                    nombre_menor_jr = nombre
                
            if genero == "M":
                cantidad_m += 1
                acumulador_edad_m += edad
            else:
                if genero == "F":
                    cantidad_f += 1
                    acumulador_edad_f += edad
                else:
                    cantidad_nb += 1
                    acumulador_edad_nb+= edad
       
            if tecnologia == "PYTHON":
                cant_python += 1
            else:
                if tecnologia == "ASP.NET":
                    cant_asp_net += 1
                else:
                    cant_js += 1

        
        if cant_python >= cant_asp_net and cant_python >= cant_js:
            tecno_mas_elegida = "PYTHON"
        else:
            if cant_asp_net >= cant_python and cant_asp_net >= cant_js:
                tecno_mas_elegida = "ASP.NET"
            else:
                tecno_mas_elegida = "JS"

        
        promedio_m = 0
        promedio_f = 0
        promedio_nb = 0

        if cantidad_m != 0:
            promedio_m = acumulador_edad_m / cantidad_m
        if cantidad_f != 0:
            promedio_f = acumulador_edad_f / cantidad_f
        if cantidad_nb != 0:
            promedio_nb = acumulador_edad_nb / cantidad_nb
        

        porcentaje_m = 0
        porcentaje_f = 0
        porcentaje_nb = 0

        if cantidad_m != 0:
            porcentaje_m = cantidad_m * 100 / contador

        if cantidad_f != 0:
            porcentaje_f = cantidad_f * 100 / contador

        if cantidad_nb != 0:
            porcentaje_nb = cantidad_nb * 100 / contador

        print(f"""
                Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
                cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {postulantes_ssr}
                ------------------------------------------------------------------------------------------
                La persona de menor edad postulada para Jr es: {nombre_menor_jr}
                ------------------------------------------------------------------------------------------
                Promedio de las edades de las personas de genero Masculino: {promedio_m:.0f}
                Promedio de las edades de las personas de genero Femenino: {promedio_f:.0f}
                Promedio de las edades de las personas de genero No binario: {promedio_nb:.0f}
                ------------------------------------------------------------------------------------------
                La tecnologia mas elegida fue {tecno_mas_elegida}
                ------------------------------------------------------------------------------------------
                El porcentaje de las personas de genero Masculino es : {porcentaje_m}
                El porcentaje de las personas de genero Femenino es : {porcentaje_f}
                El porcentaje de las personas de genero No binario es : {porcentaje_nb}""")
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
