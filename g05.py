
import csv
from pyDatalog import pyDatalog, pyEngine
from pyDatalog.pyDatalog import assert_fact, load, ask

import logging
pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

class MotorLogico(object):
    def __init__(self, database,valid_relations, lan):
        self.valid_relations = valid_relations
        self.kb = []
        self.lan = lan
        self.database = database
       
##        self.kb.append(Relation("eng", "nagware", "rel:is_derived_from", "eng", "nag"))
##        self.kb.append(Relation("eng", "nag", "rel:has_derived_form", "eng", "hamburger"))
##        self.kb.append(Relation("eng", "nag", "rel:has_derived_form", "eng", "hamburg"))
##        self.kb.append(Relation("eng", "hamburger", "rel:is_derived_from", "eng", "nag"))
##        self.kb.append(Relation("eng", "hamburg", "rel:is_derived_from", "eng", "nag"))
        if(lan == []):
            self.load_db()
        else:
            self.load_db_by_language()


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
        Y = pyDatalog.Variable()
        (Relation.parent(X, palabra1, palabra2))
        return X

    def load_db_by_language(self):
        fd = open(self.database, encoding="utf8")
        rd = csv.reader(fd, delimiter="\t")
        cont = 0
        for row in rd:
          r_type = row[1]
          if(self.valid_relations != [] and r_type not in self.valid_relations):
              continue
          f_lan = row[0][0:3]
          s_lan = row[2][0:3]
          if(f_lan != self.lan and s_lan != self.lan):
              continue
        
          f_word = row[0][5:]   
          s_word = row[2][5:]
          self.kb.append(Relation(f_lan, f_word, r_type, s_lan, s_word))
          cont += 1
        print(str(cont)+" filas leidas")
        
    
    def load_db(self):
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
        #Relation.parent(X,Word1,Word2) <= (Relation.first_word[X]==Word1) & (Relation.second_word[X]==Word2) & (Relation.r_type[X]=='rel:etymologically')
        #Relation.parent(X,Word1,Word2) <= (Relation.first_word[X]==Word2) & (Relation.second_word[X]==Word1) & (Relation.r_type[X]=='rel:etymologically_related')
        #Relation.parent(X,Word1,Word2) <= (Relation.first_word[X]==Word1) & (Relation.second_word[X]==Word2) & (Relation.r_type[X]=='rel:etymological_origin_of')
        #Relation.parent(X,Word1,Word2) <= (Relation.first_word[X]==Word2) & (Relation.second_word[X]==Word1) & (Relation.r_type[X]=='rel:etymology')
        Relation.parent(X,Word1,Word2) <= (Relation.second_word[X]==Word2) & (Relation.first_word[X]==Word1) & (Relation.r_type[X]=='rel:has_derived_form')
        Relation.parent(X,Word1,Word2) <= (Relation.first_word[X]==Word2) & (Relation.second_word[X]==Word1) & (Relation.r_type[X]=='rel:is_derived_from')
        #Relation.parent(X,Word1,Word2) <= (Relation.first_word[X]==Word2) & (Relation.second_word[X]==Word1) & (Relation.r_type[X]=='rel:variant:ortography')
        Relation.siblings(X,Y,Word1,Word2) <= Relation.parent(X,Z,Word1) & Relation.parent(Y,Z,Word2)
        #Determinar si una palabra esta relacionada con un idioma o no
        
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.first_word[X]==Word) & (Relation.first_lan[X]==Lan) 
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.second_word[X]==Word) & (Relation.second_lan[X]==Lan)
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.second_word[X]==Word) &(Relation.first_lan[X]==Lan)
        (Relation.hasLanAndWord[X,Lan,Word]==True) <= (Relation.first_word[X]==Word) & (Relation.second_lan[X]==Lan) 
        
motor = MotorLogico("etymwn.tsv",["rel:has_derived_form"],[])
Y = pyDatalog.Variable()
X = pyDatalog.Variable()
Z = pyDatalog.Variable()
print(motor.relacion_hermandad('hamburger','burger'))
#print(motor.relacion_parent('Hamburg','hamburger'))
#Y =motor.relacion_parent(X,'hamburger')
#Z = motor.relacion_parent(X,'burger')
#print(Y)
#print(Z)
#print(motor.relacion_palabra_idioma('nag','eng'))




#print(motor.relacion_parent(Y,'hamburger'))




