class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        res = []

        for str in strs:
            sortedStr = "".join(sorted(str))

            if sortedStr in hashMap:
                hashMap[sortedStr].append(str)
            else:
                hashMap[sortedStr] = [str]

        for (index, value) in hashMap.items():
            res.append(value)

        return res
