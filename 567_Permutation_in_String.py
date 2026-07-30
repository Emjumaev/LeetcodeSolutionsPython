class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        window = Counter()

        i = 0
        for j in range(len(s2)):
            window[s2[j]] += 1

            if j - i + 1 > len(s1):
                window[s2[i]] -= 1
                if window[s2[i]] == 0:
                    window.pop(s2[i])
                i += 1

            # compare two dictionaries
            if counter == window:
                return True

        return False

"""
Time: O(n * m)
Space: O(1) because we only have 26 characters in english alphabet
"""
