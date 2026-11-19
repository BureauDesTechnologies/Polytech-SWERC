class Node:
    def __init__(self):
        self.ending = 0
        self.transitions = [-1] * 26
        self.count = 0
class Trie:
    def __init__(self):
        self.nodes = []
        self.root = Node()

    def add_string(self, s):
        """
        Add a string to the trie in O(len(s)).
        """
        current = self.root
        for c in s:
            current.count += 1
            if current.transitions[c] == -1:
                new_node = Node(c)
                self.nodes.append(new_node)
                current.transitions[c] = len(self.nodes) - 1
                current = new_node
            else:
                current = self.nodes[current.transitions[c]]
        current.count += 1
        current.ending += 1

    def contains(self, s, pref=False):
        """
        Check if s is a prefix/fully contained, in O(len(s)).
        """
        current = self.root
        for c in s:
            if current.transitions[c] == -1:
                return False
            current = self.nodes[current.transitions[c]]
        return True if not pref else (current.ending)
            