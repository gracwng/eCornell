class Solution:
    def countTeams (self, teamSize_1, teamSize_2, p):
        maxCount = p // teamSize_1
        team1Count = maxCount
        # now replace teams with ppl from team2
        remainder = (p % teamSize_1 != 0)
        print(remainder)
        currentCount = maxCount * teamSize_1
        
        while (currentCount >= 0):
            team1Count -= 1
            currentCount -= teamSize_1
            newCount = (p - currentCount) // teamSize_2
            if ((p - currentCount) % teamSize_2 == 0):
                remainder = False
            maxCount = max(maxCount, team1Count + newCount)
        
        if not remainder:
            return maxCount
        else: return -1

def main():
    solution = Solution()

    print(solution.countTeams(2, 4, 7))

main()
