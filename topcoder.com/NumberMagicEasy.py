class NumberMagicEasy:
    def theNumber(self, answer):

        s = [
            {1, 2, 3, 4, 5, 6, 7, 8},
            {1, 2, 3, 4, 9, 10, 11, 12},
            {1, 2, 5, 6, 9, 10, 13, 14},
            {1, 3, 5, 7, 9, 11, 13, 15}
        ]

        result = set(range(1, 17))

        for i, a in enumerate(answer):
            if a == 'Y':
                result = result & s[i]
            else:
                result = result - s[i]

        return result.pop()

c = NumberMagicEasy()
answer = "YNYY"
print(c.theNumber(answer))