import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        maximo = None
        minimo = None
        #bandera = True
        while True:
            numero = prompt("UTN","Ingrese un numero: ")
            if numero == None:
                break
            else:
                numero = int(numero)

            if maximo == None or numero > maximo :
                maximo = numero
            else:
                if minimo == None or numero < minimo:
                    minimo = numero

            # if numero > maximo or bandera == True:
            #     maximo = numero
            # if numero < minimo or bandera == True:  -->   -->   -->   forma optima de hacer lo mismo pero aplicable a cualquier lenguaje                                                                        
            #     minimo = numero                                   (Es necesario cambiar los valores de maximo y minimo a 0 para que funcione)
            #     bandera = False
                
        self.txt_minimo.delete(0,100)
        self.txt_minimo.insert(0,minimo)
        self.txt_maximo.delete(0,100)
        self.txt_maximo.insert(0,maximo)

        

        



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
