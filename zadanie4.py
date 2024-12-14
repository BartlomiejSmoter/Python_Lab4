from collections import deque

class AhoCorasick:
    def __init__(self):
        self.trie = [{}]
        self.output = {}
        self.fail = {}

    def add_pattern(self, pattern):
        node_id = 0
        for char in pattern:
            if char not in self.trie[node_id]:
                self.trie.append({})
                self.trie[node_id][char] = len(self.trie) - 1
            node_id = self.trie[node_id][char]
        self.output[node_id] = self.output.get(node_id, []) + [pattern]

    def build(self):
        queue = deque()
        self.fail[0] = 0

        for char, child_id in self.trie[0].items():
            self.fail[child_id] = 0
            queue.append(child_id)

        while queue:
            current_node = queue.popleft()

            for char, next_node in self.trie[current_node].items():
                queue.append(next_node)

                fail_node = self.fail[current_node]
                while fail_node != 0 and char not in self.trie[fail_node]:
                    fail_node = self.fail[fail_node]
                self.fail[next_node] = self.trie[fail_node].get(char, 0)

                self.output[next_node] = self.output.get(next_node, []) + self.output.get(self.fail[next_node], [])

    def search(self, text):
        node_id = 0
        results = []

        for i, char in enumerate(text):
            while node_id != 0 and char not in self.trie[node_id]:
                node_id = self.fail[node_id]
            node_id = self.trie[node_id].get(char, 0)

            for pattern in self.output.get(node_id, []):
                results.append((i - len(pattern) + 1, pattern))

        return results

patterns = ["at", "cat", "hat", "hate", "ate"]
text = "the cat in the hat hated to wait and ate late"

aho_corasick = AhoCorasick()
for pattern in patterns:
    aho_corasick.add_pattern(pattern)

aho_corasick.build()
results = aho_corasick.search(text)

print("Found patterns:")
for position, pattern in results:
    print(f"Pattern '{pattern}' found at position {position}.")
