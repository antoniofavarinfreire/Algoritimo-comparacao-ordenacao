from algorithms.sorting_strategy import SortingStrategy

class QuickSort(SortingStrategy):

    def sort(self, data):
        self.quick_sort(data, 0, len(data) - 1)
        return data

    def quick_sort(self, data, low, high):
        if low < high:
            pi = self.partition(data, low, high)
            self.quick_sort(data, low, pi - 1)
            self.quick_sort(data, pi + 1, high)

    def partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1
