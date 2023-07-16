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
        tecnologias_elegidas = []
        cant_python = 0
        cant_js = 0
        cant_asp_net = 0
        tecno_mas_elegida = None

        while contador < 4:
            contador += 1

            tecnologia = prompt("UTN","Ingrese la tecnologia: ")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("UTN","Ingrese la tecnologia:(PYTHON, JS o ASP.NET) ")
            
            tecnologias_elegidas.append(tecnologia)

        for tipo in tecnologias_elegidas:
            if tipo == "PYTHON":
                cant_python += 1
            else:
                if tipo == "ASP.NET":
                    cant_asp_net += 1
                else:
                    cant_js += 1

        print(cant_python)
        print(cant_asp_net)
        print(cant_js)

        if cant_python > cant_asp_net and cant_python > cant_js:
            tecno_mas_elegida = "PYTHON"
        else:
            if cant_asp_net > cant_python and cant_asp_net > cant_js:
                tecno_mas_elegida = "ASP.NET"
            else:
                tecno_mas_elegida = "JS"

        print(tecno_mas_elegida)





























        # contador = 0
        # postulantes_ssr = 0
        # edades_masculino = []
        # suma_edades_masculino = 0
        # edades_femenino = []
        # suma_edades_femeninio = 0
        # edades_no_binario = []
        # suma_edades_no_binario = 0

        # edades_jr = []
        # nombre_menor_jr = ""


        # while contador < 10:
        #     contador += 1
        #     nombre = prompt("UTN","Ingrese el nombre: ")

        #     edad = int(prompt("UTN","Ingrese la edad: "))
        #     while edad < 18:
        #         edad = int(prompt("UTN","Ingrese la edad (Debe ser mayor a 17 años): "))

        #     genero = prompt("UTN","Ingrese el genero: (M, F o NB ")
        #     while genero != "M" and genero != "F" and genero != "NB":
        #         genero = prompt("UTN","Ingrese el genero: M, F o NB ")


        #     if genero == "M":
        #         edades_masculino.append(edad)
        #         suma_edades_masculino += edad
        #     else:
        #         if genero == "F":
        #             edades_femenino.append(edad)
        #             suma_edades_femeninio += edad
        #         else:
        #             edades_no_binario.append(edad)
        #             suma_edades_no_binario += edad
                    

        #     tecnologia = prompt("UTN","Ingrese la tecnologia: ")
        #     while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
        #         tecnologia = prompt("UTN","Ingrese la tecnologia:(PYTHON, JS o ASP.NET) ")

        #     puesto = prompt("UTN","Ingrese el puesto: ")
        #     while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
        #         puesto = prompt("UTN","Ingrese el puesto: (Jr, Ssr o Sr) ")

        #     if puesto == "Jr":
        #         edades_jr.append(edad)

        #     if (genero == "NB") and (tecnologia == "JS" or tecnologia == "ASP.NET") and (edad >= 25 and edad <= 40) and (puesto == "Ssr"):
        #         postulantes_ssr += 1
            
         
        # edad_jr_min = None
        # for min in edades_jr:
        #     if edad_jr_min == None or min < edad_jr_min:
        #         edad_jr_min = min
        #         nombre_menor_jr = nombre
            
            

        # print(f"""
        #         Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
        #         cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {postulantes_ssr}
        #         La persona de menor edad postulada para Jr es: {nombre_menor_jr}
        #         Promedio de las edades de las personas de genero Masculino: )
        #         Promedio de las edades de las personas de genero Femenino: )
        #         Promedio de las edades de las personas de genero No binario: """)
            



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
