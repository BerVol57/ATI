from __future__ import annotations

class Node:
    symb = None
    count: int = None
    
    left_child: Node = None
    right_child: Node = None
    
    def __init__(self, symb, count):
        self.symb = symb
        self.count = count
    

def build_huffman_tree(symbols, counts):
    nodes = [Node(symb, count) for symb, count in zip(symbols, counts)]
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key = lambda x: x.count)[::-1]
        
        left_child = nodes.pop()
        right_child = nodes.pop()
        
        merged_node = Node(None, left_child.count + right_child.count)
        
        merged_node.left_child = left_child
        merged_node.right_child = right_child
        
        nodes.append(merged_node)
    
    return nodes[0]

def generate_huffman_codes(node):
    if node is None:
        return {}

    huffman_codes = {}
    stack = [(node, "")]

    while stack:
        current_node, code = stack.pop()

        if current_node.symb is not None:
            huffman_codes[current_node.symb] = code

        if current_node.right_child is not None:
            stack.append((current_node.right_child, code + "1"))

        if current_node.left_child is not None:
            stack.append((current_node.left_child, code + "0"))

    return huffman_codes
