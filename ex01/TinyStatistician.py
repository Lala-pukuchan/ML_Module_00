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
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        arr = sorted(data)
        index = (len(arr) - 1) * percent / 100
        lower = int(index)
        upper = lower + 1
        weight = index - lower
        if upper >= len(arr):
            return arr[lower]
        else:
            return arr[lower] * (1 - weight) + arr[upper] * weight

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

        # return the exact value in an array
        return [sorted_data[q1_index], sorted_data[q3_index]]

    @staticmethod
    def var(data):
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        mean_val = sum(data) / len(data)

        variance = sum((x - mean_val) ** 2 for x in data) / (len(data) - 1)
        return variance

    @staticmethod
    def std(data):
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        return TinyStatistician.var(data) ** 0.5


output_file = "results/ex01/result_ex01.txt"

with open(output_file, "w") as file:
    print("section.1 -------------------------------", file=file)

    a = [1, 42, 300, 10, 59]
    ts = TinyStatistician()

    print("Mean:\n", ts.mean(a), file=file)
    print("expected Mean:\n 82.4", file=file)

    print("Median:\n", ts.median(a), file=file)
    print("expected Median:\n 42.0", file=file)

    print("Quartiles:\n", ts.quartile(a), file=file)
    print("expected Quartiles:\n [10.0, 59.0]", file=file)

    print("10th Percentile:\n", ts.percentile(a, 10), file=file)
    print("expected 10th Percentile:\n 4.6", file=file)

    print("15th Percentile:\n", ts.percentile(a, 15), file=file)
    print("expected 15th Percentile:\n 6.4", file=file)

    print("20th Percentile:\n", ts.percentile(a, 20), file=file)
    print("expected 20th Percentile:\n 8.2", file=file)

    print("Variance:\n", ts.var(a), file=file)
    print("expected Variance:\n 15349.3", file=file)

    print("Standard Deviation:\n", ts.std(a), file=file)
    print("expected Standard Deviation:\n 123.89229193133849", file=file)
