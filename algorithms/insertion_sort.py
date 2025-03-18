from algorithms.sorting_strategy import SortingStrategy

class InsertionSort(SortingStrategy): 

    def sort(self, data):
        n = len(data) 
        if n <= 1: 
            return data

        comparisons = 0
        swaps = 0

        for i in range(1, n): 
            key = data[i]
            j = i - 1

            while j >= 0:
                comparisons += 1
                if key < data[j]:
                    data[j + 1] = data[j]
                    swaps += 1
                    j -= 1
                else:
                    break

            data[j + 1] = key
            swaps += 1  

        print(f"InsertionSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data
