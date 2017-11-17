class Node:
    '''
    Node - a component of a Trie.
    Attributes:
        letter (str): A single letter represented by the Node
        word (str): A word that ends at the Node after traversing through the Trie
        children ({letter: <Node>}): Structure representing subsequent 
            Nodes (and corresponding letters) that build into words
    '''
    def __init__(self, letter=None):
        '''
        Initialize a Node object.
        Args:
            letter (str): A single letter represented by the Node
        '''
        self.letter = letter
        self.word = None # Store a word if it ends at the Node
        self.children = {}  

    def addChild(self, letter):
        '''
        Add child to Node.
        Args:
            letter (str): Letter of child Node.
        '''
        if letter not in self.children:
            new_child = Node(letter)
            self.children[letter] = new_child

class Trie:
    '''
    Trie - a tree of Nodes to store words and their prefixes.
    Attributes:
        head (<Node>): A blank Node object that points to the head of the Trie
        words (set): The set of all the words that the Trie has stored
    '''
    def __init__(self):
        '''
        Initalize Trie with a blank Node as its head and an empty set of words.
        '''
        self.head = Node() # head of Trie is a blank Node
        self.words = set()

    def addWord(self, word, full_word=None):
        '''
        Add word to Trie.
        Args:
            word (str): Word to add letter by letter as Nodes to the Trie
            full_word (str): Word to store in Trie (at the last letter Node and in self.words) 
        '''
        if not full_word: # allows us to store alternate names in the nodes
            full_word = word
        self.words.add(full_word)
        current_node = self.head
        # remove white space and special characters
        simple_word = ''.join(char for char in word if char.isalnum()).lower() 
        for char in simple_word:
            # traverse the trie, adding new nodes when necessary
            if char not in current_node.children:
                current_node.addChild(char)
            current_node = current_node.children[char]
        # word is complete, so add to last node
        current_node.word = full_word

    def autocomplete(self, prefix):
        '''
        Return all words in Trie that begin with an input string.
        Args:
            prefix (str): String to query Trie for complete words for.
        Returns:
            list: List of words that are prefixed by prefix.
        '''
        complete_words = set()
        current_node = self.head
        # traverse the trie to find the node where the prefix ends
        simple_prefix = ''.join(char for char in prefix if char.isalnum()).lower()
        for char in simple_prefix:
            if char not in current_node.children:
                return complete_words
            current_node = current_node.children[char]

        # return all complete words below prefix --> use DFS to traverse rest of trie
        queue = [current_node]
        while queue:
            current_node = queue.pop()
            if current_node.word:
                complete_words.add(current_node.word)
            # append all of current node's children nodes to the queue
            queue.extend(list(current_node.children.values()))
        return list(complete_words)

