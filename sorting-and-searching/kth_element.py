class solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        arr = [0] * (m + n)
        self.merge(arr, arr1, arr2)
        return arr[k-1]

    def merge(self, arr, arr1, arr2):
        i = j = k = 0

        while (i < len(arr1) and j < len(arr2)):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1
