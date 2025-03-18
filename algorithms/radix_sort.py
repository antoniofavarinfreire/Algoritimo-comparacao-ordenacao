from algorithms.sorting_strategy import SortingStrategy

class RadixSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = self.radix_sort(data)
        print(f"RadixSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data

    def counting_sort_radix(self, data, exp, counters):
        n = len(data)
        output = [0] * n
        count = [0] * 10  

        for num in data:
            index = (num // exp) % 10
            count[index] += 1
            counters["comparisons"] += 1  

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):  
            num = data[i]
            index = (num // exp) % 10
            output[count[index] - 1] = num
            count[index] -= 1
            counters["swaps"] += 1  

        for i in range(n):
            data[i] = output[i]
            counters["swaps"] += 1  

    def radix_sort(self, data):
        if not data:
            return 0, 0

        counters = {"comparisons": 0, "swaps": 0}

        max_val = max(data)
        exp = 1
        while max_val // exp > 0:
            self.counting_sort_radix(data, exp, counters)
            exp *= 10

        return counters["comparisons"], counters["swaps"]
