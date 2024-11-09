def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

phrase = "Inst-Pack"
binary_phrase = text_to_binary(phrase)
print("Texte original :", phrase)
print("Texte en binaire :", binary_phrase)

#############

def binary_to_text(binary_string):
    binary_values = binary_string.split()
    ascii_characters = [chr(int(b, 2)) for b in binary_values]
    return ''.join(ascii_characters)

binary_input = "01001110 01001000 01001101 00110010 01001001"
text_output = binary_to_text(binary_input)
print("\nBinaire original :", binary_input)
print("Texte converti :", text_output)
