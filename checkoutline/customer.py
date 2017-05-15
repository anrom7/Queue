"""
File: customer.py
"""
import random

class Customer(object):
    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival, arrivalTime, averageTimePerCustomer):
        """
        Returns a Customer object if the probability of arrival is greater than
        or equal to a random number.
        Otherwise, returns None, indicating no new customer.
        :param probabilityOfNewArrival:
        :type probabilityOfNewArrival:
        :param arrivalTime:
        :type arrivalTime:
        :param averageTimePerCustomer:
        :type averageTimePerCustomer:
        :return:
        :rtype:
        """

        if random.random() <= probabilityOfNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None

    def __init__(self, arrivalTime, serviceNeeded):
        self._arrivalTime = arrivalTime
        self._amountOfServiceNeeded = serviceNeeded

    def arrivalTime(self):
        return self._arrivalTime

    def amountOfServiceNeeded(self):
        return self._amountOfServiceNeeded

    def serve(self):
        """
        Accepts a unit of service from the cashier.
        :return:
        :rtype:
        """
        self._amountOfServiceNeeded -= 1