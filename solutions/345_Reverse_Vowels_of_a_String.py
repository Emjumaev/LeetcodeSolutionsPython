class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = set("aeiouAEIOU")
        arr = list(s)

        while(left < right):
            if arr[left] not in vowels:
                left += 1
                continue

            if arr[right] not in vowels:
                right -= 1
                continue

            # swap
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return "".join(arr)
