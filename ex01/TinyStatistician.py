import numpy as np


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
        if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
            return None

        sorted_data = sorted(data)
        n = len(sorted_data)

        q1_index = (n - 1) // 4
        q3_index = 3 * (n - 1) // 4

        if n % 2 == 0:
            q1 = (sorted_data[q1_index] + sorted_data[q1_index + 1]) / 2
            q3 = (sorted_data[q3_index] + sorted_data[q3_index + 1]) / 2
        else:
            q1 = sorted_data[q1_index]
            q3 = sorted_data[q3_index]

        return [float(q1), float(q3)]

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

    a = [1, 42, 300, 10, 59]
    ts = TinyStatistician()
    print("Mean:", ts.mean(a), file=file)
    print("Median:", ts.median(a), file=file)
    print("Quartiles:", ts.quartile(a), file=file)
    print("10th Percentile:", ts.percentile(a, 10), file=file)
    print("15th Percentile:", ts.percentile(a, 15), file=file)
    print("20th Percentile:", ts.percentile(a, 20), file=file)
    print("Variance:", ts.var(a), file=file)
    print("Standard Deviation:", ts.std(a), file=file)
