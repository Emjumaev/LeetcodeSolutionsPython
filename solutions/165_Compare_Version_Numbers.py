class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        versionArr1 = version1.split(".")
        versionArr2 = version2.split(".")

        i, j = 0, 0
        while(i < len(versionArr1) or j < len(versionArr2)):
            if i >= len(versionArr1):
                version1 = 0
            else:
                version1 = int(versionArr1[i])
            
            if j >= len(versionArr2):
                version2 = 0
            else:
                version2 = int(versionArr2[j])

            if version1 < version2:
                return -1
            elif version1 > version2:
                return 1
            
            i += 1
            j += 1

        return 0
