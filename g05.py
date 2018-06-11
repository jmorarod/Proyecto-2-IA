
import csv
from pyDatalog import pyDatalog
from pyDatalog.pyDatalog import assert_fact, load, ask

class MotorLogico(object):
    def __init__(self, database,valid_relations):
        self.valid_realtions = valid_relations
        self.kb = []
        fd = open(database, encoding="utf8")
        rd = csv.reader(fd, delimiter="\t")
        for row in rd:
          f_lan = row[0][0:3]
          f_word = row[0][5:]
          r_type = row[1]
          s_lan = row[2][0:3]
          s_word = row[2][5:]
          self.kb.append(Relation(f_lan, f_word, r_type, s_lan, s_word))

    def hermandad(self, palabra1, palabra2):
        X = pyDatalog.Variable()
        Relation.first_lan[X]=='eng'
        print(X)

class Relation(pyDatalog.Mixin):
    def __init__(self, first_lan, first_word, relation_type, second_lan, second_word):
        super(Relation, self).__init__()
        self.first_lan = first_lan
        self.first_word = first_word
        self.relation_type = relation_type
        self.second_lan = second_lan
        self.second_word = second_word
    def __repr__(self):
        return self.first_lan + ": " + self.first_word + " " + self.relation_type + " " + self.second_lan + ": " + self.second_word
    
        


    #Relation.first_lan[X]=='aaq'
    #print(X)


