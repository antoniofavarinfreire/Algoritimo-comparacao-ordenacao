from algorithms.sorting_strategy import SortingStrategy

class HeapSort(SortingStrategy):
    def sort(self, data): 
        self.heap_sort(self, data)
        return data
    
    def heapify(self, data, n, i):
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        
        if left < n and data[left] > data[largest]:
            largest = left

        
        if right < n and data[right] > data[largest]:
            largest = right

        
        if largest != i:
            data[i], data[largest] = data[largest], data[i]  
            self.heapify(data, n, largest)  
            
    def heap_sort(self, data):
        n = len(data)

       
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(data, n, i)

       
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]  
        self.heapify(data, i, 0)  

