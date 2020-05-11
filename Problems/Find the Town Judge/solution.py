from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        villagers = [0] * N

        for t in trust:
            v, j = t
            villagers[v - 1] -= 1 # v-1 because of 0-index placeholder array and villagers are indexed starting from 1.
            villagers[j - 1] += 1  # j-1 because of 0-index placeholder array and villagers are indexed starting from 1.

        for i in range(len(villagers)):
            if villagers[i] == N - 1:
                return i + 1 # i+1 since we have to return the villager index, not our placeholder index

        return -1