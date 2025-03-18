from algorithms.sorting_strategy import SortingStrategy
class InsertionSort(SortingStrategy): 

    def sort(data):
        n = len(data) 
        if n <= 1: 
            return 
        for i in range (1, n): 
            key = data[i]
            j = i -1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
                data[j + 1] = key
        return data
