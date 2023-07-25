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
        postulantes_punto_a = 0

        nombre_menor_jr = ""
        edades_tecno_jr = None
       
        generos = []
        tecnologias_elegidas = []
        puestos = []

        cant_gen_m = 0
        cant_gen_f = 0
        cant_gen_nb = 0

        edades_gen_m = 0
        edades_gen_f = 0
        edades_gen_nb = 0

        cant_tec_python = 0
        cant_tec_js = 0
        cant_tec_asp_net = 0
        tecno_mas_elegida = "No hay postulantes para Jr"
        
       

        while contador < 4:
            contador += 1

            nombre = prompt("UTN","Ingrese el nombre: ")
            

            edad = int(prompt("UTN","Ingrese la edad: "))
            while edad < 18:
                edad = int(prompt("UTN","Ingrese la edad (Debe ser mayor a 17 años): "))


            genero = prompt("UTN","Ingrese el genero: (M, F o NB ")
            while genero != "M" and genero != "F" and genero != "NB":
                genero = prompt("UTN","Ingrese el genero: M, F o NB ")

            generos.append(genero)


            tecnologia = prompt("UTN","Ingrese la tecnologia: ")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("UTN","Ingrese la tecnologia:(PYTHON, JS o ASP.NET) ")
            
            tecnologias_elegidas.append(tecnologia)


            puesto = prompt("UTN","Ingrese el puesto: ")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("UTN","Ingrese el puesto: (Jr, Ssr o Sr) ")

            puestos.append(puesto)

            while genero == "M":
                edades_gen_m += edad
                break

            while genero == "F":
                edades_gen_f += edad
                break
            else:
                if genero == "NB":
                    edades_gen_nb += edad
                    while puesto == "Ssr" and (tecnologia == "ASP.NET" or tecnologia == "JS"):
                        postulantes_punto_a += 1
                        break
                    else:
                        break

        for tipo in generos:
            if tipo == "M":
                cant_gen_m += 1
            elif tipo == "F":
                cant_gen_f += 1
            else:
                cant_gen_nb += 1
                

        print(edades_gen_m)
        print(edades_gen_f)
        print(edades_gen_nb)
        print(cant_gen_m)
        print(cant_gen_f)
        print(cant_gen_nb)



        for tecno in tecnologias_elegidas:
            if tecno == "PYTHON":
                cant_tec_python += 1
            elif tecno == "JS":
                cant_tec_js += 1
            else:
                cant_tec_asp_net += 1

        for job in puestos:
            if job == "Jr" and edades_tecno_jr == None:
                edades_tecno_jr = edad
                nombre_menor_jr = nombre
            else:
                if job == "Jr" and edad < edades_tecno_jr:
                    edades_tecno_jr = edad
                    nombre_menor_jr = nombre
            

        promedio_edades_m = 0
        promedio_edades_f = 0
        promedio_edades_nb = 0

        if cant_gen_m != 0:
            promedio_edades_m = edades_gen_m / cant_gen_m
        elif cant_gen_f != 0:
            promedio_edades_f = edades_gen_f / cant_gen_f
        elif cant_gen_nb != 0:
            promedio_edades_nb = edades_gen_nb / cant_gen_nb


        if cant_tec_python >= cant_tec_asp_net and cant_tec_python >= cant_tec_js:
            tecno_mas_elegida = "PYTHON"
        else:
            if cant_tec_asp_net >= cant_tec_python and cant_tec_asp_net >= cant_tec_js:
                tecno_mas_elegida = "ASP.NET"
            else:
                tecno_mas_elegida = "JS"
        

        porcentaje_m = cant_gen_m * 100 / contador
        porcentaje_f = cant_gen_f * 100 / contador
        porcentaje_nb = cant_gen_nb * 100 / contador
    
        

        
        print(f"""
                Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
                cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {postulantes_punto_a}
                ------------------------------------------------------------------------------------------
                La persona de menor edad postulada para Jr es: {nombre_menor_jr}
                ------------------------------------------------------------------------------------------
                Promedio de las edades de las personas de genero Masculino: {promedio_edades_m:.0f}
                Promedio de las edades de las personas de genero Femenino: {promedio_edades_f:.0f}
                Promedio de las edades de las personas de genero No binario: {promedio_edades_nb:.0f}
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
