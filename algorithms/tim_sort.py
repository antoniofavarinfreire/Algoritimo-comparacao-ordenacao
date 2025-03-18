from algorithms.sorting_strategy import SortingStrategy
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort

class TimSort(SortingStrategy):
    def sort(self, data):
        self.tim_sort(self, data)
        return data
    
    def tim_sort(self, data):
        n = len(data)
        for i in range(0, 32):
            InsertionSort(data, i, min(i + 32 - 1, n -1 ))
    
        size = 32
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
                if mid < right: 
                    MergeSort.merge(data, left, mid, right)
            size *= 2
        return data