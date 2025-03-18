from algorithms.sorting_strategy import SortingStrategy

class MergeSort(SortingStrategy):
    def sort(self, data):
        self.mergeSort(self, data, 0, len(data) - 1)
        return data
    
    def merge(data, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        
        L = [0] * (n1) 
        R = [0] * (n2)
        
        for i in range(0, n1):
            L[i] = data[l + i]
        for j in range(0, n2):
            R[j] = data[m + 1 + j]
        i = 0
        j = 0
        k = l
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else: 
                data[k] = R[k]
                j += 1
            k += 1
        while i < n1: 
            data[k] = L[i]
            i += 1
            k += 1
            
        while j < n2: 
            data[k] = R[j]
            j += 1
            k += 1
        return data
    
    def merge_sort(self, data, l, r):
        if 1 < l: 
            m = 1 + (r - 1) // 2
            
            self.merge_sort(data, l, m)
            self.merge_sort(data, m+1, r)
            self.merge(data, l, m, r)
            
