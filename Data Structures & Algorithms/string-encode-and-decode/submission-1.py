class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for w in strs:
            l = len(w)
            s = str(l) + "#" + w
            encoded_string = encoded_string + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while(i < len(s)):
            j = i
            while s[j] != "#":
                j = j + 1

            l = int(s[i:j])

            x = s[j + 1:j + 1 + l]
            decoded_string.append(x)
            i = j + 1 + l

        return decoded_string