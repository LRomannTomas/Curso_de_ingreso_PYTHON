import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        limite = int(prompt("UTN","Hasta que numero queres recorrer? "))
        lista_num_pares = []
        contador = 0
        for num in range(1,limite + 1):
            if num % 2 == 0:
                lista_num_pares.append(num)
                contador += 1
        
        alert("UTN",f"""
              Los numeros pares encontrados son: {lista_num_pares}
              La cantidad de numeros pares es: {contador}""")
            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()