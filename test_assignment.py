import math

import numpy as np
import unittest
import os
import sys
import json
from exercice1 import exercice1 as ex1
from exercice2 import exercice2 as ex2
from exercice3 import exercice3 as ex3
from exercice4 import exercice4 as ex4
from exercice5 import multiplierMatrices as ex5
from exercice6 import createVocabulary as ex6


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
class TestExercice4(unittest.TestCase):
   def test_pie_is_well_aproximed(self):
        self.assertAlmostEqual(ex4()[0],3.141, delta = 0.001)


class TestExercice5(unittest.TestCase):
   A = ([[1, 2], [1, 5]])
   B = ([[1, 2], [1, 6], [3, 8]])
   C = ([[1], [6]])

   def test_multiyply_matrix_with_uncompatible_size_1(self):
        isEqual = np.array_equal(ex5(self.A, self.B), [[0.0, 0.0], [0.0, 0.0]])
        self.assertTrue(isEqual)

   def test_multiyply_matrix_with_uncompatible_size_2(self):
        isEqual = np.array_equal(ex5(self.C, self.A), [[0.0, 0.0], [0.0, 0.0]])
        self.assertTrue(isEqual)

   def test_multiyply_matrix_with_compatible_size_1(self):
        isEqual = np.array_equal(ex5(self.B, self.A), [[3, 12], [7, 32], [11, 46]])
        self.assertTrue(isEqual)

   def test_multiyply_matrix_with_compatible_size_2(self):
        isEqual = np.array_equal(ex5(self.A, self.C), [[13], [31]])
        self.assertTrue(isEqual)

class TestExercice6(unittest.TestCase):

   def setUp(self):
        self.spam_ham_words = ["portfolio","new","user","joint", "popular"]

        self.spam_words = {"subito": 2.0267120650169232e-05, "guatemala": 2.0267120650169232e-05, "electromagnet": 2.0267120650169232e-05,
                     "postcard": 0.0002837396891023692, "valedictori": 2.0267120650169232e-05 }

        self.ham_words = {"practition": 5.174537137653037e-05, "marino": 1.0349074275306073e-05, "highpointtravel": 1.0349074275306073e-05,
                    "atm": 1.0349074275306073e-05, "alan": 6.209444565183644e-05}
        ex6()
        self.emails = {}
        with open("results.json") as json_data:
            self.emails = json.load(json_data)

        self.principal_keys = self.emails.keys()
        self.spam_dict = {}
        self.ham_dict = {}
        for element in self.principal_keys:
            if ('spam' in element.lower()):
                self.spam_dict = self.emails[element];
            if ('ham' in element.lower()):
                self.ham_dict = self.emails[element];

   def principal_keys_are_in_the_dict(self):
        ham_key = False
        spam_key = False
        for element in self.principal_keys:
            if (('ham' in element.lower())):
                ham_key = True
            if (('spam' in element.lower())):
                spam_key = True
        return ham_key and spam_key

   def spam_keys_are_in_dict(self):
        if not self.principal_keys_are_in_the_dict():
            return False
        spam_keys = self.spam_dict.keys()
        for element in self.spam_ham_words + list(self.spam_words.keys()):
            if (element not in spam_keys):
                return False
        return True

   def ham_keys_are_in_dict(self):
        if not self.principal_keys_are_in_the_dict():
            return False
        ham_keys = self.ham_dict.keys()
        for element in self.spam_ham_words + list(self.ham_words.keys()):
            if (element not in ham_keys):
                return False
        return True

   def test_spam_keys_are_in_dict(self):
        self.assertTrue(self.spam_keys_are_in_dict())

   def test_ham_keys_are_in_dict(self):
        self.assertTrue(self.ham_keys_are_in_dict())

   def test_spam_keys_should_not_be_in_ham_dict(self):
        if not self.principal_keys_are_in_the_dict():
            self.assertTrue(False)
            return
        ham_keys = self.ham_dict.keys()
        for element in self.spam_words:
            key_not_exist = element not in ham_keys
            key_give_0_prop = False
            if element in ham_keys:
                key_give_0_prop = self.ham_dict[element] == 0
            self.assertTrue(key_give_0_prop or key_not_exist )

   def test_ham_keys_should_not_be_in_spam_dict(self):
        if not self.principal_keys_are_in_the_dict():
            self.assertTrue(False)
            return
        spam_keys = self.spam_dict.keys()
        for element in self.ham_words:
            key_not_exist = element not in spam_keys
            key_give_0_prop = False
            if element in spam_keys:
                key_give_0_prop = self.spam_dict[element] == 0
            self.assertTrue(key_give_0_prop or key_not_exist )

   def test_spam_prob_are_correct(self):
        if not self.spam_keys_are_in_dict():
            self.assertTrue(False)
            return
        for element in self.spam_words:
            self.assertAlmostEqual(self.spam_dict[element], self.spam_words[element], places=9)

   def test_ham_prob_are_correct(self):
        if not self.ham_keys_are_in_dict():
            self.assertTrue(False)
            return
        for element in self.ham_words:
            self.assertAlmostEqual(self.ham_dict[element], self.ham_words[element], places=9)

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
