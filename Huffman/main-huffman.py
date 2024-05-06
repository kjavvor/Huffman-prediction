from HuffmanGenerator import HuffmanGenerator

text = ['A', 'B', 'A', 'C', 'D', 'D', 'C', 'C', 'C', 'C']

coder, decoder = HuffmanGenerator().generateBasedOnFragment(text)

code = coder.code(text)
print(code)

decodedText = decoder.decode(code)
print(decodedText)

print(coder.code(['C']))
