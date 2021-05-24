class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result=[''] * numRows
        row_index=2
        direction=1
        result[0]=s[0]
        if len(s)<=numRows or numRows==1:
            return s
        for char in s[1:]:
            result[row_index-1] += char
            if row_index==numRows or row_index==1:
                direction *= -1
            row_index += direction
        return ''.join(result)