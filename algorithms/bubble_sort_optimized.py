from algorithms.sorting_strategy import SortingStrategy

class BubbleSortOptimized(SortingStrategy):

    def sort(self, data):
        n = len(data)
        comparisons = 0  
        swaps = 0        

        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                comparisons += 1  
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swaps += 1 
                    swapped = True
            
            if not swapped: 
                break  

        print(f"BubbleSortOptimized: Comparisons = {comparisons}, Swaps = {swaps}")
        return data, comparisons, swaps