class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        getDig = lambda strDig: ord(strDig) - ord('0')
        for mag1, dig1 in enumerate(num1[::-1]):
            for mag2, dig2 in enumerate(num2[::-1]):
                product += getDig(dig1)*10**mag1 * getDig(dig2)*10**mag2
        return str(product)