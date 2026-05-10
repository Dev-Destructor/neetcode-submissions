class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            found = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > curr_temp:
                    result.append(j - i)
                    found = True
                    break
            if not found:
                result.append(0)
        return result