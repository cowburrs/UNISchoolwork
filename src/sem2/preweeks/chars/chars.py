class Solution:
    def romanToInt(self, s: str) -> int:
        x = self.romToListInt(s)
        y = self.realRomanToInt(x)
        return y

    def romToListInt(self, s: str):
        return [self.romLetterToInt(x) for x in s]

    def romLetterToInt(self, s: str):
        match s:
            case "I":
                return 1
            case "V":
                return 5
            case "X":
                return 10
            case "L":
                return 50
            case "C":
                return 100
            case "D":
                return 500
            case "M":
                return 1000
        return 0  # Code is structurally unreachable

    def findHighest(self, l: list[int]) -> int:
        start = 0
        for i in range(len(l)):
            if l[i] >= l[start]:
                start = i
        return start

    def realRomanToInt(self, l: list[int]) -> int:
        f = self.realRomanToInt
        totalnum = 0
        if len(l) == 0:
            return 0
        if all(map((lambda x: l[0] >= x), l)):
            totalnum += l[0]
            totalnum = totalnum + self.realRomanToInt(l[1:])
        else:
            x = self.findHighest(l)
            left = l[:x]
            pivot = l[x]
            right = []
            if len(l) != x + 1:
                right = l[x + 1 :]
            totalnum += pivot - f(left) + f(right)
        return totalnum
