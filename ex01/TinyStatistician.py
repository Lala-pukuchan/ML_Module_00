import numpy as np
import math


class TinyStatistician:
    # staticmethod is callable without instantiating the class.
    @staticmethod
    def mean(data):
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        total_sum = 0
        for value in data:
            total_sum += value
        return total_sum / len(data)

    @staticmethod
    def median(data):
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        sorted_data = sorted(data)
        mid_index = len(sorted_data) // 2
        if len(sorted_data) % 2 == 1:
            return float(sorted_data[mid_index])
        else:
            return (sorted_data[mid_index] + sorted_data[mid_index - 1]) / 2

    @staticmethod
    def percentile(data, percent):
        # input validation
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        # sort data
        sorted_data = sorted(data)

        # take the length and adjust for index
        n = len(sorted_data)

        index = int(np.ceil(0.01 * percent * n)) - 1

        # return the existing value in an array
        return sorted_data[index]

    @staticmethod
    def quartile(data):
        # input validation
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        # sort data
        sorted_data = sorted(data)

        # take the length and adjust for index
        n = len(sorted_data)
        n -= 1

        # calculate quartile point
        q1_point = 0.25 * (n)
        q3_point = 0.75 * (n)

        # round up for getting index
        q1_index = int(round(q1_point))
        q3_index = int(round(q3_point))

        # return the existing value in an array
        return [sorted_data[q1_index], sorted_data[q3_index]]

    @staticmethod
    def var(data):
        # input validation
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        # get mean data
        mean = TinyStatistician.mean(data)

        # sum up the squared of diff
        diff = 0
        for elem in data:
            diff += (elem - mean) ** 2

        # divide with len
        variance = diff / (len(data) - 1)

        return round(variance)

    @staticmethod
    def std(data):
        # input validation
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        # get variance
        variance = TinyStatistician.var(data)

        # get standard diviation
        std = variance**0.5

        # round to the second decimal place
        return round(std, 2)
