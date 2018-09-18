class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i, n = 0, len(s) - 1

        while i < n:                                    # O(n) time
            if s[i] == '+':
                while i < n and s[i+1] == '+':          # O(c) time
                    res.append(s[:i] + '--' + s[i+2:])  # O(n) time and space
                    i += 1
            i += 1
        return res






    """
        Time Complexity = O(c * n + n) = O(n*(c+1))
        Space Complexity = O(n)

        You are playing the following Flip Game with your friend: Given a string that contains only these two
        characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game
        ends when a person can no longer make a move and therefore the other person will be the winner.
        Write a function to compute all possible states of the string after one valid move.

        Example:
        Input: s = "++++"
        Output:
        [
          "--++",
          "+--+",
          "++--"
        ]

        Note: The print should be wrong.
    """
