from algorithms.sorting_strategy import SortingStrategy

class CountingSort(SortingStrategy):
    
    def sort(self, data):
        if not data:
            return []

        comparisons = 0
        swaps = 0

        min_val = min(data)
        max_val = max(data)
        
        size = max_val - min_val + 1
        count = [0] * size
        output = [0] * len(data)

        for num in data:
            count[num - min_val] += 1
            comparisons += 1

        for i in range(1, size):
            count[i] += count[i - 1]
            comparisons += 1

        for num in reversed(data): 
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
            swaps += 1

        print(f"CountingSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return output
