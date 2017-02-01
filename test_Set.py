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

    def testInset(self):

        # checks to see if it adds something to the set
        set = Set()
        set.insert(2)
        self.assertEqual(set.setList, [2])
        # checks to make sure is does not add duplicates
        set.insert(2)
        self.assertEqual(set.setList, [2])


    def testContains(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)
        self.assertEqual(set.contains(2), True)
        self.assertEqual(set.contains(100), False)

    def testIsSubsetOf(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)

        set2 = Set()
        set2.insert(2)
        set2.insert(3)

        self.assertEqual(set2.isSubsetOf(set), True)

        set2.insert(5)
        self.assertEqual(set2.isSubsetOf(set), False)


    def testLen(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)
        self.assertEqual(len(set), 3)

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

        self.assertEqual(set + set2, set3)

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

    def testEq(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)
        set.insert(5)

        set2 = Set()
        set2.insert(1)
        set2.insert(2)
        set2.insert(3)
        set2.insert(5)

        self.assertEqual(set == set2, True)

    def testNe(self):
        set = Set()
        set.insert(1)
        set.insert(2)
        set.insert(3)
        set.insert(5)

        set2 = Set()
        set2.insert(1)
        set2.insert(6)
        set2.insert(8)
        set2.insert(9)

        self.assertEqual(set != set2, True)

def main(argv):
    unittest.main()

#if __name__ == '__name__':
main(sys.argv)
