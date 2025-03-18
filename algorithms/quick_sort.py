from algorithms.sorting_strategy import SortingStrategy

class QuickSort(SortingStrategy):

    def sort(self, data):
        comparisons, swaps = self.quick_sort(data, 0, len(data) - 1, {"comparisons": 0, "swaps": 0})
        print(f"QuickSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data

    def quick_sort(self, data, low, high, counters):
        if low < high:
            pi = self.partition(data, low, high, counters)
            self.quick_sort(data, low, pi - 1, counters)
            self.quick_sort(data, pi + 1, high, counters)

        return counters["comparisons"], counters["swaps"]

    def partition(self, data, low, high, counters):
        pivot = data[high]
        i = low - 1

        for j in range(low, high):
            counters["comparisons"] += 1  
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                counters["swaps"] += 1  

        data[i + 1], data[high] = data[high], data[i + 1]
        counters["swaps"] += 1  
        return i + 1
