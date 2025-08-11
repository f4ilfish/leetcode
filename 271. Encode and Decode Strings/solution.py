from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#"
        encoded_strings: List[str] = []
        for string in strs:
            encoded_chars = [str(ord(char)) for char in string]
            encoded_string = "*".join(encoded_chars)
            encoded_strings.append(encoded_string)
        return "#".join(encoded_strings)
    
    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == "#":
            return []
        decoded_strings: List[str] = []
        strings = s.split("#")
        for string in strings:
            decoded_chars: List[str] = []
            chars = string.split("*")
            for char in chars:
                if char == "":
                    decoded_chars.append("")
                else:
                    decoded_chars.append(chr(int(char)))
            decoded_strings.append("".join(decoded_chars))
        return decoded_strings


if __name__ == "__main__":
    input = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
    solution = Solution()
    encoded_input = solution.encode(input)
    decoded_input = solution.decode(encoded_input)
    print(f"Input: {input}")
    print(f"Encoded: {encoded_input}")
    print(f"Decoded: {decoded_input}")
