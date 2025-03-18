from algorithms.sorting_strategy import SortingStrategy

class MergeSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = self.merge_sort(data, 0, len(data) - 1, {"comparisons": 0, "swaps": 0})
        print(f"MergeSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data
    
    def merge(self, data, l, m, r, counters):
        n1 = m - l + 1
        n2 = r - m
        
        L = [0] * n1 
        R = [0] * n2
        
        for i in range(n1):
            L[i] = data[l + i]
        for j in range(n2):
            R[j] = data[m + 1 + j]

        i, j, k = 0, 0, l
        
        while i < n1 and j < n2:
            counters["comparisons"] += 1
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else: 
                data[k] = R[j]
                j += 1
            k += 1
            counters["swaps"] += 1

        while i < n1: 
            data[k] = L[i]
            i += 1
            k += 1
            counters["swaps"] += 1

        while j < n2: 
            data[k] = R[j]
            j += 1
            k += 1
            counters["swaps"] += 1

    def merge_sort(self, data, l, r, counters):
        if l < r: 
            m = l + (r - l) // 2
            
            self.merge_sort(data, l, m, counters)
            self.merge_sort(data, m + 1, r, counters)
            self.merge(data, l, m, r, counters)
        
        return counters["comparisons"], counters["swaps"]
