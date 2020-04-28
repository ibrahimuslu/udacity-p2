
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
    
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = [] # return list of suffixes
        # print(suffixes)
        # recursive suffix creation code to return list
        def suffix_rec(current_node, c, suffix=''):
            for (idx,char) in enumerate(current_node.children): 
                if idx > 0 :
                    suffix=suffix+c
                suffix=suffix+char
                if current_node.children[char].is_word:
                    suffixes.append(suffix)
                    if len(current_node.children[char].children) > 0:
                        suffix_rec(current_node.children[char],char, suffix)
                else:
                    suffix_rec(current_node.children[char],char, suffix)
                suffix='' # on going out erase the suffix
        suffix_rec(self,'','') 
        return suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix   
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node

# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

MyTrie = Trie()
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            # print(prefixNode.suffixes
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

f('a')
f(prefix='an')
f(prefix='tri')
f(prefix='f')
f(prefix='fu')