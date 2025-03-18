from algorithms.sorting_strategy import SortingStrategy

class ShellSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = self.shell_sort(data)
        print(f"ShellSort: Comparisons = {comparisons}, Swaps = {swaps}")
        return data, comparisons, swaps

    def shell_sort(self, data):
        n = len(data)
        gap = n // 2  
        comparisons = 0
        swaps = 0

        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i

                while j >= gap:
                    comparisons += 1
                    if data[j - gap] > temp:
                        data[j] = data[j - gap]
                        swaps += 1
                        j -= gap
                    else:
                        break

                data[j] = temp
                swaps += 1  

            gap //= 2  

        return comparisons, swaps
