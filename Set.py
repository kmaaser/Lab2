
# ----------------------------------------------------------------------
# Set.py
# David Reed
# Karenna Maaser
# 1/23/2017
# ----------------------------------------------------------------------

class Set:

    # ------------------------------------------------------------------

    def __init__(self, aSet: list):

        """
        pre: none


        :param aSet: a list of items that are in the set
        """

        """
        pre:
        post: constructs aSet object with specified parameters"""

        self.set = aSet
        self.listOfSet = ()
    # ------------------------------------------------------------------

    def insert(self, item):

        """ adds an item to the list in the set
        """

        self.listOfSet.insert(item)
    # ------------------------------------------------------------------

    def contains(self, thing):
        """

        :param thing:
        :return: returns True or False indicating if the parameter is in the set
        """

        pass
    # ------------------------------------------------------------------

    def isSubsetOf (self, object):

        """

        :param object: Set object
        :return: True if the set is a subset of the parameter set and false otherwise
        """
        pass
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """ returns the number of items in the set

        :return:
        """
        pass
    # ------------------------------------------------------------------

    def __add__(self, other):

        """

        :param other:
        :return: a new Set that is the union of the two sets
        """
        pass
    # ------------------------------------------------------------------

    def __sub__(self, other):

        """

        :param other:
        :return: a new Set which is the difference of the two sets (the items in the left set that are not in the right set)
        """
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
