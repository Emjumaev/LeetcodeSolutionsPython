from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashMap = {}

        for domain in cpdomains:
            splitDomain = domain.split(" ")
            count = int(splitDomain[0])
            domainStr = splitDomain[1]

            subdomains = domainStr.split(".")

            curStr = ""
            for i in range(len(subdomains) - 1, -1, -1):
                curStr = subdomains[i] + curStr
                if curStr in hashMap:
                    hashMap[curStr] += count
                else:
                    hashMap[curStr] = count
                curStr = "." + curStr
        
        ans = []
        for key, value in hashMap.items():
            ans.append(f"{value} {key}")

        return ans
