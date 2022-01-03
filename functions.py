# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:51:31 2022

@author: Julien
"""

from classes import Node

def freq(msg):
    table = {}
    
    for s in msg:
        table[s] = msg.count(s)

    return table

def tree(msg):
    table = freq(msg)
    keys = list(table.keys())
    values = list(table.values())
    
    nodes = []
    
    for k in keys:
        nodes.append(Node(table.get(k), k))
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        
        right = nodes[0]
        left = nodes[1]
       
        left.code = 0
        right.code = 1
       
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
       
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
        
    return(nodes[0])

def symbolToCode(t, s):
    if len(t.symbol) == 1:
        return(str(t.code))
    else:
        if s in t.right.symbol:
            return(str(t.right.code) + symbolToCode(t.right, s))
        else:
            return(str(t.left.code) + symbolToCode(t.left, s))
   
def codeToSymbol(t, c):
    if len(c) == 1:
        return(t.symbol)
    else:
        if int(c[0]) == t.left.code:
            return(codeToSymbol(t.left, c[1:]))
        else:
            return(codeToSymbol(t.right, c[1:]))
        
def HuffmanCompression(msg):
    t = tree(msg)
    
    msg_compressed = ''
    
    for s in msg:
        msg_compressed += symbolToCode(t, s)
    
    return(msg_compressed, len(msg_compressed), t)

def HuffmanDecompression(msg, t):
    #t = tree(msg)
    n = len(msg)
    
    msg_decompressed = ''
    
    a = 0
    b = 1
    
    while a < n:
        s = codeToSymbol(t, msg[a:b])
        if len(s) != 1:
            b+=1
        else:
            msg_decompressed += s
            a = b
            b+=1
        
    return(msg_decompressed, len(msg_decompressed))

def ASCIIvsHuffman(msg):
    ascii_nb_bits = 8*len(msg)
    
    huffman_bin_msg, huffman_nb_bits, t = HuffmanCompression(msg)
    
    return(ascii_nb_bits, huffman_nb_bits)