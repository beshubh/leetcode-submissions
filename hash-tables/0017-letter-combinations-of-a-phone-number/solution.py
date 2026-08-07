

MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        current = []
        output = []
        def go(i: int):
            if i == n - 1:
                return list(MAPPING[digits[i]])
            result = []
            for j in MAPPING[digits[i]]:
                for k in go(i + 1):
                    result.append(j + k)
            return result
        return go(0)
        
