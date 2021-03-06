import pytest
from g05 import *


def test_parent_true():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "a"))

    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "a"))

    resultado = motor.relacion_parent("x", "a")
    assert len(resultado) > 0


def test_parent_false():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "a"))

    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "a"))

    resultado = motor.relacion_parent("d", "e")
    assert len(resultado) == 0


def test_hermandad_true_one_parent():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "y"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))

    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "y", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))

    resultado = motor.relacion_hermandad("c", "d")
    assert len(resultado) > 0


def test_hermandad_false_one_parent():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "y"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))

    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "y", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))

    resultado = motor.relacion_hermandad("a", "d")
    assert len(resultado[0].data) == 0 and len(resultado[1].data) == 0


def test_hermandad_true_two_parent():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "y"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))

    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "y", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))

    resultado = motor.relacion_hermandad("a", "b")
    assert len(resultado) > 0


def test_hermandad_false_two_parent():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "y"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "z"))

    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "y", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "z", "rel:has_derived_form", "eng", "c"))

    resultado = motor.relacion_hermandad("a", "c")
    assert len(resultado[0].data) == 0 and len(resultado[1].data) == 0


def test_tio_true():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "f", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "g", "rel:is_derived_from", "eng", "c"))

    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "f"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "g"))

    resultado = motor.relacion_tio("c", "d")
    assert len(resultado) > 0


def test_tio_false():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "f", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "g", "rel:is_derived_from", "eng", "c"))

    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "f"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "g"))

    resultado = motor.relacion_tio("d", "c")
    assert len(resultado) == 0


def test_primos_primer_nivel_true():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "f", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "g", "rel:is_derived_from", "eng", "d"))

    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "f"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "g"))

    resultado = motor.relacion_primer_primos("e", "g")
    assert len(resultado) > 0


def test_primos_primer_nivel_false():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "f", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "g", "rel:is_derived_from", "eng", "d"))

    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "f"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "g"))

    resultado = motor.relacion_primer_primos("e", "f")
    assert len(resultado[0].data) == 0


def test_primos_diferentes_nivel_true():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "f", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "g", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "h", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "i", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "j", "rel:is_derived_from", "eng", "f"))
    motor.kb.append(Relation("eng", "k", "rel:is_derived_from", "eng", "f"))
    motor.kb.append(Relation("eng", "y", "rel:is_derived_from", "eng", "i"))

    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "f"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "g"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "h"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "i"))
    motor.kb.append(Relation("eng", "f", "rel:has_derived_form", "eng", "j"))
    motor.kb.append(Relation("eng", "f", "rel:has_derived_form", "eng", "k"))
    motor.kb.append(Relation("eng", "i", "rel:has_derived_form", "eng", "y"))

    resultado = motor.relacion_primos_nivel("y", "g")
    assert len(resultado[0].data) > 0 and resultado[1] == 3


def test_primos_mismo_nivel_true():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "f", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "g", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "h", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "i", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "j", "rel:is_derived_from", "eng", "f"))
    motor.kb.append(Relation("eng", "k", "rel:is_derived_from", "eng", "f"))
    motor.kb.append(Relation("eng", "y", "rel:is_derived_from", "eng", "i"))

    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "f"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "g"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "h"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "i"))
    motor.kb.append(Relation("eng", "f", "rel:has_derived_form", "eng", "j"))
    motor.kb.append(Relation("eng", "f", "rel:has_derived_form", "eng", "k"))
    motor.kb.append(Relation("eng", "i", "rel:has_derived_form", "eng", "y"))

    resultado = motor.relacion_primos_nivel("d", "f")
    assert len(resultado[0].data) > 0 and resultado[1] == 1


def test_primos_nivel_false():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("eng", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("eng", "b", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "c", "rel:is_derived_from", "eng", "a"))
    motor.kb.append(Relation("eng", "d", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "e", "rel:is_derived_from", "eng", "b"))
    motor.kb.append(Relation("eng", "f", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "g", "rel:is_derived_from", "eng", "c"))
    motor.kb.append(Relation("eng", "h", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "i", "rel:is_derived_from", "eng", "d"))
    motor.kb.append(Relation("eng", "j", "rel:is_derived_from", "eng", "f"))
    motor.kb.append(Relation("eng", "k", "rel:is_derived_from", "eng", "f"))
    motor.kb.append(Relation("eng", "y", "rel:is_derived_from", "eng", "i"))

    motor.kb.append(Relation("eng", "x", "rel:has_derived_form", "eng", "a"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "b"))
    motor.kb.append(Relation("eng", "a", "rel:has_derived_form", "eng", "c"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "d"))
    motor.kb.append(Relation("eng", "b", "rel:has_derived_form", "eng", "e"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "f"))
    motor.kb.append(Relation("eng", "c", "rel:has_derived_form", "eng", "g"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "h"))
    motor.kb.append(Relation("eng", "d", "rel:has_derived_form", "eng", "i"))
    motor.kb.append(Relation("eng", "f", "rel:has_derived_form", "eng", "j"))
    motor.kb.append(Relation("eng", "f", "rel:has_derived_form", "eng", "k"))
    motor.kb.append(Relation("eng", "i", "rel:has_derived_form", "eng", "y"))

    resultado = motor.relacion_primos_nivel("b", "k")
    assert len(resultado[0].data) == 0


def test_palabra_idioma_true():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("deu", "a", "rel:is_derived_from", "eng", "x"))

    resultado = motor.relacion_palabra_idioma("x", "deu")
    assert len(resultado) > 0


def test_palabra_idioma_false():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(Relation("deu", "a", "rel:is_derived_from", "eng", "x"))
    motor.kb.append(Relation("deu", "b", "rel:is_derived_from", "sco", "y"))

    resultado = motor.relacion_palabra_idioma("b", "eng")
    assert len(resultado) == 0


def test_palabras_originadas():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(
        Relation(
            "eng",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "eng",
            "hamburger"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "eng",
            "hamburg"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburger",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburg",
            "rel:is_derived_from",
            "eng",
            "nag"))

    resultado = motor.palabras_originadas("nag", "eng")
    assert len(resultado[1].data) == 5


def test_idiomas_relacionados_palabra():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(
        Relation(
            "eng",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pal"))
    motor.kb.append(
        Relation(
            "deu",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pa"))
    motor.kb.append(
        Relation(
            "eng",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "deu",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "deu",
            "hamburger"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "eng",
            "hamburg"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburger",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburg",
            "rel:is_derived_from",
            "eng",
            "nag"))

    resultado = motor.idiomas_relacionados_palabra("nag")

    assert resultado[1] == {('deu', 'eng'), ('eng', 'deu'), ('eng', 'eng')}


def test_contador_palabras_comun():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(
        Relation(
            "eng",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pal"))
    motor.kb.append(
        Relation(
            "deu",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pa"))
    motor.kb.append(
        Relation(
            "eng",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "deu",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nagw"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "deu",
            "hambu"))
    motor.kb.append(
        Relation(
            "eng",
            "na",
            "rel:has_derived_form",
            "eng",
            "hamburge"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburger",
            "rel:is_derived_from",
            "deu",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburg",
            "rel:is_derived_from",
            "eng",
            "ham"))

    resultado = motor.contador_palabras_comun_idiomas("eng", "deu")

    assert resultado[1] == 4 


def test_palabras_comun_idiomas():
    motor = MotorLogico("etymwn.tsv", [], [], False)
    motor.kb.append(
        Relation(
            "eng",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pal"))
    motor.kb.append(
        Relation(
            "deu",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pa"))
    motor.kb.append(
        Relation(
            "eng",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "deu",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nagw"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "deu",
            "hambu"))
    motor.kb.append(
        Relation(
            "eng",
            "na",
            "rel:has_derived_form",
            "eng",
            "hamburge"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburger",
            "rel:is_derived_from",
            "deu",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburg",
            "rel:is_derived_from",
            "eng",
            "ham"))
    motor.kb.append(
        Relation(
            "eng",
            "hello",
            "rel:is_derived_from",
            "ita",
            "hola"))

    resultado = motor.palabras_comun_idiomas("eng", "deu")

    assert resultado[1] == {'palabra', 'nagware', 'nag'}


def test_mayor_aporte_idioma():
    motor = MotorLogico("etymwn.tsv", [], ["eng", "deu", "fro"])
    motor.kb.append(
        Relation(
            "eng",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pal"))
    motor.kb.append(
        Relation(
            "deu",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pa"))
    motor.kb.append(
        Relation(
            "eng",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "deu",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nagw"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "deu",
            "hambu"))
    motor.kb.append(
        Relation(
            "eng",
            "na",
            "rel:has_derived_form",
            "eng",
            "hamburge"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburger",
            "rel:is_derived_from",
            "deu",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburg",
            "rel:is_derived_from",
            "eng",
            "ham"))
    motor.kb.append(
        Relation(
            "eng",
            "hello",
            "rel:is_derived_from",
            "fro",
            "hola"))
    motor.kb.append(
        Relation(
            "eng",
            "bye",
            "rel:is_derived_from",
            "fro",
            "adios"))
    motor.kb.append(
        Relation(
            "eng",
            "abc",
            "rel:is_derived_from",
            "fro",
            "asd"))
    motor.kb.append(
        Relation(
            "eng",
            "dfe",
            "rel:is_derived_from",
            "fro",
            "zxc"))

    resultado = motor.mayor_aporte_a_idioma("eng", True)

    assert resultado[1] == 'deu' and resultado[2] == 0.42857142857142855


def test_aporte_idiomas():
    motor = MotorLogico("etymwn.tsv", [], ["eng", "deu", "fro"])
    motor.kb.append(
        Relation(
            "eng",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pal"))
    motor.kb.append(
        Relation(
            "deu",
            "palabra",
            "rel:is_derived_from",
            "deu",
            "pa"))
    motor.kb.append(
        Relation(
            "eng",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nag"))
    motor.kb.append(
        Relation(
            "deu",
            "nagware",
            "rel:is_derived_from",
            "eng",
            "nagw"))
    motor.kb.append(
        Relation(
            "eng",
            "nag",
            "rel:has_derived_form",
            "deu",
            "hambu"))
    motor.kb.append(
        Relation(
            "eng",
            "na",
            "rel:has_derived_form",
            "eng",
            "hamburge"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburger",
            "rel:is_derived_from",
            "deu",
            "nag"))
    motor.kb.append(
        Relation(
            "eng",
            "hamburg",
            "rel:is_derived_from",
            "eng",
            "ham"))
    motor.kb.append(
        Relation(
            "eng",
            "hello",
            "rel:is_derived_from",
            "fro",
            "hola"))
    motor.kb.append(
        Relation(
            "eng",
            "bye",
            "rel:is_derived_from",
            "fro",
            "adios"))
    motor.kb.append(
        Relation(
            "eng",
            "abc",
            "rel:is_derived_from",
            "fro",
            "asd"))
    motor.kb.append(
        Relation(
            "eng",
            "dfe",
            "rel:is_derived_from",
            "fro",
            "zxc"))

    resultado = motor.aporte_idiomas("eng", True)

    assert resultado[1] == [
        'deu', 'fro'] and resultado[2] == [
        (0.42857142857142855, 0.5714285714285714)]
