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

        # checks to see if item is in the list
        if item in self.setList:
            # if the item is in the list, nothing happens
            pass
        else:
            # if the item is not in the list, it is added to the list
            self.setList.append(item)

    # ------------------------------------------------------------------

    def contains(self, item):
        """

        :param item:
        :return: returns True or False indicating if the parameter is in the set
        """

        # checks to see if item is in list
        if item in self.setList:
            # if item is in list it will return True
            return True
        # if item is not in list, it will return False
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

        # checks the first list
        for i in self.setList:
            # inserts the items into the new set
            set.insert(i)
        # checks the second list
        for i in other.setList:
            # inserts items into the new set
            set.insert(i)

        return set
    # ------------------------------------------------------------------

    def __sub__(self, other):

        """

        :param other:
        :return: a new Set which is the difference of the two sets (the items in the left set that are not in the right set)
        """

        # makes a new set
        set = Set()


        for i in self.setList:
            # checks to see if i is in the other list
            if not other.contains(i):
                set.insert(i)
        return set
    # ------------------------------------------------------------------

    def __eq__(self, other):

        """

        :param other:
        :return: True if the Sets are equal to each other and False if they are not
        """

        # checks to see if the they are subsets of each other
        if self.isSubsetOf(other) and other.isSubsetOf(self):
            return True
        return False
    # ------------------------------------------------------------------

    def __ne__(self, other):

        """

        :param other:
        :return: True if the Sets are not equal and False if they are
        """

        # checks to see if they are not subsets of each other
        if not self.isSubsetOf(other) and not other.isSubsetOf(self):
            return True
        return False
    # ------------------------------------------------------------------
