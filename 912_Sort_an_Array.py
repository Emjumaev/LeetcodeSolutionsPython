class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        leftPortion = self.mergeSort(arr[0:mid])
        rightPortion = self.mergeSort(arr[mid:])

        # merge two sorted portion
        i = 0
        j = 0

        sortedArr = []
        while(i < len(leftPortion) and j < len(rightPortion)):
            if leftPortion[i] < rightPortion[j]:
                sortedArr.append(leftPortion[i])
                i += 1
            else:
                sortedArr.append(rightPortion[j])
                j += 1

        # appending leftover elements
        sortedArr.extend(leftPortion[i:])
        sortedArr.extend(rightPortion[j:])

        return sortedArr
