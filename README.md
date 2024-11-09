# 01001110_01001000_01001101_00110010_01001001
def ttb(text):     br = ' '.join(format(ord(char), '08b') for char in text)     return br
