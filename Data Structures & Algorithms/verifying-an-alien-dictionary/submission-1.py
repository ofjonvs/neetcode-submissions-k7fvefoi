class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd = {c: i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda x: [orderInd[c] for c in x])