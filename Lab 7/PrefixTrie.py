from __future__ import annotations

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        # self.node_count = 0

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                # self.node_count += 1
            node = node.children[char]
        node.is_end_of_word = True

    def get_adjacency_list(self):
        adjacency_list = []
        node_map = {self.root: 0}
        # Ініціалізація лічильника ID для наступних вузлів
        self.next_node_id = 1

        def traverse(node: TrieNode, current_id):
            for char, child_node in node.children.items():
                if child_node not in node_map:
                    node_map[child_node] = self.next_node_id
                    adjacency_list.append((current_id, self.next_node_id, char))
                    # Інкрементуємо після додавання
                    self.next_node_id += 1
                    traverse(child_node, node_map[child_node])
                else:
                    adjacency_list.append((current_id, node_map[child_node], char))

        traverse(self.root, 0)
        return adjacency_list
