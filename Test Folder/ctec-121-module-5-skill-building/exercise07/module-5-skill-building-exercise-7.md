# Module 5 - Skill Building Exercise No. 7

## Caesar Cipher

A Caesar cipher is a simple substitution cipher based on the idea of shifting each letter of the plaintext message a fixed number (called the key) of positions in the alphabet. For example, if the key value is 2, the word Sourpuss” would be encoded as “Uqwtrwuu.” The original message can be recovered by “reencoding” it using the negative of the key. Write a program that can encode and decode Caesar ciphers. The input to the program will be a string of plaintext and the value of the key. The output will be an encoded message where each character in the original message is replaced by shifting it key characters in the Unicode character set. For example, if ch is a character in the string and key is the amount to shift, then the character that replaces ch can be calculated as: chr(ord(ch) + key).

For example if the key is 2 and the input is "Bill Baker", the output will be: 'Dknn"Dcmgt'. If I run the program again with a key of -2 and use the output from the first run as the input string, I should get "Bill Baker" again.