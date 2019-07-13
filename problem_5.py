## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                # print("This char was not in the trieNode: " + str(char))
                current_node.children[char] = TrieNode()

            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        ##examples of suffixes that represent prefix "u": untion, actory, un
        current_node = self.root
        for char in prefix:
            if char not in current_node.children.keys():
                ##this prefix is not in part of the values in the
                return None
        return current_node

class TrieNode:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.children = {}
        self.is_word = False

    def insert(self, word):
        current_node[char] = TrieNode()

    def suffixes(self, suffix = ''):

        def suffixes_rec(trie_node, suffix, result):
            # base case
            if not trie_node.children:
                result.append(suffix)
            else:
                for char in trie_node.children:
                    suffixes_rec(trie_node.children[char], suffix + char, result)

        results = []
        suffixes_rec(self, suffix, results)
        return results

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
