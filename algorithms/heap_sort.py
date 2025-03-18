from algorithms.sorting_strategy import SortingStrategy

class HeapSort(SortingStrategy):
    def sort(self, data): 
        comparisons, swaps = self.heap_sort(data)
        print(f"HeapSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data
    
    def heapify(self, data, n, i, counters):
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        if left < n:
            counters["comparisons"] += 1
            if data[left] > data[largest]:
                largest = left

        if right < n:
            counters["comparisons"] += 1
            if data[right] > data[largest]:
                largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]  
            counters["swaps"] += 1
            self.heapify(data, n, largest, counters)  
            
    def heap_sort(self, data):
        n = len(data)
        counters = {"comparisons": 0, "swaps": 0}

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(data, n, i, counters)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]  
            counters["swaps"] += 1
            self.heapify(data, i, 0, counters)  

        return counters["comparisons"], counters["swaps"]
