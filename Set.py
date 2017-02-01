# ----------------------------------------------------------------------
# Set.py
# David Reed
# Karenna Maaser
# 2/1/2017
# ----------------------------------------------------------------------

class Set:

    # ------------------------------------------------------------------

    def __init__(self):

        """
        pre: none


        :param
        """

        """
        pre:
        post: Sets list equal"""

        self.setList = []
    # ------------------------------------------------------------------

    def insert(self, item):

        """ adds an item to the list in the set
        """
        # adds an item to the list
        if item in self.setList:
            pass
        else:
            self.setList.append(item)

    # ------------------------------------------------------------------

    def contains(self, item):
        """

        :param item:
        :return: returns True or False indicating if the parameter is in the set
        """

        # checks to see if item is in list
        if item in self.setList:
            return True
        return False
    # ------------------------------------------------------------------

    def isSubsetOf (self, object):

        """

        :param object: Set object
        :return: True if the set is a subset of the parameter set and false otherwise
        """

        for i in self.setList:
            # checks to see if i is not contained
            if not object.contains(i):
                return False
        return True
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """ returns the number of items in the set

        :return:
        """
        # returns the length of the list
        return len(self.setList)
    # ------------------------------------------------------------------

    def __add__(self, other):

        """

        :param other:
        :return: a new Set that is the union of the two sets
        """
        set = Set()
        for i in self.setList:
            # inserts the items into the new set
            set.insert(i)
        for i in other.setList:
            set.insert(i)

        return set
    # ------------------------------------------------------------------

    def __sub__(self, other):

        """

        :param other:
        :return: a new Set which is the difference of the two sets (the items in the left set that are not in the right set)
        """
        set = Set()
        for i in self.setList:
            if not other.contains(i):
                set.insert(i)
        return set
    # ------------------------------------------------------------------

    def __eq__(self, other):

        """

        :param other:
        :return: True if the Sets are equal to each other and False if they are not
        """


        # checks to see if the lengths and the sets are equal
        if self.isSubsetOf(other) and other.isSubsetOf(self):
                return True
        return False
    # ------------------------------------------------------------------

    def __ne__(self, other):

        """

        :param other:
        :return: True if the Sets are not equal and False if they are
        """
        if not self.isSubsetOf(other) and other.isSubsetOf(self):
                return True
        return False
    # ------------------------------------------------------------------
