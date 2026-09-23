class Solution:

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ":" + s
        return encoded

    def decode(self, s):
        res = []
        r = 0
        while r < len(s):
            length_str = ""
            while s[r] != ":":
                length_str += s[r]
                r += 1
            length = int(length_str)
            r += 1 
            word = s[r:r + length]
            res.append(word)
            r += length
        return res