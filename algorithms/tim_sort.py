from algorithms.sorting_strategy import SortingStrategy
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort

class TimSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = self.tim_sort(data)
        print(f"TimSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data, comparisons, swaps

    def tim_sort(self, data):
        n = len(data)
        comparisons = 0
        swaps = 0

        for i in range(0, n, 32):
            comp, swp = self.insertion_sort(data, i, min(i + 32 - 1, n - 1))
            comparisons += comp
            swaps += swp

        size = 32
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
                if mid < right: 
                    comp, swp = self.merge_sort(data, left, mid, right)
                    comparisons += comp
                    swaps += swp
            size *= 2

        return comparisons, swaps

    def insertion_sort(self, data, left, right):
        comparisons = 0
        swaps = 0
        for i in range(left + 1, right + 1):
            key = data[i]
            j = i - 1
            while j >= left:
                comparisons += 1
                if key < data[j]:
                    data[j + 1] = data[j]
                    swaps += 1
                    j -= 1
                else:
                    break
            data[j + 1] = key
            swaps += 1
        return comparisons, swaps

    def merge_sort(self, data, left, mid, right):
        comparisons = 0
        swaps = 0

        n1 = mid - left + 1
        n2 = right - mid

        L = data[left: left + n1]
        R = data[mid + 1: mid + 1 + n2]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            comparisons += 1
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            swaps += 1
            k += 1

        while i < n1:
            data[k] = L[i]
            i += 1
            k += 1
            swaps += 1

        while j < n2:
            data[k] = R[j]
            j += 1
            k += 1
            swaps += 1

        return comparisons, swaps
