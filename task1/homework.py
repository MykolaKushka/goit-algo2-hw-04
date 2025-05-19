from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Суфікс повинен бути рядком")

        count = 0

        def dfs(node, current_word):
            nonlocal count
            if node.value is not None:
                if current_word.endswith(pattern):
                    count += 1
            for char, child in node.children.items():
                dfs(child, current_word + char)

        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Префікс повинен бути рядком")

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    assert trie.count_words_with_suffix("e") == 1
    assert trie.count_words_with_suffix("ion") == 1
    assert trie.count_words_with_suffix("a") == 1
    assert trie.count_words_with_suffix("at") == 1

    assert trie.has_prefix("app") == True
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True
    assert trie.has_prefix("ca") == True

    print("Усі тести пройдено успішно.")
