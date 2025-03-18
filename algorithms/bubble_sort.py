from algorithms.sorting_strategy import SortingStrategy

class BubbleSort(SortingStrategy):

    def sort(self, data):
        n = len(data)
        comparisons = 0  
        swaps = 0        

        for i in range(n):
            for j in range(n - i - 1):
                comparisons += 1  
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swaps += 1 

        print(f"BubbleSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data
