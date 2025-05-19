class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None 


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = value

    def get(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value
