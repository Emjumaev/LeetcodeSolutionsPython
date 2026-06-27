class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        j = 0
        hashMap = {}

        for student in students:
            if student in hashMap:
                hashMap[student] += 1
            else:
                hashMap[student] = 1

        while(i < len(sandwiches)):
            if sandwiches[i] == students[j]:
                hashMap[students[j]] -= 1
                i += 1
                j += 1
            else:
                if sandwiches[i] not in hashMap or hashMap[sandwiches[i]] == 0:
                    return len(sandwiches) - i
                students.append(students[j])
                j += 1

        return 0
