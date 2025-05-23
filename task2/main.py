from longest_common_word import LongestCommonWord

# Тести
trie = LongestCommonWord()
strings = ["flower", "flow", "flight"]
assert trie.find_longest_common_word(strings) == "fl"

trie = LongestCommonWord()
strings = ["interspecies", "interstellar", "interstate"]
assert trie.find_longest_common_word(strings) == "inters"

trie = LongestCommonWord()
strings = ["dog", "racecar", "car"]
assert trie.find_longest_common_word(strings) == ""

trie = LongestCommonWord()
strings = []
assert trie.find_longest_common_word(strings) == ""

print("Усі тести пройдено успішно.")
