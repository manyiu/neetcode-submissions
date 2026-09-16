class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a: List[int], b: List[int]) -> List[int]:
            c = []

            while a and b:
                if a[0] < b[0]:
                    c.append(a.pop(0))
                else:
                    c.append(b.pop(0))

            c = c + a if a else c + b
            return c

        def mergeSort(a: List[int]) -> List[int]:
            if len(a) <= 1:
                return a

            mid = len(a) // 2

            left = a[:mid]
            right = a[mid:]

            return merge(mergeSort(left), mergeSort(right))

        return mergeSort(nums)