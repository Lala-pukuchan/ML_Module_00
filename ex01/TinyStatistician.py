import numpy as np

class TinyStatistician:
    def __init__(self, input_data):
        if isinstance(input_data, list, np.ndarray):
            self.data = input_data
        else:
            raise TypeError("Wrong input data type")
    
    def mean(self):
        # return none (indicating that the function does not return anything.)
        if len(self.data) == 0:
            return None

        total_sum = 0
        for value in self.data:
            total_sum += value
        return total_sum / len(self.data)

    def median(self):
        if len(self.data) == 0:
            return None

        sorted_data = sorted(self.data)
        if len(sorted_data) % 2 == 1:
            return sorted_data[len(sorted_data) // 2]
        else:
            return (sorted_data[len(sorted_data) // 2] + sorted_data[len(sorted_data) // 2 - 1]) / 2
        
    def quartile(data):
        if len(data) == 0:
            return None

        sorted_data = sorted(data)

        def percentile(arr, percent):
            index = (len(arr) - 1) * percent
            lower = int(index)
            upper = lower + 1
            # 0 <= weight <= 1
            weight = index - lower
            if upper >= len(arr):
                return arr[lower]
            else:
                return arr[lower] * (1 - weight) + arr[upper] * weight

        q1 = percentile(sorted_data, 0.25)
        q3 = percentile(sorted_data, 0.75)

        return [q1, q3]

    
