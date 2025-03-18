from algorithms.sorting_strategy import SortingStrategy

class RadixSort(SortingStrategy):
    def sort(self, data):
        self.counting_sort_radix(self, data)
        return data
    
    def counting_sort_radix(data, exp):
        n = len(data)
        output = [0] * n
        count = [0] * 10  

        
        for num in data:
            index = (num // exp) % 10
            count[index] += 1

        
        for i in range(1, 10):
            count[i] += count[i - 1]

        
        for i in range(n - 1, -1, -1):  
            num = data[i]
            index = (num // exp) % 10
            output[count[index] - 1] = num
            count[index] -= 1

        
        for i in range(n):
            data[i] = output[i]

    def radix_sort(self, data):
        if not data:
            return []

        
        max_val = max(data)
        
        
        exp = 1
        while max_val // exp > 0:
            self.counting_sort_radix(data, exp)
            exp *= 10