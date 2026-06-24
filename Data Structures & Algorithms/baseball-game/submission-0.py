class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == "C":
                score.pop()
            elif i == "D":
                score.append(score[-1]*2)
            elif i == "+":
                score.append(score[-2] + score[-1])
            else:
                score.append(int(i))
        return sum(score)