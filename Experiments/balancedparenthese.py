class Solution:
    def Solution(self):
        pass

    def scoreOfParentheses(self, parstring):
        completepair = 0
        openpar = 0
        closepar = 0
        for i in range(0, len(parstring)):
            if parstring[i] == '(':
                openpar += 1
            elif parstring[i] == ')':
                if openpar != 0:
                    openpar -= 1
                    completepair += 1

        return completepair


if __name__ == '__main__':
    solve = Solution()
    pairs = solve.scoreOfParentheses('((()))))')
    print(f"Complete pairs of parentheses {pairs}")

