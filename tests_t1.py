#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:55:38 2018

@author: 08201713
"""

import t1
import unittest

class TestBruto(unittest.TestCase):

    def numero(self):

        result = t1.diaseg(33,11,2000)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
