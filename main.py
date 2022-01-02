# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:09:47 2022

@author: Julien
"""

from functions import HuffmanCompression, HuffmanDecompression
from functions import ASCIIvsHuffman as AvsH


#Run on some example

from examples import otis

example = otis

# Check our code work

msg_compressed, nb_bits, tree = HuffmanCompression(example)
msg_decompressed, nb_bits = HuffmanDecompression(msg_compressed, tree)

print('---------------------------------------------------------------\n' +
      'Original message : \n' + example +
      '\n\nCompressed message, binary format : ' + msg_compressed + 
      '\n\nDecompressed message : \n' + msg_decompressed)

print('\n\nWe check both message are equal : ' + str(example == msg_decompressed))

# Compare the standard ASCII format to this compressed one

bits_ascii, bits_huff = AvsH(example)
print('Bits in ASCII format : ' + str(bits_ascii) + 
      '\nBits in Huffman Compressed format : ' + str(bits_huff) +
      '\nCompression rate : ' + str(100*(bits_ascii-bits_huff)/bits_ascii))

#With a bigger example

from examples import lipsum

example = lipsum

# Compare the standard ASCII format to this compressed one

bits_ascii, bits_huff = AvsH(example)
print('\n\n----------------------------------------'+
      '----------------------------------------'+
      '\nBigger example, 50 paragraphs of lorem ipsum : \n'
      'Bits in ASCII format : ' + str(bits_ascii) + 
      '\nBits in Huffman Compressed format : ' + str(bits_huff)+
      '\nCompression rate : ' + str(100*(bits_ascii-bits_huff)/bits_ascii))




