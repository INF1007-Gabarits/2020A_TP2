import math

import numpy as np
import unittest
import os
import sys
from exercice1 import exercice1 as ex1
from exercice2 import exercice2 as ex2
from exercice3 import exercice3 as ex3


class TestExercice1(unittest.TestCase):
    CONST_SIZE = 1000

    def test_tri_dix_elements(self):
        array = np.random.randint(-100, 100, 10)
        isEqual = np.array_equal(np.sort(array), ex1(array))
        self.assertTrue(isEqual)

    def test_tri_complet(self):
        array = np.random.randint(-100, 100, self.CONST_SIZE)
        isEqual = np.array_equal(np.sort(array), ex1(array))
        self.assertTrue(isEqual)


class TestExercice2(unittest.TestCase):
    def test_paranthese_bien_1(self):
        self.assertEqual(ex2("()"), "(.)")

    def test_paranthese_bien_2(self):
        self.assertEqual(ex2("(()())"), "((.)(.))")

    def test_paranthese_bien_3(self):
        self.assertEqual(ex2("(())((()))()"), "((.))(((.)))(.)")

    def test_paranthese_bien_4(self):
        self.assertEqual(ex2("((((((()))))))"), "(((((((.)))))))")

    def test_non_parenthese_1(self):
        value_returned = str(ex2("(((")).lower()
        self.assertIn("corr", value_returned)

    def test_non_parenthese_2(self):
        value_returned = str(ex2(")))")).lower()
        self.assertIn("corr", value_returned)

    def test_non_parenthese_3(self):
        value_returned = str(ex2("((())")).lower()
        self.assertIn("corr", value_returned)

    def test_non_parenthese_4(self):
        value_returned = str(ex2("(()))")).lower()
        self.assertIn("corr", value_returned)


class TestExercice3(unittest.TestCase):
    CONST_GRAVITE = 9.81
    CONST_HAUTEUR = 100.5
    MAX_DIFF = 2  # si les etudiants font h > 0.01 ou h >= 0.01 on ne penalise pas

    def test_rebond_faible(self):
        self.generique_test(self.CONST_HAUTEUR, 0.2)

    def test_rebond_fort(self):
        self.generique_test(self.CONST_HAUTEUR, 0.7)

    def generique_test(self, hauteur_initiale, coefficient_rebond):
        nb_rebonds_attendu = self.verification(hauteur_initiale, coefficient_rebond)
        nb_rebonds_test = ex3(hauteur_initiale, coefficient_rebond)

        diff = abs(nb_rebonds_attendu - nb_rebonds_test)
        self.assertTrue(diff <= self.MAX_DIFF)

    def verification(self, hauteur_initiale, coefficient_rebond):
        h = hauteur_initiale
        nb_rebonds = 0
        while h > 0.01:
            v = math.sqrt(2 * self.CONST_GRAVITE * h)
            v *= coefficient_rebond
            h = v * v / (2 * self.CONST_GRAVITE)
            nb_rebonds += 1
        return nb_rebonds


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
