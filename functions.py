# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:51:31 2022

@author: Julien
"""

from classes import Node
import time

def freq(msg):
    table = {}
    
    for s in msg:
        if s not in table.keys():
            table[s] = 1
        else:
            table[s] = table[s] + 1
    return table

def tree(msg):
    table = freq(msg)
    keys = list(table.keys())
    values = list(table.values())
    
    nodes = []
    
    for k in keys:
        nodes.append(Node(table.get(k), k))
    
    nodes = sorted(nodes, key=lambda x: x.prob)
    
    while len(nodes) > 1:
        
        right = nodes[0]
        left = nodes[1]
       
        left.code = 0
        right.code = 1
       
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
       
        nodes.remove(left)
        nodes.remove(right)
        
        nodes.insert(0, newNode)
        
        nodes = sorted(nodes, key=lambda x: x.prob)
         
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
        
# def treeToTable(t, c=None, l=[]):
#     if len(t.symbol) == 1:
#         return([str(c) + str(t.code), t.symbol])
#     else:
#         l.append(treeToTable(t.left, t.code,l))
#         l.append(treeToTable(t.right, t.code,l))
        
#         return(l)
        
def HuffmanCompression(msg):
    t0 = time.time()
    t = tree(msg)
    print('Time tree : ' + str(time.time()-t0))
    
    msg_compressed = ''
    
    t0 = time.time()
    for s in msg:
        msg_compressed += symbolToCode(t, s)
        
    print('Time compression : ' + str(time.time()-t0))
    
    return(msg_compressed, len(msg_compressed), t)

def HuffmanDecompression(msg, t):
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
    print('\n\n----------------------------------------'+
          '----------------------------------------')
    bits_ascii= 8*len(msg)
    
    t0 = time.time()
    t = tree(msg)
    t_tree = time.time()-t0
    
    
    msg_compressed = ''
    
    t0 = time.time()
    
    for s in msg:
        msg_compressed += symbolToCode(t, s)
        
    t_compr = time.time()-t0
    
    bits_huff = len(msg_compressed)
    
    print('Time tree : ' + str(t_tree))
    print('Time compression : ' + str(t_compr))
    print('Time computation ratio : '+ str(100*t_tree/t_compr))
    print('\nBits in ASCII format : ' + str(bits_ascii) + 
          '\nBits in Huffman Compressed format : ' + str(bits_huff)+
          '\nCompression rate : ' + str(100*(bits_ascii-bits_huff)/bits_ascii))
    