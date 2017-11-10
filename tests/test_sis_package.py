# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:57:31 2017
@author: nicholas

"""
import sys
import logging
import shutil
import time
import os
import unittest

logger = logging

from .context import sis
from sis import sis, multifasta

@unittest.skipIf((sys.version_info[0] != 3) or (sys.version_info[1] < 5),
                 "Subprocess.call among other things wont run if tried " +
                 " with less than python 3.5")
class sisTestCase(unittest.TestCase):
    """ tests for sis.py
    """
    def setUp(self):
        self.startTime = time.time()
        self.to_be_removed = []

    def test_zeros(self):
        """ return an array filled with zeros"""
        self.assertEqual(sis.zeros(7), [0,0,0,0,0,0,0])


    def tearDown(self):
        """ delete temp files if no errors """
        for filename in self.to_be_removed:
            try:
                os.unlink(filename)
            except IsADirectoryError:
                shutil.rmtree(filename)
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

if __name__ == '__main__':
    unittest.main()
