from algorithms.sorting_strategy import SortingStrategy

class InsertionSort(SortingStrategy):
    def sort(data, size):
        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, data): 
                if data[j] < data[min_index]:
                    min_index = j 
            (data[ind], data[min_index]) = (data[min_index], data[ind])
        return data