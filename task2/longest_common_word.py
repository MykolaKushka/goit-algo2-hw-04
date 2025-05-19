from trie import Trie, TrieNode


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Потрібен список рядків")

        if not strings:
            return ""

        # Додаємо всі рядки в дерево
        for i, word in enumerate(strings):
            self.put(word, i)

        # Пошук найдовшого префікса
        prefix = []
        node = self.root

        while True:
            if len(node.children) != 1 or node.value is not None:
                break
            char, next_node = next(iter(node.children.items()))
            prefix.append(char)
            node = next_node

        return "".join(prefix)
