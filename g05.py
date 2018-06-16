
import csv

from pyDatalog.pyDatalog import assert_fact, load, ask, clear
from pyDatalog import pyDatalog, pyEngine

import logging
pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

class MotorLogico(object):
    def __init__(self, database,valid_relations, lan, load_database = False):
        self.valid_relations = valid_relations
        self.kb = []
        self.lan = lan
        self.database = database
        #pyDatalog.clear()
        self.kb.append(Relation("eng", "palabra", "rel:etymology", "eng", "pal"))
        self.kb.append(Relation("deu", "pala", "rel:etymology", "eng", "pal"))
        self.kb.append(Relation("deu", "palata", "rel:etymology", "eng", "pal"))
        self.kb.append(Relation("deu", "pollo", "rel:etymology", "deu", "pal"))
        self.kb.append(Relation("deu", "polloo", "rel:etymology", "deu", "palabra"))
        self.kb.append(Relation("eng", "palabra", "rel:is_derived_from", "sco", "pal"))
##        self.kb.append(Relation("deu", "pala", "rel:is_derived_from", "eng", "palabra"))
##        self.kb.append(Relation("deu", "palata", "rel:is_derived_from", "eng", "pala"))
##        self.kb.append(Relation("deu", "pollo", "rel:is_derived_from", "eng", "palata"))
##        self.kb.append(Relation("deu", "palabra", "rel:is_derived_from", "deu", "pa"))
##        self.kb.append(Relation("eng", "nagware", "rel:is_derived_from", "eng", "nag"))
##        self.kb.append(Relation("deu", "nagware", "rel:is_derived_from", "eng", "nag"))
##        self.kb.append(Relation("eng", "nag", "rel:has_derived_form", "deu", "hamburger"))
##        self.kb.append(Relation("eng", "nag", "rel:has_derived_form", "eng", "hamburg"))
##        self.kb.append(Relation("eng", "hamburger", "rel:is_derived_from", "eng", "nag"))
##        self.kb.append(Relation("eng", "hamburg", "rel:is_derived_from", "eng", "nag"))
        try:
            if(load_database):
                if(lan == []):
                    self.load_db()
                else:
                    self.load_db_by_language()
        except:
            self.kb = []

    
    def relacion_palabra_idioma(self, palabra, idioma):
        X = pyDatalog.Variable()
        Relation.hasLanAndWord[X,idioma, palabra]
        return X
      
        
    def relacion_hermandad(self, palabra1, palabra2):
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Relation.siblings(X,Y,palabra1, palabra2)
        return X,Y
    
    def relacion_parent(self, palabra1, palabra2):
        X = pyDatalog.Variable()
        (Relation.parent(X, palabra1, palabra2))
        return X

    def palabras_originadas(self,palabra,idioma):
        X = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        Relation.originatedWords(X,palabra,idioma,Result)
        return Result
    
    def idiomas_relacionados_palabra(self, palabra):
        X = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        Relation.lanByWord(X,palabra,Result)
        Result = set(eval(str(Result)))
        return X,Result
    
    def palabras_comun_idiomas(self, idioma1, idioma2):
        returnList = []
        X = self.palabras_comun_idiomas_aux(idioma1, idioma2)
        X = set(eval(str(X)))
        return X
            
    def palabras_comun_idiomas_aux(self, idioma1, idioma2):
        X = pyDatalog.Variable()
        Y = pyDatalog.Variable()
        Z = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        Relation.wordInCommon(X,Y,idioma1,idioma2,Z)
        return X,Z
        
    
    def contador_palabras_comun_idiomas(self, idioma1, idioma2):
        
        return len(self.palabras_comun_idiomas_aux(idioma1, idioma2)[1])

    
    def aporte_idiomas(self,idioma):
        if(self.lan == []):
            return self.aporte_idiomas_aux(idioma,self.get_idiomas_file)
        else:
            return self.aporte_idiomas_aux(idioma,self.lan)
        
    def aporte_idiomas_aux(self,idioma,idiomas):
        X = pyDatalog.Variable()
        Result = pyDatalog.Variable()
        inferences=[]
        percentages=[]
        total = 0
        for i in idiomas:
            if(i!=idioma):
                inferences += [Relation.proportionPerLan(X,idioma,i)]#hacer que si devolvió algo entonces agregar i a results
                #if(len(Result)>0):
                    #results+=[[lan,Result]]
                    #total += len(Result)
                    #percentages+=[len(Result)]
        #percentages = self.lista_porcentaje(percentages,total)
        #return results,percentages
        return results
    
        

    def get_idiomas_file():
        try:
            idiomas_file = open("lan.txt","r")
            idiomas = []
            for row in idiomas_file:
                idiomas += [row.rstrip()]
            return idiomas
        except:
            return []
        
    def lista_porcentaje(self,lista,total):
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
        print(str(cont)+" filas leidas")

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
          if([f_word,f_lan] not in words ):
              words.append([f_word,f_lan])
              add_to_kb = True
          if([s_word,s_lan] not in words):
              words.append([s_word,s_lan])
              add_to_kb = True
          if(add_to_kb):
              self.kb.append(Relation(f_lan, f_word, r_type, s_lan, s_word))
              cont += 1
        print(str(cont)+" relaciones agregadas a kb")
    
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
        

class Relation(pyDatalog.Mixin):
    def __init__(self, first_lan, first_word, relation_type, second_lan, second_word):
        super(Relation, self).__init__()
        self.first_lan = first_lan
        self.first_word = first_word
        self.r_type = relation_type
        self.second_lan = second_lan
        self.second_word = second_word
    def __repr__(self):
        return self.first_lan + ": " + self.first_word + " " + self.r_type + " " + self.second_lan + ": " + self.second_word
    @pyDatalog.program()
    def _():
        
        #Determinar si dos palabras son hermanas
        Relation.parent(X,Word1,Word2) <=  (Relation.second_word[X]==Word2) & (Relation.first_word[X]==Word1) & (Relation.r_type[X]=='rel:derived')
        Relation.parent(X,Word1,Word2) <= (Relation.second_word[X]==Word2) & (Relation.first_word[X]==Word1) & (Relation.r_type[X]=='rel:has_derived_form')
        Relation.parent(X,Word1,Word2) <= (Relation.first_word[X]==Word2) & (Relation.second_word[X]==Word1) & (Relation.r_type[X]=='rel:is_derived_from')
        Relation.siblings(X,Y,Word1,Word2) <= Relation.parent(X,Z,Word1) & Relation.parent(Y,Z,Word2)
        #Determinar si una palabra esta relacionada con un idioma o no
        
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.first_word[X]==Word) & (Relation.first_lan[X]==Lan) 
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.second_word[X]==Word) & (Relation.second_lan[X]==Lan)
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.second_word[X]==Word) &(Relation.first_lan[X]==Lan)
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.first_word[X]==Word) & (Relation.second_lan[X]==Lan) 
        #Palabras originadas por otra
        Relation.originatedWords(X,Word,Lan,Result) <= (Relation.second_word[X]==Word) & (Relation.second_lan[X]==Lan) & (Relation.r_type[X]=='rel:is_derived_from') & ((Relation.first_word[X],Relation.first_lan[X])==Result)
        Relation.originatedWords(X,Word,Lan,Result) <= (Relation.first_word[X]==Word) & (Relation.first_lan[X]==Lan) & (Relation.r_type[X]=='rel:has_derived_form') & ((Relation.second_word[X],Relation.second_lan[X])==Result)
        Relation.originatedWords(X,Word,Lan,Result) <= (Relation.second_word[X]==Word) & (Relation.second_lan[X]==Lan) & (Relation.r_type[X]=='rel:etymology') & ((Relation.first_word[X],Relation.first_lan[X])==Result)
        Relation.originatedWords(X,Word,Lan,Result) <= (Relation.first_word[X]==Word) & (Relation.first_lan[X]==Lan) & (Relation.r_type[X]=='rel:etymological_origin_of') & ((Relation.second_word[X],Relation.second_lan[X])==Result)
        Relation.originatedWords(X,Word,Lan,Result) <= (Relation.first_word[X]==Word) & (Relation.first_lan[X]==Lan) & (Relation.r_type[X]=='rel:variant:orthography') & ((Relation.second_word[X],Relation.second_lan[X])==Result)
        #Idiomas relacionados con una palabra
        Relation.lanByWord(X,Word,Result) <= (Relation.second_word[X]==Word) & ((Relation.first_lan[X],Relation.second_lan[X])==Result)
        Relation.lanByWord(X,Word,Result) <= (Relation.first_word[X]==Word) & ((Relation.first_lan[X],Relation.second_lan[X])==Result)
        #Palabras comunes entre dos idiomas(Contar)
        (Relation.countWordInCommon[X,Y,Lan1,Lan2]==len_(Y)) <= (Relation.second_word[X] == Relation.second_word[Y]) & (Relation.second_lan[X]==Lan1) & (Relation.second_lan[Y]==Lan2) & (X!=Y)
        (Relation.countWordInCommon[X,Y,Lan1,Lan2]==len_(Y)) <= (Relation.first_word[X] == Relation.first_word[Y]) & (Relation.first_lan[X]==Lan1) & (Relation.first_lan[Y]==Lan2) & (X!=Y)
        (Relation.countWordInCommon[X,Y,Lan1,Lan2]==len_(Y)) <= (Relation.second_word[X] == Relation.first_word[Y]) &  (Relation.second_lan[X]==Lan1) & (Relation.first_lan[Y]==Lan2) & (X!=Y)
        (Relation.countWordInCommon[X,Y,Lan1,Lan2]==len_(Y)) <= (Relation.second_word[X] == Relation.first_word[Y]) &  (Relation.second_lan[X]==Lan2) & (Relation.first_lan[Y]==Lan1) & (X!=Y)
        #Palabras comunes entre dos idiomas(Listar)
        Relation.wordInCommon(X,Y,Lan1,Lan2,Z) <= (Relation.second_word[X] == Relation.second_word[Y]) & (Relation.second_lan[X]==Lan1) & (Relation.second_lan[Y]==Lan2) & (X!=Y)& (Relation.second_word[X] == Z) 
        Relation.wordInCommon(X,Y,Lan1,Lan2,Z) <= (Relation.first_word[X] == Relation.first_word[Y])   & (Relation.first_lan[X]==Lan1) & (Relation.first_lan[Y]==Lan2)  & (X!=Y) & (Relation.first_word[X] == Z)
        Relation.wordInCommon(X,Y,Lan1,Lan2,Z) <= (Relation.second_word[X] == Relation.first_word[Y]) &  (Relation.second_lan[X]==Lan1) & (Relation.first_lan[Y]==Lan2)   & (X!=Y) & (Relation.second_word[X] == Z)
        Relation.wordInCommon(X,Y,Lan1,Lan2,Z) <= (Relation.second_word[X] == Relation.first_word[Y]) &  (Relation.second_lan[X]==Lan2) & (Relation.first_lan[Y]==Lan1)   & (X!=Y) & (Relation.second_word[X] == Z)
        #Aporte a idioma(Listar)
        Relation.proportionPerLan(X,BaseLan,GLan) <= (Relation.first_lan[X]==BaseLan) & (Relation.second_lan[X]==GLan) & (Relation.r_type[X]=='rel:etymology')
        Relation.proportionPerLan(X,BaseLan,GLan) <= (Relation.first_lan[X]==GLan) & (Relation.second_lan[X]==BaseLan) & (Relation.r_type[X]=='rel:etymological_origin_of') 
        Relation.proportionPerLan(X,BaseLan,GLan) <= (Relation.first_lan[X]==GLan) & (Relation.second_lan[X]==BaseLan) & (Relation.r_type[X]=='rel:variant:orthography')
        Relation.proportionPerLan(X,BaseLan,GLan) <= (Relation.second_lan[X]==GLan) & (Relation.first_lan[X]==BaseLan) & (Relation.r_type[X]=='rel:has_derived_form')
        Relation.proportionPerLan(X,BaseLan,GLan) <= (Relation.first_lan[X]==BaseLan) & (Relation.second_lan[X]==GLan) & (Relation.r_type[X]=='rel:is_derived_from')
        Relation.proportionPerLan(X,BaseLan,GLan) <= (Relation.second_lan[X]==GLan) & (Relation.first_lan[X]==BaseLan) & (Relation.r_type[X]=='rel:derived')

motor = MotorLogico("etymwn.tsv",[],["eng","deu","sco"])
Y = pyDatalog.Variable()
X = pyDatalog.Variable()
Z = pyDatalog.Variable()
def funcion():
    #motor = MotorLogico("etymwn.tsv",["rel:has_derived_form"],[])
    return motor.aporte_idiomas("eng")
#print(motor.relacion_hermandad('hamburger','burger'))
#print(motor.relacion_parent('Hamburg','hamburger'))
#Y =motor.relacion_parent(X,'hamburger')
#Z = motor.relacion_parent(X,'burger')
#print(Y)
#print(Z)
#print(motor.relacion_palabra_idioma('nag','eng'))




#print(motor.relacion_parent(Y,'hamburger'))




