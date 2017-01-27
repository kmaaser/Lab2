
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

        self.setList.insert(item)
    # ------------------------------------------------------------------

    def contains(self, item):
        """

        :param item:
        :return: returns True or False indicating if the parameter is in the set
        """

        for i in self.setList:
            # if i is in the set list
            if i.item == item:
                return True
        return False

        pass



    # ------------------------------------------------------------------

    def isSubsetOf (self, object):

        """

        :param object: Set object
        :return: True if the set is a subset of the parameter set and false otherwise
        """

        for i in self.setList:
            if not object.contains(i):
                return False
        return True
        pass
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """ returns the number of items in the set

        :return:
        """

        return len(self.setList)
    # ------------------------------------------------------------------

    def __add__(self, other):

        """

        :param other:
        :return: a new Set that is the union of the two sets
        """

        for i in self.setList:
            if not other.setList.contains(i):
                other.setList.append(i)

        return other
        pass
    # ------------------------------------------------------------------

    def __sub__(self, other):

        """

        :param other:
        :return: a new Set which is the difference of the two sets (the items in the left set that are not in the right set)
        """

        for i in self.setList:
            if self.setList.contains(i):
                other.setList.list.remove(i)

        return other
        pass
    # ------------------------------------------------------------------

    def __eq__(self, other):

        """

        :param other:
        :return: True if the Sets are equal to each other and False if they are not
        """
        pass
    # ------------------------------------------------------------------

    def __ne__(self, other):

        """

        :param other:
        :return: True if the Sets are not equal and False if they are
        """
        pass
    # ------------------------------------------------------------------
