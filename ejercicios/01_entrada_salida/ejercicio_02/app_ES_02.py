import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # numero = 10
        # cant_divisores = 0
        
        # for i in range(1,numero + 1):
        #     if numero % i == 0:
        #         cant_divisores += 1
        # if cant_divisores == 2:
        #     print("Es primo")
        # else:
        #     print("No es primo")

        cadena = "hola"
        cant_cadena = len(cadena)
        for i in cadena:
            print(cadena[cant_cadena - 1])
            


            
    
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()