"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]

"""

"""
Algorithm:
Encoding Process
- Initialize an empty string (or a string builder/stream for efficiency) to hold the encoded string.
- Iterate over each string in the input list. For each string:
- Replace each occurrence of the slash character / with two slash characters //. This is our way of "escaping" the slash character.
- Add the escaped string and our chosen delimiter /: to the encoded string.
- Return the encoded string after all strings in the input list have been processed.

Decoding Process
- Initialize an empty list to hold the decoded strings.
- Initialize an empty string to build the current string being decoded.
- Iterate over the characters in the encoded string. For each character:
- If the character and the next one form the delimiter /:, add the current string to the list of decoded strings and clear the current string for the next one. Skip the next character in the string.
- If the character and the next one form the escaped slash //, add a single slash to the current string. Skip the next character in the string.
- Otherwise, add the character to the current string.
- Return the list of decoded strings after all characters in the encoded string have been processed.
"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        for s in strs:
            encoded_str += s.replace('/', '//') + '/:'

        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs = []
        curr_str = ''
        i = 0
        while i < len(s):
            if s[i:i+2] == '/:':
                decoded_strs.append(curr_str)
                curr_str = ''
                i += 2
            elif s[i:i+2] == '//':
                curr_str += '/'
                i += 2
            else:
                curr_str += s[i]
                i += 1
        return decoded_strs

def main():
    pass

if __name__ == '__main__':
    main()
