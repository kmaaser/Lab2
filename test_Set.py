# ----------------------------------------------------------------------
# test_Set.py
# David Reed
# Karenna Maaser
# 2/1/2017
# ----------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '..')
from Set import *

class SetTest(unittest.TestCase):

    # ----------------------------------------------------------------------

    def testInset(self):

        # checks to see if it adds something to the set
        set = Set()
        set.insert(2)
        self.assertEqual(set.setList, [2])
        set.insert(3)
        self.assertEqual(set.setList, [2, 3])
        # checks to make sure ir does not add duplicates
        set.insert(2)
        self.assertEqual(set.setList, [2, 3])
    # ----------------------------------------------------------------------

    def testContains(self):

        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)
        # Checks to see if 2 is in the set and will return true
        self.assertEqual(set.contains(2), True)
        # makes sure that 100 is not in the set and will return false
        self.assertEqual(set.contains(100), False)
    # ----------------------------------------------------------------------

    def testIsSubsetOf(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)

        set2 = Set()
        set2.insert(2)
        set2.insert(3)

        # checks if set 2 is a subset of set, returns true
        self.assertEqual(set2.isSubsetOf(set), True)

        set2.insert(5)

        # after inserting a number, makes sure that set2 is not a sub set of set, return false
        self.assertEqual(set2.isSubsetOf(set), False)
    # ----------------------------------------------------------------------


    def testLen(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)

        # makes sure it returns the right length
        self.assertEqual(len(set), 3)
    # ----------------------------------------------------------------------

    def testAdd(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)

        set2 = Set()
        set2.insert(1)
        set2.insert(3)
        set2.insert(4)

        set3 = Set()
        set3.insert(1)
        set3.insert(2)
        set3.insert(3)
        set3.insert(4)

        # makes sure it is adding correctly
        self.assertEqual(set + set2, set3)
        self.assertEqual(set + set, set)
    # ----------------------------------------------------------------------

    def testSub(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)
        set.insert(5)

        set2 = Set()
        set2.insert(1)
        set2.insert(3)
        set2.insert(4)

        set3 = Set()
        set3.insert(2)
        set3.insert(5)

        self.assertEqual(set - set2, set3)
    # ----------------------------------------------------------------------

    def testEq(self):
        set1 = Set()
        set1.insert(1)
        set1.insert(2)
        set1.insert(3)
        set1.insert(5)

        set2 = Set()
        set2.insert(1)
        set2.insert(2)
        set2.insert(3)
        set2.insert(5)

        # checks to see if the sets are equal
        self.assertEqual(set1 == set2, True)

        set3 = Set()
        set3.insert(1)
        set3.insert(2)
        set3.insert(3)
        set3.insert(5)

        set4 = Set()
        set4.insert(3)
        set4.insert(6)
        set4.insert(8)
        set4.insert(9)

        # checks to see if the lists are equal
        # they are not so it will return false
        self.assertEqual(set3 == set4, False)
    # ----------------------------------------------------------------------

    def testNe(self):
        set1 = Set()
        set1.insert(1)
        set1.insert(2)
        set1.insert(3)
        set1.insert(5)

        set2 = Set()
        set2.insert(7)
        set2.insert(6)
        set2.insert(8)
        set2.insert(9)

        # checks to see if the lists are not equal
        self.assertEqual(set1 != set2, True)

        set3 = Set()
        set3.insert(1)
        set3.insert(2)
        set3.insert(3)
        set3.insert(5)

        set4 = Set()
        set4.insert(1)
        set4.insert(2)
        set4.insert(3)
        set4.insert(5)

        # checks to see if they are not equal
        # the sets are equal so it will return false
        self.assertEqual(set3 != set4, False)
    # ----------------------------------------------------------------------

def main(argv):
    unittest.main()

#if __name__ == '__name__':
main(sys.argv)
