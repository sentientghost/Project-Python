class solution:
    def quickSort(self, arr, low, high):
        if (low < high):
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = (low - 1)

        for j in range(low, high):
            if (arr[j] < pivot):
                i += 1
                self.swap(arr, i, j)

        self.swap(arr, i + 1, high)
        return (i + 1)

    def swap(self, arr, x_index, y_index):
        temp = arr[x_index]
        arr[x_index] = arr[y_index]
        arr[y_index] = temp
