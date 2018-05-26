#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:55:38 2018

@author: 08201713
"""

import exer1
import unittest

class TestTam(unittest.TestCase):

    def test_tamanho_correto(self):

        result = exer1.tamanho('abcdefg')
        self.assertEqual(result, 7)

    def test_tamanho_errado_20(self):

        result = exer1.tamanho('abcdefghijklmnopqrstuvxwyz')
        self.assertEqual(result,-1)

    def test_tamanho_errado_0(self):

        result = exer1.tamanho('')
        self.assertEqual(result,-1)

class TestCaract(unittest.TestCase):

    def test_find_certo(self):

        result = exer1.find('abcdefg','c')
        self.assertEqual(result, 2)        

    def test_find_errado(self):

        result = exer1.find('abcdefg','x')
        self.assertEqual(result,-1)

    def test_find_errado_2(self):

        result = exer1.find('abcdefg','cc')
        self.assertEqual(result,-1)

if __name__ == '__main__':
    unittest.main()
