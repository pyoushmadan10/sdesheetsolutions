class Solution:
    def isPowerOfFour(self, n):
        # If 'n' is 1, it is a power of four
        if n == 1:
            return True

        # If 'n' is non-positive, it cannot be a power of four
        if n <= 0:
            return False

        # Calculate the square root of 'n'
        sqrtN = math.sqrt(n)

        # Take the logarithm base 2 of the square root
        log2SqrtN = math.log2(sqrtN)

        # Check if the result of the logarithmic operation is an integer
        return log2SqrtN == int(log2SqrtN)