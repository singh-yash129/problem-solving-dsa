class Solution:
    def encode(self, strs: list[str]) -> str:
        # If the list is empty, return a unique marker that couldn't 
        # possibly be created by your ord() logic (e.g., "EMPTY")
        if not strs:
            return "EMPTY"
            
        encoded_str = ""
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                encoded_str += str(ord(strs[i][j]))
                if j < len(strs[i]) - 1:
                    encoded_str += '-'
            if i < len(strs) - 1:
                encoded_str += "#$"
                
        return encoded_str[::-1]

    def decode(self, s: str) -> list[str]:
        # 1. Handle the true empty list case
        if s == "EMPTY":
            return []
            
        # 2. Handle the case where the input was an empty string s="" 
        # (though your encode now prevents this, it's good safety)
        if not s:
            return [""]
            
        s = s[::-1]
        res = []
        # split("#$") on a string representing [""] will return ['']
        words = s.split("#$")
        for word in words:
            # If word is empty string, it means the original element was ""
            if word == "":
                res.append("")
                continue
                
            current_str = ""
            ascii_values = word.split("-")
            for val in ascii_values:
                if val:
                    current_str += chr(int(val))
            res.append(current_str)
        return res