from algorithms.sorting_strategy import SortingStrategy

class SelectionSort(SortingStrategy):
    def sort(self, data):
        size = len(data)
        comparisons = 0  # Count comparisons
        swaps = 0        # Count swaps

        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, size):
                comparisons += 1  # Counting comparisons
                if data[j] < data[min_index]:
                    min_index = j 

            if min_index != ind:
                data[ind], data[min_index] = data[min_index], data[ind]  # Swap elements
                swaps += 1  # Counting swaps

        print(f"SelectionSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data
