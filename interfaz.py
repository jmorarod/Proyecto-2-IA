from tkinter import ttk, font, StringVar, Text, HORIZONTAL, END
from tkinter import filedialog as fd
import tkinter as tk
from g05 import *
#from tec.ic.ia.p2.g05 import *


class Palabras_Frame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        fuente = font.Font(weight='bold')


        self.motor = MotorLogico("basepruebas.tsv",[],[])
        self.motor.load_db()
        
        self.etiq1 = ttk.Label(self, text='Palabra 1:',font=fuente)
        self.etiq2=ttk.Label(self, text='Palabra 2:',font=fuente)

        self.etiq3 = ttk.Label(self, text='Operaciones:',font=fuente)
        self.etiq4=ttk.Label(self, text='Relaciones:',font=fuente)


        self.radio = StringVar()

        self.radio_etymological_origin_of_txt = StringVar()
        self.radio_has_derived_from_txt = StringVar()
        self.radio_is_derived_from_txt = StringVar()
        self.radio_etymology_txt = StringVar()
        self.radio_etymologically_related_txt = StringVar()
        self.radio_variant_orthography_txt= StringVar()
        self.radio_derived_txt = StringVar()
        self.radio_etymologically_txt = StringVar()

        self.radio_etymological_origin_of_txt.set("n")
        self.radio_has_derived_from_txt.set("n")
        self.radio_is_derived_from_txt.set("n")
        self.radio_etymology_txt.set("n")
        self.radio_etymologically_related_txt.set("n")
        self.radio_variant_orthography_txt.set("n")
        self.radio_derived_txt.set("n")
        self.radio_etymologically_txt.set("n")


        

        self.salida_operacion = Text(self, width = 50, height = 15)
        self.salida_operacion.place(relx=0.06, rely=0.3)
        
        
        self.radio_hermanos = ttk.Checkbutton(self, text="¿Son hermanos?", variable=self.radio, onvalue="Hermanos", offvalue="")
        self.radio_primos = ttk.Checkbutton(self, text="¿Son primos?", variable=self.radio, onvalue="Primos", offvalue="")
        self.radio_hijos = ttk.Checkbutton(self, text="¿Palabra2 es hija de Palabra1?", variable=self.radio, onvalue="Hija", offvalue="")
        self.radio_tio = ttk.Checkbutton(self, text="¿Palabra1 es tía de Palabra2?", variable=self.radio, onvalue="Tio", offvalue="")
        self.radio_primos_grado = ttk.Checkbutton(self, text="¿Son primos, en qué grado?", variable=self.radio, onvalue="PrimosGrado", offvalue="")


        self.radio_etymological_origin_of = ttk.Checkbutton(self, text="rel:etymological_origin_of", variable=self.radio_etymological_origin_of_txt, onvalue="rel:etymological_origin_of", offvalue="n")
        self.radio_has_derived_from = ttk.Checkbutton(self, text="rel:has_derived_form", variable=self.radio_has_derived_from_txt, onvalue="rel:has_derived_form", offvalue="n")
        self.radio_is_derived_from = ttk.Checkbutton(self, text="rel:is_derived_from", variable=self.radio_is_derived_from_txt, onvalue="rel:is_derived_from", offvalue="n")
        self.radio_etymology = ttk.Checkbutton(self, text="rel:etymology", variable=self.radio_etymology_txt, onvalue="rel:etymology", offvalue="n")
        self.radio_etymologically_related = ttk.Checkbutton(self, text="rel:etymologically_related", variable=self.radio_etymologically_related_txt, onvalue="rel:etymologically_related", offvalue="n")
        self.radio_variant_orthography = ttk.Checkbutton(self, text="rel:variant:orthography", variable=self.radio_variant_orthography_txt, onvalue="rel:variant:orthography", offvalue="n")
        self.radio_derived = ttk.Checkbutton(self, text="rel:derived", variable=self.radio_derived_txt, onvalue="rel:derived", offvalue="n")
        self.radio_etymologically = ttk.Checkbutton(self, text="rel:etymologically", variable=self.radio_etymologically_txt, onvalue="rel:etymologically", offvalue="n")

        self.radio_hermanos.place(relx=0.7, rely=0.1)
        self.radio_primos.place(relx=0.7, rely=0.15)
        self.radio_hijos.place(relx=0.7, rely=0.2)
        self.radio_tio.place(relx=0.7, rely=0.25)
        self.radio_primos_grado.place(relx=0.7, rely=0.3)

        self.radio_etymological_origin_of.place(relx=0.7, rely=0.5)
        self.radio_has_derived_from.place(relx=0.7, rely=0.55)
        self.radio_is_derived_from.place(relx=0.7, rely=0.6)
        self.radio_etymology.place(relx=0.7, rely=0.65)
        self.radio_etymologically_related.place(relx=0.7, rely=0.7)
        self.radio_variant_orthography.place(relx=0.7, rely=0.75)
        self.radio_derived.place(relx=0.7, rely=0.8)
        self.radio_etymologically.place(relx=0.7, rely=0.85)
        
        
        self.palabra1=StringVar()
        self.palabra2=StringVar()

        self.entrada_palabra1 = ttk.Entry(self, textvariable=self.palabra1, width=30)
        self.entrada_palabra2 = ttk.Entry(self, textvariable=self.palabra2, width=30)

        self.separ=ttk.Separator(self, orient=HORIZONTAL)

        self.boton1 = ttk.Button(self, text="Realizar operación", command=self.operar)
        self.boton2 = ttk.Button(self, text="Cancelar", command=quit)

        self.boton_abrir_archivo = ttk.Button(self, text = "Abrir base", command = self.abrir_archivo)
        self.boton_abrir_archivo.place(relx=0.06, rely=0.23)

        
        self.entrada_palabra1.place(relx=0.1, rely=0.1)
        self.entrada_palabra2.place(relx=0.4,rely=0.1)
        self.boton1.place(relx=0.30, rely=0.2)
        self.etiq1.place(relx=0.1, rely=0.03)
        self.etiq2.place(relx=0.4, rely=0.03)
        self.etiq3.place(relx=0.7, rely=0.05)
        self.etiq4.place(relx=0.7, rely=0.45)


        
    def operar(self):

        relaciones = []
        resultado = []
        resultado_primos = ()

        resultado_x = []
        resultado_y = []

        
        
        
        relaciones.append(self.radio_etymological_origin_of_txt.get())
        relaciones.append(self.radio_has_derived_from_txt.get())
        relaciones.append(self.radio_is_derived_from_txt.get())
        relaciones.append(self.radio_etymology_txt.get())
        relaciones.append(self.radio_etymologically_related_txt.get())
        relaciones.append(self.radio_variant_orthography_txt.get())
        relaciones.append(self.radio_derived_txt.get())
        relaciones.append(self.radio_etymologically_txt.get())
        
        

        relaciones_limpio = []

        for i in relaciones:
            if i != "n":
                relaciones_limpio.append(i)

        self.motor.valid_relations = relaciones_limpio
        self.motor.load_db()
        print(self.motor.valid_relations)
        

        self.salida_operacion.delete('1.0', END)
        
        if self.radio.get() == "Hermanos":
            resultado_x,resultado_y = self.motor.relacion_hermandad(self.palabra1.get(), self.palabra2.get())
            resultado_list_x = str(resultado_x)
            resultado_list_y = str(resultado_y)
            print(resultado_list_x)
            print(resultado_list_y)
            
            if len(resultado_x) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+resultado_list_x)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
            print("Hermanos")
        elif self.radio.get() == "Primos":
            resultado = self.motor.relacion_primer_primos(self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            
            if len(resultado) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
            else:
                self.salida_operacion.insert("1.0", "False")
            print("Primos")
        elif self.radio.get() == "Hija":
            resultado = self.motor.relacion_parent(self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            
            if len(resultado) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                #self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
            print("Hija")
        elif self.radio.get() == "Tio":
            resultado = self.motor.relacion_tio(self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            
            if len(resultado) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
            
            print("Tio")
        elif self.radio.get() == "PrimosGrado":
            resultado_primos = self.motor.relacion_primos_nivel(self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado_primos[0].data)
            
            if len(resultado_primos) > 0:
                self.salida_operacion.insert("1.0", "grado: "+str(resultado_primos[1]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Inferencias: \n"+resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
            
            print("PrimosGrado")


            
        

    def abrir_archivo(self):
        
        archivo = fd.askopenfilename()
        self.motor.database = archivo
        self.motor.kb = []
        self.motor.load_db()
        print(self.motor.database)
        

class Idiomas_Idiomas_Frame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        fuente = font.Font(weight='bold')

        self.motor = MotorLogico("basepruebas.tsv",[],[])
        self.motor.load_db()
        

        self.etiq1 = ttk.Label(self, text='Idioma 1:',font=fuente)
        self.etiq2=ttk.Label(self, text='Idioma 2:',font=fuente)

        self.etiq3 = ttk.Label(self, text='Operaciones:',font=fuente)
        self.etiq4=ttk.Label(self, text='Relaciones:',font=fuente)


        self.radio = StringVar()

        self.radio_etymological_origin_of_txt = StringVar()
        self.radio_has_derived_from_txt = StringVar()
        self.radio_is_derived_from_txt = StringVar()
        self.radio_etymology_txt = StringVar()
        self.radio_etymologically_related_txt = StringVar()
        self.radio_variant_orthography_txt= StringVar()
        self.radio_derived_txt = StringVar()
        self.radio_etymologically_txt = StringVar()


        self.radio_etymological_origin_of_txt.set("n")
        self.radio_has_derived_from_txt.set("n")
        self.radio_is_derived_from_txt.set("n")
        self.radio_etymology_txt.set("n")
        self.radio_etymologically_related_txt.set("n")
        self.radio_variant_orthography_txt.set("n")
        self.radio_derived_txt.set("n")
        self.radio_etymologically_txt.set("n")


        

        self.salida_operacion = Text(self, width = 50, height = 15)
        self.salida_operacion.place(relx=0.06, rely=0.3)
        
        
        self.radio_comunes_idiomas_cuenta = ttk.Checkbutton(self, text="¿Contar palabras comunes entre idiomas?", variable=self.radio, onvalue="ContarPalabras", offvalue="")
        self.radio_comunes_idiomas_lista = ttk.Checkbutton(self, text="¿Listar palabras comunes entre idiomas?", variable=self.radio, onvalue="ListarPalabras", offvalue="")
        self.radio_aporte_idiomas = ttk.Checkbutton(self, text="¿Idioma que más aportó a otro?", variable=self.radio, onvalue="IdiomaAporte", offvalue="")
        self.radio_aporte_entre_idiomas = ttk.Checkbutton(self, text="¿Listar todos los idiomas que aportaron al otro?", variable=self.radio, onvalue="IdiomasAporte", offvalue="")
        

        self.radio_etymological_origin_of = ttk.Checkbutton(self, text="rel:etymological_origin_of", variable=self.radio_etymological_origin_of_txt, onvalue="rel:etymological_origin_of", offvalue="n")
        self.radio_has_derived_from = ttk.Checkbutton(self, text="rel:has_derived_form", variable=self.radio_has_derived_from_txt, onvalue="rel:has_derived_form", offvalue="n")
        self.radio_is_derived_from = ttk.Checkbutton(self, text="rel:is_derived_from", variable=self.radio_is_derived_from_txt, onvalue="rel:is_derived_from", offvalue="n")
        self.radio_etymology = ttk.Checkbutton(self, text="rel:etymology", variable=self.radio_etymology_txt, onvalue="rel:etymology", offvalue="n")
        self.radio_etymologically_related = ttk.Checkbutton(self, text="rel:etymologically_related", variable=self.radio_etymologically_related_txt, onvalue="rel:etymologically_related", offvalue="n")
        self.radio_variant_orthography = ttk.Checkbutton(self, text="rel:variant:orthography", variable=self.radio_variant_orthography_txt, onvalue="rel:variant:orthography", offvalue="n")
        self.radio_derived = ttk.Checkbutton(self, text="rel:derived", variable=self.radio_derived_txt, onvalue="rel:derived", offvalue="n")
        self.radio_etymologically = ttk.Checkbutton(self, text="rel:etymologically", variable=self.radio_etymologically_txt, onvalue="rel:etymologically", offvalue="n")

        self.radio_comunes_idiomas_cuenta.place(relx=0.7, rely=0.1)
        self.radio_comunes_idiomas_lista.place(relx=0.7, rely=0.15)
        self.radio_aporte_idiomas.place(relx=0.7, rely=0.2)
        self.radio_aporte_entre_idiomas.place(relx=0.7, rely=0.25)
        
        self.radio_etymological_origin_of.place(relx=0.7, rely=0.5)
        self.radio_has_derived_from.place(relx=0.7, rely=0.55)
        self.radio_is_derived_from.place(relx=0.7, rely=0.6)
        self.radio_etymology.place(relx=0.7, rely=0.65)
        self.radio_etymologically_related.place(relx=0.7, rely=0.7)
        self.radio_variant_orthography.place(relx=0.7, rely=0.75)
        self.radio_derived.place(relx=0.7, rely=0.8)
        self.radio_etymologically.place(relx=0.7, rely=0.85)
        
        
        self.palabra1=StringVar()
        self.palabra2=StringVar()

        self.entrada_palabra1 = ttk.Entry(self, textvariable=self.palabra1, width=30)
        self.entrada_palabra2 = ttk.Entry(self, textvariable=self.palabra2, width=30)

        self.separ=ttk.Separator(self, orient=HORIZONTAL)

        self.boton1 = ttk.Button(self, text="Realizar operación", command=self.operar)
        self.boton2 = ttk.Button(self, text="Cancelar", command=quit)

        self.boton_abrir_archivo = ttk.Button(self, text = "Abrir base", command = self.abrir_archivo)
        self.boton_abrir_archivo.place(relx=0.06, rely=0.23)

        
        self.entrada_palabra1.place(relx=0.1, rely=0.1)
        self.entrada_palabra2.place(relx=0.4,rely=0.1)
        self.boton1.place(relx=0.30, rely=0.2)
        self.etiq1.place(relx=0.1, rely=0.03)
        self.etiq2.place(relx=0.4, rely=0.03)
        self.etiq3.place(relx=0.7, rely=0.05)
        self.etiq4.place(relx=0.7, rely=0.45)


        
    def operar(self):

        relaciones = []
        resultado = []
        resultado_primos = ()

        resultado_x = []
        resultado_y = []

        
        


        relaciones.append(self.radio_etymological_origin_of_txt.get())
        relaciones.append(self.radio_has_derived_from_txt.get())
        relaciones.append(self.radio_is_derived_from_txt.get())
        relaciones.append(self.radio_etymology_txt.get())
        relaciones.append(self.radio_etymologically_related_txt.get())
        relaciones.append(self.radio_variant_orthography_txt.get())
        relaciones.append(self.radio_derived_txt.get())
        relaciones.append(self.radio_etymologically_txt.get())
        
        

        relaciones_limpio = []

        for i in relaciones:
            if i != "n":
                relaciones_limpio.append(i)
        print(relaciones_limpio)

        self.motor.valid_relations = relaciones_limpio
        self.motor.load_db()
        
        
        print(self.motor.valid_relations)
        

        self.salida_operacion.delete('1.0', END)
        
        if self.radio.get() == "ContarPalabras":
            resultado = self.motor.contador_palabras_comun_idiomas(self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            if len(resultado[0].data) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+str(resultado[0].data))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Contador de palabras: \n"+str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
        
            print("ContarPalabras")
        elif self.radio.get() == "ListarPalabras":
            resultado = self.motor.palabras_comun_idiomas(self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            if len(resultado[0].data) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+str(resultado[0].data))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Lista de palabras: \n"+str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
        
            
            print("ListarPalabras")
        elif self.radio.get() == "IdiomaAporte":
            resultado = self.motor.mayor_aporte_a_idioma(self.palabra1.get(), False)
            resultado_list = str(resultado)
            if len(resultado[0]) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+str(resultado[0]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Aporte: \n"+str(resultado[2]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Idioma: \n"+str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")

                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
        
            
            print("IdiomaAporte")
        elif self.radio.get() == "IdiomasAporte":
            resultado = self.motor.aporte_idiomas(self.palabra1.get(), False)
            resultado_list = str(resultado)
            if len(resultado[0]) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+str(resultado[0]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Aporte: \n"+str(resultado[2].data))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Idioma: \n"+str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")

                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")

            print("IdiomasAporte")
            
            
    def abrir_archivo(self):
        archivo = fd.askopenfilename()
        self.motor.database = archivo
        self.motor.load_db()
        
        print(self.motor.database)
        

class Palabras_Idiomas_Frame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        fuente = font.Font(weight='bold')

        self.motor = MotorLogico("basepruebas.tsv",[],[])
        self.motor.load_db()
        print(self.motor.database)
        


        #self.tabs = ttk.Notebook(raiz)
        self.etiq1 = ttk.Label(self, text='Palabra:',font=fuente)
        self.etiq2=ttk.Label(self, text='Idioma:',font=fuente)

        self.etiq3 = ttk.Label(self, text='Operaciones:',font=fuente)
        self.etiq4=ttk.Label(self, text='Relaciones:',font=fuente)


        self.radio = StringVar()

        self.radio_etymological_origin_of_txt = StringVar()
        self.radio_has_derived_from_txt = StringVar()
        self.radio_is_derived_from_txt = StringVar()
        self.radio_etymology_txt = StringVar()
        self.radio_etymologically_related_txt = StringVar()
        self.radio_variant_orthography_txt= StringVar()
        self.radio_derived_txt = StringVar()
        self.radio_etymologically_txt = StringVar()

        self.radio_etymological_origin_of_txt.set("n")
        self.radio_has_derived_from_txt.set("n")
        self.radio_is_derived_from_txt.set("n")
        self.radio_etymology_txt.set("n")
        self.radio_etymologically_related_txt.set("n")
        self.radio_variant_orthography_txt.set("n")
        self.radio_derived_txt.set("n")
        self.radio_etymologically_txt.set("n")

        

        

        self.salida_operacion = Text(self, width = 50, height = 15)
        self.salida_operacion.place(relx=0.06, rely=0.3)
        
        
        self.radio_palabras_relacionadas = ttk.Checkbutton(self, text="¿Palabra relacionada con idioma?", variable=self.radio, onvalue="PalabraIdioma", offvalue="")
        self.radio_idiomas_originados = ttk.Checkbutton(self, text="¿Palabras en idioma originadas por palabra?", variable=self.radio, onvalue="IdiomasOriginados", offvalue="")
        self.radio_idiomas_relacionados = ttk.Checkbutton(self, text="¿Idiomas relacionados con palabra?", variable=self.radio, onvalue="IdiomasRelacionados", offvalue="")
        

        self.radio_etymological_origin_of = ttk.Checkbutton(self, text="rel:etymological_origin_of", variable=self.radio_etymological_origin_of_txt, onvalue="rel:etymological_origin_of", offvalue="")
        self.radio_has_derived_from = ttk.Checkbutton(self, text="rel:has_derived_form", variable=self.radio_has_derived_from_txt, onvalue="rel:has_derived_form", offvalue="")
        self.radio_is_derived_from = ttk.Checkbutton(self, text="rel:is_derived_from", variable=self.radio_is_derived_from_txt, onvalue="rel:is_derived_from", offvalue="")
        self.radio_etymology = ttk.Checkbutton(self, text="rel:etymology", variable=self.radio_etymology_txt, onvalue="rel:etymology", offvalue="")
        self.radio_etymologically_related = ttk.Checkbutton(self, text="rel:etymologically_related", variable=self.radio_etymologically_related_txt, onvalue="rel:etymologically_related", offvalue="")
        self.radio_variant_orthography = ttk.Checkbutton(self, text="rel:variant:orthography", variable=self.radio_variant_orthography_txt, onvalue="rel:variant:orthography", offvalue="")
        self.radio_derived = ttk.Checkbutton(self, text="rel:derived", variable=self.radio_derived_txt, onvalue="rel:derived", offvalue="")
        self.radio_etymologically = ttk.Checkbutton(self, text="rel:etymologically", variable=self.radio_etymologically_txt, onvalue="rel:etymologically", offvalue="")

        self.radio_palabras_relacionadas.place(relx=0.7, rely=0.1)
        self.radio_idiomas_originados.place(relx=0.7, rely=0.15)
        self.radio_idiomas_relacionados.place(relx=0.7, rely=0.2)
        
        self.radio_etymological_origin_of.place(relx=0.7, rely=0.5)
        self.radio_has_derived_from.place(relx=0.7, rely=0.55)
        self.radio_is_derived_from.place(relx=0.7, rely=0.6)
        self.radio_etymology.place(relx=0.7, rely=0.65)
        self.radio_etymologically_related.place(relx=0.7, rely=0.7)
        self.radio_variant_orthography.place(relx=0.7, rely=0.75)
        self.radio_derived.place(relx=0.7, rely=0.8)
        self.radio_etymologically.place(relx=0.7, rely=0.85)
        
        
        self.palabra1=StringVar()
        self.palabra2=StringVar()

        self.entrada_palabra1 = ttk.Entry(self, textvariable=self.palabra1, width=30)
        self.entrada_palabra2 = ttk.Entry(self, textvariable=self.palabra2, width=30)

        self.separ=ttk.Separator(self, orient=HORIZONTAL)

        self.boton1 = ttk.Button(self, text="Realizar operación", command=self.operar)
        self.boton2 = ttk.Button(self, text="Cancelar", command=quit)

        self.boton_abrir_archivo = ttk.Button(self, text = "Abrir base", command = self.abrir_archivo)
        self.boton_abrir_archivo.place(relx=0.06, rely=0.23)

        
        self.entrada_palabra1.place(relx=0.1, rely=0.1)
        self.entrada_palabra2.place(relx=0.4,rely=0.1)
        self.boton1.place(relx=0.30, rely=0.2)
        self.etiq1.place(relx=0.1, rely=0.03)
        self.etiq2.place(relx=0.4, rely=0.03)
        self.etiq3.place(relx=0.7, rely=0.05)
        self.etiq4.place(relx=0.7, rely=0.45)


        
    def operar(self):

        relaciones = []
        resultado = []
        resultado_primos = ()

        resultado_x = []
        resultado_y = []

            

        
        relaciones.append(self.radio_etymological_origin_of_txt.get())
        relaciones.append(self.radio_has_derived_from_txt.get())
        relaciones.append(self.radio_is_derived_from_txt.get())
        relaciones.append(self.radio_etymology_txt.get())
        relaciones.append(self.radio_etymologically_related_txt.get())
        relaciones.append(self.radio_variant_orthography_txt.get())
        relaciones.append(self.radio_derived_txt.get())
        relaciones.append(self.radio_etymologically_txt.get())
        
        

        relaciones_limpio = []

        for i in relaciones:
            if i != "n":
                relaciones_limpio.append(i)
        
        self.motor.valid_relations = relaciones_limpio
        self.motor.load_db()
        print(self.motor.valid_relations)
        
        

        self.salida_operacion.delete('1.0', END)
        
        if self.radio.get() == "PalabraIdioma":
            resultado = self.motor.relacion_palabra_idioma(self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            if len(resultado) > 0:
                self.salida_operacion.insert("1.0", resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
        
            print("PalabraIdioma")
        elif self.radio.get() == "IdiomasOriginados":
            resultado = self.motor.palabras_originadas(self.palabra1.get(), self.palabra2.get())
            print(resultado)
            resultado_list_inferencias = str(resultado[0].data)
            resultado_list_palabras = str(resultado[1].data)
            
            if len(resultado[0].data) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+resultado_list_inferencias)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Resultados: \n"+resultado_list_palabras)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
            
            print("IdiomasOriginados")
        elif self.radio.get() == "IdiomasRelacionados":
            resultado = self.motor.idiomas_relacionados_palabra(self.palabra1.get())
            print(resultado)
            resultado_list_inferencias = str(resultado[0].data)
            resultado_list_palabras = str(resultado[1])
            
            if len(resultado[0].data) > 0:
                self.salida_operacion.insert("1.0", "Inferencias: \n"+resultado_list_inferencias)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "Resultados: \n"+resultado_list_palabras)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")
                
                
            else:
                self.salida_operacion.insert("1.0", "False")
            print("IdiomasRelacionados")
        

            
        

    
    def abrir_archivo(self):
        archivo = fd.askopenfilename()
        self.motor.database = archivo
        print(self.motor.database)
        
        


class Aplicacion(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        #self.raiz = Tk()
        main_window.title("Segundo Proyecto")
        main_window.geometry('1000x500')
        fuente = font.Font(weight='bold')
        
        self.notebook = ttk.Notebook(self, width=1000, height=500)
        
        self.operaciones_palabras_palabras = Palabras_Frame(self.notebook)
        self.notebook.add(
            self.operaciones_palabras_palabras, text="Operaciones con palabras", padding=10)

        self.operaciones_palabras_idiomas = Palabras_Idiomas_Frame(self.notebook)
        self.notebook.add(
            self.operaciones_palabras_idiomas, text="Operaciones con palabras/idiomas", padding=10)

        self.operaciones_idiomas_idiomas = Idiomas_Idiomas_Frame(self.notebook)
        self.notebook.add(
            self.operaciones_idiomas_idiomas, text="Operaciones con idiomas", padding=10)
        
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()
        
        
def main():
    main_window = tk.Tk()
    mi_app = Aplicacion(main_window)
    mi_app.mainloop()
   #mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()
