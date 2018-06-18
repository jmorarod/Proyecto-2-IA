
import csv

from pyDatalog.pyDatalog import assert_fact, load, ask, clear
from pyDatalog import pyDatalog, pyEngine

import logging
pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)


#from tkinter import *

#from tkinter import ttk, font

from tkinter import ttk, font, StringVar, Text, HORIZONTAL, END


from tkinter import filedialog as fd

import tkinter as tk


class Relation(pyDatalog.Mixin):
    def __init__(
            self,
            first_lan,
            first_word,
            relation_type,
            second_lan,
            second_word):
        super(Relation, self).__init__()
        self.first_lan = first_lan
        self.first_word = first_word
        self.r_type = relation_type
        self.second_lan = second_lan
        self.second_word = second_word

    def __repr__(self):
        return self.first_lan + ": " + self.first_word + " " + \
            self.r_type + " " + self.second_lan + ": " + self.second_word

    @pyDatalog.program()
    def _():

        # Determinar si dos palabras son hermanas
        Relation.parent(
            X,
            Word1,
            Word2) <= (
            Relation.second_word[X] == Word2) & (
            Relation.first_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:derived')
        Relation.parent(
            X,
            Word1,
            Word2) <= (
            Relation.second_word[X] == Word2) & (
            Relation.first_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:has_derived_form')
        Relation.parent(
            X,
            Word1,
            Word2) <= (
            Relation.first_word[X] == Word2) & (
            Relation.second_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:is_derived_from')
        Relation.siblings(
            X,
            Y,
            Word1,
            Word2) <= Relation.parent(
            X,
            Z,
            Word1) & Relation.parent(
            Y,
            Z,
            Word2)

        # Determinar si dos palabras son primos primer nivel
        Relation.cousins(
            W,
            X,
            Y,
            Z,
            Word1,
            Word2) <= Relation.parent(
            W,
            A,
            Word1) & Relation.parent(
            X,
            B,
            Word2) & Relation.siblings(
                Y,
                Z,
                A,
            B)

        # Determinar si una palabra es tia de otra
        Relation.uncle(
            X,
            Y,
            Z,
            Word1,
            Word2) <= Relation.parent(
            X,
            A,
            Word2) & Relation.siblings(
            Y,
            Z,
            A,
            Word1)

        # Determinar ancestros de una palabra
        Relation.ancestor(
            X,
            Word1,
            Word2) <= (
            Relation.first_word[X] == Word2) & (
            Relation.second_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:is_derived_from')
        Relation.ancestor(
            X,
            Word1,
            Word2) <= (
            Relation.first_word[X] == Z) & (
            Relation.second_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:is_derived_from') & (
                    Relation.ancestor(
                        Y,
                        Z,
                        Word2))

        Relation.ancestor(
            X,
            Word1,
            Word2) <= (
            Relation.first_word[X] == Word2) & (
            Relation.second_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:has_derived_form')
        Relation.ancestor(
            X,
            Word1,
            Word2) <= (
            Relation.first_word[X] == Z) & (
            Relation.second_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:has_derived_form') & (
                    Relation.ancestor(
                        Y,
                        Z,
                        Word2))

        Relation.ancestor(
            X,
            Word1,
            Word2) <= (
            Relation.first_word[X] == Word2) & (
            Relation.second_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:derived')
        Relation.ancestor(
            X,
            Word1,
            Word2) <= (
            Relation.first_word[X] == Z) & (
            Relation.second_word[X] == Word1) & (
                Relation.r_type[X] == 'rel:derived') & (
                    Relation.ancestor(
                        Y,
                        Z,
                        Word2))

        Relation.ances(
            X,
            Y,
            Word1,
            Word2) <= Relation.ancestor(
            X,
            A,
            Word1) & Relation.ancestor(
            Y,
            B,
            Word2) & (
                A == B)

        # Determinas si dos palabras son primos y devolver grado
        Relation.counsingrade(
            W,
            X,
            Y,
            Z,
            Word1,
            Word2) <= Relation.ancestor(
            W,
            A,
            Word1) & Relation.ancestor(
            X,
            B,
            Word2) & Relation.siblings(
                Y,
                Z,
                A,
            B)

        # Determinar si una palabra esta relacionada con un idioma o no

        (Relation.hasLanAndWord[X, Lan, Word]) <= (
            Relation.first_word[X] == Word) & (Relation.first_lan[X] == Lan)
        (Relation.hasLanAndWord[X, Lan, Word]) <= (
            Relation.second_word[X] == Word) & (Relation.second_lan[X] == Lan)
        (Relation.hasLanAndWord[X, Lan, Word]) <= (
            Relation.second_word[X] == Word) & (Relation.first_lan[X] == Lan)
        (Relation.hasLanAndWord[X, Lan, Word]) <= (
            Relation.first_word[X] == Word) & (Relation.second_lan[X] == Lan)
        # Palabras originadas por otra
        Relation.originatedWords(
            X,
            Word,
            Lan,
            Result) <= (
            Relation.second_word[X] == Word) & (
            Relation.second_lan[X] == Lan) & (
                Relation.r_type[X] == 'rel:is_derived_from') & (
                    (Relation.first_word[X],
                     Relation.first_lan[X]) == Result)
        Relation.originatedWords(
            X,
            Word,
            Lan,
            Result) <= (
            Relation.first_word[X] == Word) & (
            Relation.first_lan[X] == Lan) & (
                Relation.r_type[X] == 'rel:has_derived_form') & (
                    (Relation.second_word[X],
                     Relation.second_lan[X]) == Result)
        Relation.originatedWords(
            X,
            Word,
            Lan,
            Result) <= (
            Relation.second_word[X] == Word) & (
            Relation.second_lan[X] == Lan) & (
                Relation.r_type[X] == 'rel:etymology') & (
                    (Relation.first_word[X],
                     Relation.first_lan[X]) == Result)
        Relation.originatedWords(
            X,
            Word,
            Lan,
            Result) <= (
            Relation.first_word[X] == Word) & (
            Relation.first_lan[X] == Lan) & (
                Relation.r_type[X] == 'rel:etymological_origin_of') & (
                    (Relation.second_word[X],
                     Relation.second_lan[X]) == Result)
        Relation.originatedWords(
            X,
            Word,
            Lan,
            Result) <= (
            Relation.first_word[X] == Word) & (
            Relation.first_lan[X] == Lan) & (
                Relation.r_type[X] == 'rel:variant:orthography') & (
                    (Relation.second_word[X],
                     Relation.second_lan[X]) == Result)
        # Idiomas relacionados con una palabra
        Relation.lanByWord(
            X, Word, Result) <= (
            Relation.second_word[X] == Word) & (
            (Relation.first_lan[X], Relation.second_lan[X]) == Result)
        Relation.lanByWord(
            X, Word, Result) <= (
            Relation.first_word[X] == Word) & (
            (Relation.first_lan[X], Relation.second_lan[X]) == Result)
        # Palabras comunes entre dos idiomas(Contar)
        (Relation.countWordInCommon[X, Y, Lan1, Lan2] == len_(Y)) <= (Relation.second_word[X] == Relation.second_word[Y]) & (
            Relation.second_lan[X] == Lan1) & (Relation.second_lan[Y] == Lan2) & (X != Y)
        (Relation.countWordInCommon[X, Y, Lan1, Lan2] == len_(Y)) <= (Relation.first_word[X] == Relation.first_word[Y]) & (
            Relation.first_lan[X] == Lan1) & (Relation.first_lan[Y] == Lan2) & (X != Y)
        (Relation.countWordInCommon[X, Y, Lan1, Lan2] == len_(Y)) <= (Relation.second_word[X] == Relation.first_word[Y]) & (
            Relation.second_lan[X] == Lan1) & (Relation.first_lan[Y] == Lan2) & (X != Y)
        (Relation.countWordInCommon[X, Y, Lan1, Lan2] == len_(Y)) <= (Relation.second_word[X] == Relation.first_word[Y]) & (
            Relation.second_lan[X] == Lan2) & (Relation.first_lan[Y] == Lan1) & (X != Y)
        # Palabras comunes entre dos idiomas(Listar)
        Relation.wordInCommon(
            X,
            Y,
            Lan1,
            Lan2,
            Z) <= (
            Relation.second_word[X] == Relation.second_word[Y]) & (
            Relation.second_lan[X] == Lan1) & (
                Relation.second_lan[Y] == Lan2) & (
                    X != Y) & (
                        Relation.second_word[X] == Z)
        Relation.wordInCommon(
            X,
            Y,
            Lan1,
            Lan2,
            Z) <= (
            Relation.first_word[X] == Relation.first_word[Y]) & (
            Relation.first_lan[X] == Lan1) & (
                Relation.first_lan[Y] == Lan2) & (
                    X != Y) & (
                        Relation.first_word[X] == Z)
        Relation.wordInCommon(
            X,
            Y,
            Lan1,
            Lan2,
            Z) <= (
            Relation.second_word[X] == Relation.first_word[Y]) & (
            Relation.second_lan[X] == Lan1) & (
                Relation.first_lan[Y] == Lan2) & (
                    X != Y) & (
                        Relation.second_word[X] == Z)
        Relation.wordInCommon(
            X,
            Y,
            Lan1,
            Lan2,
            Z) <= (
            Relation.second_word[X] == Relation.first_word[Y]) & (
            Relation.second_lan[X] == Lan2) & (
                Relation.first_lan[Y] == Lan1) & (
                    X != Y) & (
                        Relation.second_word[X] == Z)
        # Aporte a idioma(Listar)
        Relation.proportionPerLan(
            X,
            BaseLan,
            GLan) <= (
            Relation.first_lan[X] == BaseLan) & (
            Relation.second_lan[X] == GLan) & (
                Relation.r_type[X] == 'rel:etymology')
        Relation.proportionPerLan(
            X,
            BaseLan,
            GLan) <= (
            Relation.first_lan[X] == GLan) & (
            Relation.second_lan[X] == BaseLan) & (
                Relation.r_type[X] == 'rel:etymological_origin_of')
        Relation.proportionPerLan(
            X,
            BaseLan,
            GLan) <= (
            Relation.first_lan[X] == GLan) & (
            Relation.second_lan[X] == BaseLan) & (
                Relation.r_type[X] == 'rel:variant:orthography')
        Relation.proportionPerLan(
            X,
            BaseLan,
            GLan) <= (
            Relation.second_lan[X] == GLan) & (
            Relation.first_lan[X] == BaseLan) & (
                Relation.r_type[X] == 'rel:has_derived_form')
        Relation.proportionPerLan(
            X,
            BaseLan,
            GLan) <= (
            Relation.first_lan[X] == BaseLan) & (
            Relation.second_lan[X] == GLan) & (
                Relation.r_type[X] == 'rel:is_derived_from')
        Relation.proportionPerLan(
            X,
            BaseLan,
            GLan) <= (
            Relation.second_lan[X] == GLan) & (
            Relation.first_lan[X] == BaseLan) & (
                Relation.r_type[X] == 'rel:derived')


# Funciones para usar en expresiones logicas

def lista_vacia(lista):
    if(lista == []):
        return True
    return False


def lista_porcentaje(lista, total):
    for i in range(len(lista)):
        lista[i] /= total
    return lista


def max_index(lista):
    max_value = 0
    max_index = 0
    for i in range(len(lista)):
        if(lista.data[0][i] > max_value):
            max_value = lista[i]
            max_index = i
    return max_index

#motor = MotorLogico("etymwn.tsv",[],["eng","deu","sco"])


def funcion():
    # motor = MotorLogico("etymwn.tsv",["rel:has_derived_form"],[])
    # return (motor.relacion_primos_nivel("h","j"))
    return motor.aporte_idiomas("eng")


class MotorLogico(object):
    def __init__(self, database, valid_relations, lan, load_database=False):
        self.valid_relations = valid_relations
        self.kb = []
        self.lan = lan
        self.database = database

        try:
            if(load_database):
                if(lan == []):
                    self.load_db()
                else:
                    self.load_db_by_language()
        except BaseException:
            self.kb = []

    def relacion_palabra_idioma(self, palabra, idioma):
        X = pyDatalog.Variable()
        Relation.hasLanAndWord[X, idioma, palabra]
        return X

    def relacion_hermandad(self, palabra1, palabra2):
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Relation.siblings(X, Y, palabra1, palabra2)
        return X, Y

    def relacion_parent(self, palabra1, palabra2):
        X = pyDatalog.Variable()
        (Relation.parent(X, palabra1, palabra2))
        return X

    def relacion_primer_primos(self, palabra1, palabra2):
        W = pyDatalog.Variable()
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Z = pyDatalog.Variable()
        (Relation.cousins(W, X, Y, Z, palabra1, palabra2))
        return Y, Z

    def relacion_tio(self, palabra1, palabra2):
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Z = pyDatalog.Variable()
        return Relation.uncle(X, Y, Z, palabra1, palabra2)

    def relacion_ancestro(self, palabra1, palabra2):
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        return Relation.ancestro(X, palabra1, palabra2)

    def primos_aux(self, palabra1):
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Relation.ancestor(X, Y, palabra1)
        return Y

    def relacion_primos_nivel(self, palabra1, palabra2):
        W = pyDatalog.Variable()
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Z = pyDatalog.Variable()
        w1 = len(self.primos_aux(palabra1))
        w2 = len(self.primos_aux(palabra2))
        grade = len(Relation.ances(X, Y, palabra1, palabra2))
        level = max(w1, w2) - grade
        resultado = Relation.counsingrade(W, X, Y, Z, palabra1, palabra2)
        return (resultado, level)

    def palabras_originadas(self, palabra, idioma):
        X = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        Relation.originatedWords(X, palabra, idioma, Result)
        return X, Result

    def idiomas_relacionados_palabra(self, palabra):
        X = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        Relation.lanByWord(X, palabra, Result)
        Result = set(eval(str(Result)))
        return X, Result

    def palabras_comun_idiomas(self, idioma1, idioma2):
        returnList = []
        X, Result = self.palabras_comun_idiomas_aux(idioma1, idioma2)
        Result = set(eval(str(Result)))
        return X, Result

    def palabras_comun_idiomas_aux(self, idioma1, idioma2):
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Z = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        Relation.wordInCommon(X, Y, idioma1, idioma2, Z)
        return X, Z

    def contador_palabras_comun_idiomas(self, idioma1, idioma2):
        inferencias, resultado = self.palabras_comun_idiomas_aux(
            idioma1, idioma2)
        return inferencias, len(resultado)

    def mayor_aporte_a_idioma(self, idioma, test=False):
        inferencias, idiomas, porcentajes = self.aporte_idiomas(idioma, test)
        Result = pyDatalog.Variable()
        pyDatalog.create_terms("max_index")
        print(max_index(porcentajes) == Result)
        return inferencias, idiomas[int(
            str(Result.v()))], porcentajes.data[0][int(str(Result.v()))]

    # Retorna las inferencias, la lista de idiomas que aportaron y el
    # porcentaje de cada una respectivamente
    def aporte_idiomas(self, idioma, test=False):
        if(self.lan == []):
            return self.aporte_idiomas_aux(
                idioma, self.get_idiomas_file(), test)
        else:
            return self.aporte_idiomas_aux(idioma, self.lan, test)

    def aporte_idiomas_aux(self, idioma, idiomas, test=False):
        X = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        Porcentajes = pyDatalog.Variable()
        lan_kb = []
        inferences = []
        idiomas_lista = []
        percentages = []
        total = 0
        pyDatalog.create_terms('lista_vacia')
        pyDatalog.create_terms('lista_porcentaje')

        for i in idiomas:
            if(i != idioma):
                if(not test):
                    self.kb = []
                    self.lan = [i]
                    self.load_db_by_language()

                (lista_vacia(Relation.proportionPerLan(X, idioma, i)) == Result)
                if(not Result.v()):
                    inferences += [Relation.proportionPerLan(X, idioma, i)]
                    idiomas_lista += [i]
                    total += len(Relation.proportionPerLan(X, idioma, i))
                    percentages += [len(Relation.proportionPerLan(X, idioma, i))]
        (lista_porcentaje(percentages, total) == Porcentajes)
        return inferences, idiomas_lista, Porcentajes

    def get_idiomas_file(self):
        try:
            idiomas_file = open("lan.txt", "r")
            idiomas = []
            for row in idiomas_file:
                idiomas += [row.rstrip()]
            return idiomas
        except BaseException:
            return []

    def lista_porcentaje(self, lista, total):
        for i in lista:
            i /= total
        return lista

    def load_db_by_language(self):
        print("Idioma")
        fd = open(self.database, encoding="utf8")
        rd = csv.reader(fd, delimiter="\t")
        cont = 0
        for row in rd:
            r_type = row[1]
            if(self.valid_relations != [] and r_type not in self.valid_relations):
                continue
            f_lan = row[0][0:3]
            s_lan = row[2][0:3]
            if(f_lan not in self.lan and s_lan not in self.lan):
                continue

            f_word = row[0][5:]
            s_word = row[2][5:]
            self.kb.append(Relation(f_lan, f_word, r_type, s_lan, s_word))
            cont += 1
        print(str(cont) + " filas leidas")

    def load_db_equals(self):
        print("Equals")
        fd = open(self.database, encoding="utf8")
        rd = csv.reader(fd, delimiter="\t")
        words = []
        cont = 0
        for row in rd:
            r_type = row[1]
            add_to_kb = False
            if(self.valid_relations != [] and r_type not in self.valid_relations):
                continue
            f_lan = row[0][0:3]
            s_lan = row[2][0:3]
            if(f_lan not in self.lan and s_lan not in self.lan):
                continue
            f_word = row[0][5:]

            s_word = row[2][5:]
            if([f_word, f_lan] not in words):
                words.append([f_word, f_lan])
                add_to_kb = True
            if([s_word, s_lan] not in words):
                words.append([s_word, s_lan])
                add_to_kb = True
            if(add_to_kb):
                self.kb.append(Relation(f_lan, f_word, r_type, s_lan, s_word))
                cont += 1
        print(str(cont) + " relaciones agregadas a kb")

    def load_db(self):
        print("Completa")
        fd = open(self.database, encoding="utf8")
        rd = csv.reader(fd, delimiter="\t")
        for row in rd:
            r_type = row[1]
            if(self.valid_relations != [] and r_type not in self.valid_relations):
                continue
            f_lan = row[0][0:3]
            f_word = row[0][5:]
            s_lan = row[2][0:3]
            s_word = row[2][5:]
            self.kb.append(Relation(f_lan, f_word, r_type, s_lan, s_word))


class Palabras_Frame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fuente = font.Font(weight='bold')

        self.motor = None

        self.etiq1 = ttk.Label(self, text='Palabra 1:', font=fuente)
        self.etiq2 = ttk.Label(self, text='Palabra 2:', font=fuente)

        self.etiq3 = ttk.Label(self, text='Operaciones:', font=fuente)
        self.etiq4 = ttk.Label(self, text='Relaciones:', font=fuente)

        self.radio = StringVar()

        self.radio_etymological_origin_of_txt = StringVar()
        self.radio_has_derived_from_txt = StringVar()
        self.radio_is_derived_from_txt = StringVar()
        self.radio_etymology_txt = StringVar()
        self.radio_etymologically_related_txt = StringVar()
        self.radio_variant_orthography_txt = StringVar()
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

        self.salida_operacion = Text(self, width=50, height=15)
        self.salida_operacion.place(relx=0.06, rely=0.3)

        self.radio_hermanos = ttk.Checkbutton(
            self,
            text="¿Son hermanos?",
            variable=self.radio,
            onvalue="Hermanos",
            offvalue="")
        self.radio_primos = ttk.Checkbutton(
            self,
            text="¿Son primos?",
            variable=self.radio,
            onvalue="Primos",
            offvalue="")
        self.radio_hijos = ttk.Checkbutton(
            self,
            text="¿Palabra2 es hija de Palabra1?",
            variable=self.radio,
            onvalue="Hija",
            offvalue="")
        self.radio_tio = ttk.Checkbutton(
            self,
            text="¿Palabra1 es tía de Palabra2?",
            variable=self.radio,
            onvalue="Tio",
            offvalue="")
        self.radio_primos_grado = ttk.Checkbutton(
            self,
            text="¿Son primos?",
            variable=self.radio,
            onvalue="PrimosGrado",
            offvalue="")

        self.radio_etymological_origin_of = ttk.Checkbutton(
            self,
            text="rel:etymological_origin_of",
            variable=self.radio_etymological_origin_of_txt,
            onvalue="rel:etymological_origin_of",
            offvalue="n")
        self.radio_has_derived_from = ttk.Checkbutton(
            self,
            text="rel:has_derived_form",
            variable=self.radio_has_derived_from_txt,
            onvalue="rel:has_derived_form",
            offvalue="n")
        self.radio_is_derived_from = ttk.Checkbutton(
            self,
            text="rel:is_derived_from",
            variable=self.radio_is_derived_from_txt,
            onvalue="rel:is_derived_from",
            offvalue="n")
        self.radio_etymology = ttk.Checkbutton(
            self,
            text="rel:etymology",
            variable=self.radio_etymology_txt,
            onvalue="rel:etymology",
            offvalue="n")
        self.radio_etymologically_related = ttk.Checkbutton(
            self,
            text="rel:etymologically_related",
            variable=self.radio_etymologically_related_txt,
            onvalue="rel:etymologically_related",
            offvalue="n")
        self.radio_variant_orthography = ttk.Checkbutton(
            self,
            text="rel:variant:orthography",
            variable=self.radio_variant_orthography_txt,
            onvalue="rel:variant:orthography",
            offvalue="n")
        self.radio_derived = ttk.Checkbutton(
            self,
            text="rel:derived",
            variable=self.radio_derived_txt,
            onvalue="rel:derived",
            offvalue="n")
        self.radio_etymologically = ttk.Checkbutton(
            self,
            text="rel:etymologically",
            variable=self.radio_etymologically_txt,
            onvalue="rel:etymologically",
            offvalue="n")

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

        self.palabra1 = StringVar()
        self.palabra2 = StringVar()

        self.entrada_palabra1 = ttk.Entry(
            self, textvariable=self.palabra1, width=30)
        self.entrada_palabra2 = ttk.Entry(
            self, textvariable=self.palabra2, width=30)

        self.separ = ttk.Separator(self, orient=HORIZONTAL)

        self.boton1 = ttk.Button(
            self,
            text="Realizar operación",
            command=self.operar)
        self.boton2 = ttk.Button(self, text="Cancelar", command=quit)

        self.boton_abrir_archivo = ttk.Button(
            self, text="Abrir base", command=self.abrir_archivo)
        self.boton_abrir_archivo.place(relx=0.06, rely=0.23)

        self.entrada_palabra1.place(relx=0.1, rely=0.1)
        self.entrada_palabra2.place(relx=0.4, rely=0.1)
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

        self.motor = MotorLogico("etymwn.tsv", [], [])

        """ #padre/hijo
        self.motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
        self.motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "d"))
        self.motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
        self.motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
        self.motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "a"))
        """

        """#hermandad
        self.motor.kb.append(Relation("eng","a","rel:is_derived_from","eng","x"))
        self.motor.kb.append(Relation("eng","a","rel:is_derived_from","eng","y"))
        self.motor.kb.append(Relation("eng","b","rel:is_derived_from","eng","x"))
        self.motor.kb.append(Relation("eng","c","rel:is_derived_from","eng","b"))
        self.motor.kb.append(Relation("eng","d","rel:is_derived_from","eng","b"))

        self.motor.kb.append(Relation("eng","x","rel:has_derived_form","eng","a"))
        self.motor.kb.append(Relation("eng","x","rel:has_derived_form","eng","b"))
        self.motor.kb.append(Relation("eng","y","rel:has_derived_form","eng","a"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","c"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","d"))
        """

        """ primos primer
        self.motor.kb.append(Relation("eng","b","rel:is_derived_from","eng","a"))
        self.motor.kb.append(Relation("eng","c","rel:is_derived_from","eng","a"))
        self.motor.kb.append(Relation("eng","d","rel:is_derived_from","eng","a"))
        self.motor.kb.append(Relation("eng","e","rel:is_derived_from","eng","b"))
        self.motor.kb.append(Relation("eng","f","rel:is_derived_from","eng","b"))
        self.motor.kb.append(Relation("eng","g","rel:is_derived_from","eng","d"))

        self.motor.kb.append(Relation("eng","a","rel:has_derived_form","eng","b"))
        self.motor.kb.append(Relation("eng","a","rel:has_derived_form","eng","c"))
        self.motor.kb.append(Relation("eng","a","rel:has_derived_form","eng","d"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","e"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","f"))
        self.motor.kb.append(Relation("eng","d","rel:has_derived_form","eng","g"))
        """

        """ tios
        self.motor.kb.append(Relation("eng","b","rel:is_derived_from","eng","a"))
        self.motor.kb.append(Relation("eng","c","rel:is_derived_from","eng","a"))
        self.motor.kb.append(Relation("eng","d","rel:is_derived_from","eng","b"))
        self.motor.kb.append(Relation("eng","e","rel:is_derived_from","eng","b"))
        self.motor.kb.append(Relation("eng","f","rel:is_derived_from","eng","c"))
        self.motor.kb.append(Relation("eng","g","rel:is_derived_from","eng","c"))

        self.motor.kb.append(Relation("eng","a","rel:has_derived_form","eng","b"))
        self.motor.kb.append(Relation("eng","a","rel:has_derived_form","eng","c"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","d"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","e"))
        self.motor.kb.append(Relation("eng","c","rel:has_derived_form","eng","f"))
        self.motor.kb.append(Relation("eng","c","rel:has_derived_form","eng","g"))
        """

        """ primos grado
        self.motor.kb.append(Relation("eng","a","rel:is_derived_from","eng","x"))
        self.motor.kb.append(Relation("eng","b","rel:is_derived_from","eng","a"))
        self.motor.kb.append(Relation("eng","c","rel:is_derived_from","eng","a"))
        self.motor.kb.append(Relation("eng","d","rel:is_derived_from","eng","b"))
        self.motor.kb.append(Relation("eng","e","rel:is_derived_from","eng","b"))
        self.motor.kb.append(Relation("eng","f","rel:is_derived_from","eng","c"))
        self.motor.kb.append(Relation("eng","g","rel:is_derived_from","eng","c"))
        self.motor.kb.append(Relation("eng","h","rel:is_derived_from","eng","d"))
        self.motor.kb.append(Relation("eng","i","rel:is_derived_from","eng","d"))
        self.motor.kb.append(Relation("eng","j","rel:is_derived_from","eng","f"))
        self.motor.kb.append(Relation("eng","k","rel:is_derived_from","eng","f"))
        self.motor.kb.append(Relation("eng","y","rel:is_derived_from","eng","i"))

        self.motor.kb.append(Relation("eng","x","rel:has_derived_form","eng","a"))
        self.motor.kb.append(Relation("eng","a","rel:has_derived_form","eng","b"))
        self.motor.kb.append(Relation("eng","a","rel:has_derived_form","eng","c"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","d"))
        self.motor.kb.append(Relation("eng","b","rel:has_derived_form","eng","e"))
        self.motor.kb.append(Relation("eng","c","rel:has_derived_form","eng","f"))
        self.motor.kb.append(Relation("eng","c","rel:has_derived_form","eng","g"))
        self.motor.kb.append(Relation("eng","d","rel:has_derived_form","eng","h"))
        self.motor.kb.append(Relation("eng","d","rel:has_derived_form","eng","i"))
        self.motor.kb.append(Relation("eng","f","rel:has_derived_form","eng","j"))
        self.motor.kb.append(Relation("eng","f","rel:has_derived_form","eng","k"))
        self.motor.kb.append(Relation("eng","i","rel:has_derived_form","eng","y"))
        """

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

        self.salida_operacion.delete('1.0', END)

        if self.radio.get() == "Hermanos":
            resultado_x, resultado_y = self.motor.relacion_hermandad(
                self.palabra1.get(), self.palabra2.get())
            resultado_list_x = str(resultado_x)
            resultado_list_y = str(resultado_y)
            print(resultado_list_x)
            print(resultado_list_y)

            if len(resultado_x) > 0:
                self.salida_operacion.insert("1.0", resultado_list_x)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")
            print("Hermanos")
        elif self.radio.get() == "Primos":
            resultado = self.motor.relacion_primer_primos(
                self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)

            if len(resultado) > 0:
                self.salida_operacion.insert("1.0", resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")
            print("Primos")
        elif self.radio.get() == "Hija":
            resultado = self.motor.relacion_parent(
                self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)

            if len(resultado) > 0:
                self.salida_operacion.insert("1.0", resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")
            print("Hija")
        elif self.radio.get() == "Tio":
            resultado = self.motor.relacion_tio(
                self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)

            if len(resultado) > 0:
                self.salida_operacion.insert("1.0", resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")

            print("Tio")
        elif self.radio.get() == "PrimosGrado":
            resultado_primos = self.motor.relacion_primos_nivel(
                self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado_primos[0].data)
            print(resultado_list)

            if len(resultado_primos) > 0:
                self.salida_operacion.insert("1.0", resultado_list)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "grado: " + str(resultado_primos[1]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")

            print("PrimosGrado")

    def abrir_archivo(self):

        archivo = fd.askopenfilename()


class Idiomas_Idiomas_Frame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fuente = font.Font(weight='bold')

        self.motor = None

        self.etiq1 = ttk.Label(self, text='Idioma 1:', font=fuente)
        self.etiq2 = ttk.Label(self, text='Idioma 2:', font=fuente)

        self.etiq3 = ttk.Label(self, text='Operaciones:', font=fuente)
        self.etiq4 = ttk.Label(self, text='Relaciones:', font=fuente)

        self.radio = StringVar()

        self.radio_etymological_origin_of_txt = StringVar()
        self.radio_has_derived_from_txt = StringVar()
        self.radio_is_derived_from_txt = StringVar()
        self.radio_etymology_txt = StringVar()
        self.radio_etymologically_related_txt = StringVar()
        self.radio_variant_orthography_txt = StringVar()
        self.radio_derived_txt = StringVar()
        self.radio_etymologically_txt = StringVar()

        self.salida_operacion = Text(self, width=50, height=15)
        self.salida_operacion.place(relx=0.06, rely=0.3)

        self.radio_comunes_idiomas_cuenta = ttk.Checkbutton(
            self,
            text="¿Contar palabras comunes entre idiomas?",
            variable=self.radio,
            onvalue="ContarPalabras",
            offvalue="")
        self.radio_comunes_idiomas_lista = ttk.Checkbutton(
            self,
            text="¿Listar palabras comunes entre idiomas?",
            variable=self.radio,
            onvalue="ListarPalabras",
            offvalue="")
        self.radio_aporte_idiomas = ttk.Checkbutton(
            self,
            text="¿Idioma que más aportó a otro?",
            variable=self.radio,
            onvalue="IdiomaAporte",
            offvalue="")
        self.radio_aporte_entre_idiomas = ttk.Checkbutton(
            self,
            text="¿Listar todos los idiomas que aportaron al otro?",
            variable=self.radio,
            onvalue="IdiomasAporte",
            offvalue="")

        self.radio_etymological_origin_of = ttk.Checkbutton(
            self,
            text="rel:etymological_origin_of",
            variable=self.radio_etymological_origin_of_txt,
            onvalue="rel:etymological_origin_of",
            offvalue="")
        self.radio_has_derived_from = ttk.Checkbutton(
            self,
            text="rel:has_derived_form",
            variable=self.radio_has_derived_from_txt,
            onvalue="rel:has_derived_form",
            offvalue="")
        self.radio_is_derived_from = ttk.Checkbutton(
            self,
            text="rel:is_derived_from",
            variable=self.radio_is_derived_from_txt,
            onvalue="rel:is_derived_from",
            offvalue="")
        self.radio_etymology = ttk.Checkbutton(
            self,
            text="rel:etymology",
            variable=self.radio_etymology_txt,
            onvalue="rel:etymology",
            offvalue="")
        self.radio_etymologically_related = ttk.Checkbutton(
            self,
            text="rel:etymologically_related",
            variable=self.radio_etymologically_related_txt,
            onvalue="rel:etymologically_related",
            offvalue="")
        self.radio_variant_orthography = ttk.Checkbutton(
            self,
            text="rel:variant:orthography",
            variable=self.radio_variant_orthography_txt,
            onvalue="rel:variant:orthography",
            offvalue="")
        self.radio_derived = ttk.Checkbutton(
            self,
            text="rel:derived",
            variable=self.radio_derived_txt,
            onvalue="rel:derived",
            offvalue="")
        self.radio_etymologically = ttk.Checkbutton(
            self,
            text="rel:etymologically",
            variable=self.radio_etymologically_txt,
            onvalue="rel:etymologically",
            offvalue="")

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

        self.palabra1 = StringVar()
        self.palabra2 = StringVar()

        self.entrada_palabra1 = ttk.Entry(
            self, textvariable=self.palabra1, width=30)
        self.entrada_palabra2 = ttk.Entry(
            self, textvariable=self.palabra2, width=30)

        self.separ = ttk.Separator(self, orient=HORIZONTAL)

        self.boton1 = ttk.Button(
            self,
            text="Realizar operación",
            command=self.operar)
        self.boton2 = ttk.Button(self, text="Cancelar", command=quit)

        self.boton_abrir_archivo = ttk.Button(
            self, text="Abrir base", command=self.abrir_archivo)
        self.boton_abrir_archivo.place(relx=0.06, rely=0.23)

        self.entrada_palabra1.place(relx=0.1, rely=0.1)
        self.entrada_palabra2.place(relx=0.4, rely=0.1)
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

        self.motor = MotorLogico("etymwn.tsv", [], [])

        """
        #contador palabras común
        self.motor.kb.append(Relation("eng", "palabra", "rel:is_derived_from", "deu", "pal"))
        self.motor.kb.append(Relation("deu", "palabra", "rel:is_derived_from", "deu", "pa"))
        self.motor.kb.append(Relation("eng", "nagware", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("deu", "nagware", "rel:is_derived_from", "eng", "nagw"))
        self.motor.kb.append(Relation("eng", "nag", "rel:has_derived_form", "deu", "hambu"))
        self.motor.kb.append(Relation("eng", "na", "rel:has_derived_form", "eng", "hamburge"))
        self.motor.kb.append(Relation("eng", "hamburger", "rel:is_derived_from", "deu", "nag"))
        self.motor.kb.append(Relation("eng", "hamburg", "rel:is_derived_from", "eng", "ham"))
        """

        """
        #lista palabras común
        self.motor.kb.append(Relation("eng", "palabra", "rel:is_derived_from", "deu", "pal"))
        self.motor.kb.append(Relation("deu", "palabra", "rel:is_derived_from", "deu", "pa"))
        self.motor.kb.append(Relation("eng", "nagware", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("deu", "nagware", "rel:is_derived_from", "eng", "nagw"))
        self.motor.kb.append(Relation("eng", "nag", "rel:has_derived_form", "deu", "hambu"))
        self.motor.kb.append(Relation("eng", "na", "rel:has_derived_form", "eng", "hamburge"))
        self.motor.kb.append(Relation("eng", "hamburger", "rel:is_derived_from", "deu", "nag"))
        self.motor.kb.append(Relation("eng", "hamburg", "rel:is_derived_from", "eng", "ham"))
        self.motor.kb.append(Relation("eng", "hello", "rel:is_derived_from", "ita", "hola"))
        """

        # mayor aporte idioma a otro
        """
        self.motor.kb.append(Relation("eng", "palabra", "rel:is_derived_from", "deu", "pal"))
        self.motor.kb.append(Relation("deu", "palabra", "rel:is_derived_from", "deu", "pa"))
        self.motor.kb.append(Relation("eng", "nagware", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("deu", "nagware", "rel:is_derived_from", "eng", "nagw"))
        self.motor.kb.append(Relation("eng", "nag", "rel:has_derived_form", "deu", "hambu"))
        self.motor.kb.append(Relation("eng", "na", "rel:has_derived_form", "eng", "hamburge"))
        self.motor.kb.append(Relation("eng", "hamburger", "rel:is_derived_from", "deu", "nag"))
        self.motor.kb.append(Relation("eng", "hamburg", "rel:is_derived_from", "eng", "ham"))
        self.motor.kb.append(Relation("eng", "hello", "rel:is_derived_from", "fro", "hola"))
        self.motor.kb.append(Relation("eng", "bye", "rel:is_derived_from", "fro", "adios"))
        self.motor.kb.append(Relation("eng", "abc", "rel:is_derived_from", "fro", "asd"))
        self.motor.kb.append(Relation("eng", "dfe", "rel:is_derived_from", "fro", "zxc"))
        """

        # mayor aporte idiomas a otro

        self.motor.kb.append(
            Relation(
                "eng",
                "palabra",
                "rel:is_derived_from",
                "deu",
                "pal"))
        self.motor.kb.append(
            Relation(
                "deu",
                "palabra",
                "rel:is_derived_from",
                "deu",
                "pa"))
        self.motor.kb.append(
            Relation(
                "eng",
                "nagware",
                "rel:is_derived_from",
                "eng",
                "nag"))
        self.motor.kb.append(
            Relation(
                "deu",
                "nagware",
                "rel:is_derived_from",
                "eng",
                "nagw"))
        self.motor.kb.append(
            Relation(
                "eng",
                "nag",
                "rel:has_derived_form",
                "deu",
                "hambu"))
        self.motor.kb.append(
            Relation(
                "eng",
                "na",
                "rel:has_derived_form",
                "eng",
                "hamburge"))
        self.motor.kb.append(
            Relation(
                "eng",
                "hamburger",
                "rel:is_derived_from",
                "deu",
                "nag"))
        self.motor.kb.append(
            Relation(
                "eng",
                "hamburg",
                "rel:is_derived_from",
                "eng",
                "ham"))
        self.motor.kb.append(
            Relation(
                "eng",
                "hello",
                "rel:is_derived_from",
                "fro",
                "hola"))
        self.motor.kb.append(
            Relation(
                "eng",
                "bye",
                "rel:is_derived_from",
                "fro",
                "adios"))
        self.motor.kb.append(
            Relation(
                "eng",
                "abc",
                "rel:is_derived_from",
                "fro",
                "asd"))
        self.motor.kb.append(
            Relation(
                "eng",
                "dfe",
                "rel:is_derived_from",
                "fro",
                "zxc"))

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

        self.salida_operacion.delete('1.0', END)

        if self.radio.get() == "ContarPalabras":
            resultado = self.motor.contador_palabras_comun_idiomas(
                self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            if len(resultado[0].data) > 0:
                self.salida_operacion.insert(
                    "1.0", "Inferencias: \n" + str(resultado[0].data))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Contador de palabras: \n" + str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")

            print("ContarPalabras")
        elif self.radio.get() == "ListarPalabras":
            resultado = self.motor.palabras_comun_idiomas(
                self.palabra1.get(), self.palabra2.get())
            resultado_list = str(resultado)
            if len(resultado[0].data) > 0:
                self.salida_operacion.insert(
                    "1.0", "Inferencias: \n" + str(resultado[0].data))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Lista de palabras: \n" + str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")

            print("ListarPalabras")
        elif self.radio.get() == "IdiomaAporte":
            resultado = self.motor.mayor_aporte_a_idioma(
                self.palabra1.get(), True)
            resultado_list = str(resultado)
            if len(resultado[0]) > 0:
                self.salida_operacion.insert(
                    "1.0", "Inferencias: \n" + str(resultado[0]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Aporte: \n" + str(resultado[2]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Idioma: \n" + str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")

                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")

            print("IdiomaAporte")
        elif self.radio.get() == "IdiomasAporte":
            resultado = self.motor.aporte_idiomas(self.palabra1.get(), True)
            resultado_list = str(resultado)
            if len(resultado[0]) > 0:
                self.salida_operacion.insert(
                    "1.0", "Inferencias: \n" + str(resultado[0]))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Aporte: \n" + str(resultado[2].data))
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Idioma: \n" + str(resultado[1]))
                self.salida_operacion.insert("1.0", "\n")

                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")

            print("IdiomasAporte")

    def abrir_archivo(self):
        # print(fd.askopenfilename)
        archivo = fd.askopenfilename()
        print(archivo)


class Palabras_Idiomas_Frame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fuente = font.Font(weight='bold')

        self.motor = None

        #self.tabs = ttk.Notebook(raiz)
        self.etiq1 = ttk.Label(self, text='Palabra:', font=fuente)
        self.etiq2 = ttk.Label(self, text='Idioma:', font=fuente)

        self.etiq3 = ttk.Label(self, text='Operaciones:', font=fuente)
        self.etiq4 = ttk.Label(self, text='Relaciones:', font=fuente)

        self.radio = StringVar()

        self.radio_etymological_origin_of_txt = StringVar()
        self.radio_has_derived_from_txt = StringVar()
        self.radio_is_derived_from_txt = StringVar()
        self.radio_etymology_txt = StringVar()
        self.radio_etymologically_related_txt = StringVar()
        self.radio_variant_orthography_txt = StringVar()
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

        self.salida_operacion = Text(self, width=50, height=15)
        self.salida_operacion.place(relx=0.06, rely=0.3)

        self.radio_palabras_relacionadas = ttk.Checkbutton(
            self,
            text="¿Palabra relacionada con idioma?",
            variable=self.radio,
            onvalue="PalabraIdioma",
            offvalue="")
        self.radio_idiomas_originados = ttk.Checkbutton(
            self,
            text="¿Palabras en idioma originadas por palabra?",
            variable=self.radio,
            onvalue="IdiomasOriginados",
            offvalue="")
        self.radio_idiomas_relacionados = ttk.Checkbutton(
            self,
            text="¿Idiomas relacionados con palabra?",
            variable=self.radio,
            onvalue="IdiomasRelacionados",
            offvalue="")

        self.radio_etymological_origin_of = ttk.Checkbutton(
            self,
            text="rel:etymological_origin_of",
            variable=self.radio_etymological_origin_of_txt,
            onvalue="rel:etymological_origin_of",
            offvalue="")
        self.radio_has_derived_from = ttk.Checkbutton(
            self,
            text="rel:has_derived_form",
            variable=self.radio_has_derived_from_txt,
            onvalue="rel:has_derived_form",
            offvalue="")
        self.radio_is_derived_from = ttk.Checkbutton(
            self,
            text="rel:is_derived_from",
            variable=self.radio_is_derived_from_txt,
            onvalue="rel:is_derived_from",
            offvalue="")
        self.radio_etymology = ttk.Checkbutton(
            self,
            text="rel:etymology",
            variable=self.radio_etymology_txt,
            onvalue="rel:etymology",
            offvalue="")
        self.radio_etymologically_related = ttk.Checkbutton(
            self,
            text="rel:etymologically_related",
            variable=self.radio_etymologically_related_txt,
            onvalue="rel:etymologically_related",
            offvalue="")
        self.radio_variant_orthography = ttk.Checkbutton(
            self,
            text="rel:variant:orthography",
            variable=self.radio_variant_orthography_txt,
            onvalue="rel:variant:orthography",
            offvalue="")
        self.radio_derived = ttk.Checkbutton(
            self,
            text="rel:derived",
            variable=self.radio_derived_txt,
            onvalue="rel:derived",
            offvalue="")
        self.radio_etymologically = ttk.Checkbutton(
            self,
            text="rel:etymologically",
            variable=self.radio_etymologically_txt,
            onvalue="rel:etymologically",
            offvalue="")

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

        self.palabra1 = StringVar()
        self.palabra2 = StringVar()

        self.entrada_palabra1 = ttk.Entry(
            self, textvariable=self.palabra1, width=30)
        self.entrada_palabra2 = ttk.Entry(
            self, textvariable=self.palabra2, width=30)

        self.separ = ttk.Separator(self, orient=HORIZONTAL)

        self.boton1 = ttk.Button(
            self,
            text="Realizar operación",
            command=self.operar)
        self.boton2 = ttk.Button(self, text="Cancelar", command=quit)

        self.boton_abrir_archivo = ttk.Button(
            self, text="Abrir base", command=self.abrir_archivo)
        self.boton_abrir_archivo.place(relx=0.06, rely=0.23)

        self.entrada_palabra1.place(relx=0.1, rely=0.1)
        self.entrada_palabra2.place(relx=0.4, rely=0.1)
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

        self.motor = MotorLogico("etymwn.tsv", [], [])

        """
         #palabra relacionada con idioma
        self.motor.kb.append(Relation("deu","a","rel:is_derived_from","eng","x"))
        """

        """
            #palabras originadas idioma
        self.motor.kb.append(Relation("eng", "nagware", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("eng", "nag", "rel:has_derived_form", "eng", "hamburger"))
        self.motor.kb.append(Relation("eng", "nag", "rel:has_derived_form", "eng", "hamburg"))
        self.motor.kb.append(Relation("eng", "hamburger", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("eng", "hamburg", "rel:is_derived_from", "eng", "nag"))
        """
        """
            #idiomas relacionados con palabra
        self.motor.kb.append(Relation("eng", "palabra", "rel:is_derived_from", "deu", "pal"))
        self.motor.kb.append(Relation("deu", "palabra", "rel:is_derived_from", "deu", "pa"))
        self.motor.kb.append(Relation("eng", "nagware", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("deu", "nagware", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("eng", "nag", "rel:has_derived_form", "deu", "hamburger"))
        self.motor.kb.append(Relation("eng", "nag", "rel:has_derived_form", "eng", "hamburg"))
        self.motor.kb.append(Relation("eng", "hamburger", "rel:is_derived_from", "eng", "nag"))
        self.motor.kb.append(Relation("eng", "hamburg", "rel:is_derived_from", "eng", "nag"))
        """

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

        self.salida_operacion.delete('1.0', END)

        if self.radio.get() == "PalabraIdioma":
            resultado = self.motor.relacion_palabra_idioma(
                self.palabra1.get(), self.palabra2.get())
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
            resultado = self.motor.palabras_originadas(
                self.palabra1.get(), self.palabra2.get())
            print(resultado)
            resultado_list_inferencias = str(resultado[0].data)
            resultado_list_palabras = str(resultado[1].data)

            if len(resultado[0].data) > 0:
                self.salida_operacion.insert(
                    "1.0", "Inferencias: \n" + resultado_list_inferencias)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Resultados: \n" + resultado_list_palabras)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")

            print("IdiomasOriginados")
        elif self.radio.get() == "IdiomasRelacionados":
            resultado = self.motor.idiomas_relacionados_palabra(
                self.palabra1.get())
            print(resultado)
            resultado_list_inferencias = str(resultado[0].data)
            resultado_list_palabras = str(resultado[1])

            if len(resultado[0].data) > 0:
                self.salida_operacion.insert(
                    "1.0", "Inferencias: \n" + resultado_list_inferencias)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert(
                    "1.0", "Resultados: \n" + resultado_list_palabras)
                self.salida_operacion.insert("1.0", "\n")
                self.salida_operacion.insert("1.0", "True")
                self.salida_operacion.see("end")

            else:
                self.salida_operacion.insert("1.0", "False")
            print("IdiomasRelacionados")

    def abrir_archivo(self):
        # print(fd.askopenfilename)
        archivo = fd.askopenfilename()
        self.motor = MotorLogico("etymwn.tsv", [], [])

        self.motor.kb.append(
            Relation(
                "eng",
                "a",
                "rel:is_derived_from",
                "eng",
                "x"))
        self.motor.kb.append(
            Relation(
                "eng",
                "a",
                "rel:is_derived_from",
                "eng",
                "d"))
        self.motor.kb.append(
            Relation(
                "eng",
                "c",
                "rel:is_derived_from",
                "eng",
                "a"))
        self.motor.kb.append(
            Relation(
                "eng",
                "b",
                "rel:is_derived_from",
                "eng",
                "a"))
        self.motor.kb.append(
            Relation(
                "eng",
                "e",
                "rel:is_derived_from",
                "eng",
                "a"))
        resultado = self.motor.relacion_parent("n", "a")
        print(resultado)

        # print(self.motor.database)
        # self.motor.load_db()
        # print(self.motor.kb)


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
            self.operaciones_palabras_palabras,
            text="Operaciones con palabras",
            padding=10)

        self.operaciones_palabras_idiomas = Palabras_Idiomas_Frame(
            self.notebook)
        self.notebook.add(
            self.operaciones_palabras_idiomas,
            text="Operaciones con palabras/idiomas",
            padding=10)

        self.operaciones_idiomas_idiomas = Idiomas_Idiomas_Frame(self.notebook)
        self.notebook.add(
            self.operaciones_idiomas_idiomas,
            text="Operaciones con idiomas",
            padding=10)

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


# print(motor.relacion_hermandad('hamburger','burger'))
# print(motor.relacion_parent('Hamburg','hamburger'))
# Y =motor.relacion_parent(X,'hamburger')
# Z = motor.relacion_parent(X,'burger')
# print(Y)
# print(Z)
# print(motor.relacion_palabra_idioma('nag','eng'))


#rel = Relation("eng","a","rel:is_derived_from","eng","x")

# print(motor.relacion_parent(Y,'hamburger'))
