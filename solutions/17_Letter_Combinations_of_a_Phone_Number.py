class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hashMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        combinations = []

        for digit in digits:
            letters = hashMap[digit]

            newCombinations = []
            for letter in letters:
                if len(combinations) == 0:
                    newCombinations.append(letter)
                else:
                    for combination in combinations:
                        newCombination = combination + letter
                        newCombinations.append(newCombination)

            combinations = newCombinations

        return combinations
