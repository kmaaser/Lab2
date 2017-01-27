
# ----------------------------------------------------------------------
# Set.py
# David Reed
# Karenna Maaser
# 1/23/2017
# ----------------------------------------------------------------------

class Set:

    # ------------------------------------------------------------------

    def __init__(self, setList):

        """
        pre: none


        :param
        """

        """
        pre:
        post: Sets list equal"""

        self.setList = setList
    # ------------------------------------------------------------------

    def insert(self, item):

        """ adds an item to the list in the set
        """
        # adds an item to the list
        self.setList.insert(item)
    # ------------------------------------------------------------------

    def contains(self, item):
        """

        :param item:
        :return: returns True or False indicating if the parameter is in the set
        """

        # Check to see if the types are the same
        if type(self.setList) == type(item):
            for i in self.setList:
                # if i is in the set list
                if i.item == item:
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

        for i in self.setList:
            # checks to see if i is in the other list
            if not other.setList.contains(i):
                # if i is not in the other list, it is added to the other list
                other.setList.append(i)

        return other
    # ------------------------------------------------------------------

    def __sub__(self, other):

        """

        :param other:
        :return: a new Set which is the difference of the two sets (the items in the left set that are not in the right set)
        """
        newList = self.setList
        for i in newList:
            if other.setList.contains(i):
                newList.remove(i)

        return Set(newList)
    # ------------------------------------------------------------------

    def __eq__(self, other):

        """

        :param other:
        :return: True if the Sets are equal to each other and False if they are not
        """

        # makes the lengths of the lists
        a = len(self.setList)
        b = len(other.setList)

        # checks to see if the lengths and the sets are equal
        if a == b and self.setList.isSubsetOf(other.setList) and other.setList.isSubsetOf(self.setList):
                return True
        return False
    # ------------------------------------------------------------------

    def __ne__(self, other):

        """

        :param other:
        :return: True if the Sets are not equal and False if they are
        """
        pass
    # ------------------------------------------------------------------
