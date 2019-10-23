# method that prints all anagrams from a given word.
def print_anagrams(word, english_words, prefix=""):
   if len(word) <= 1:
       str = prefix + word
       # searches for word in english_words data structure, if the word if found then it exists.
       if english_words.find(str) is True:
           print(prefix + word)
   else:
       # creates different combinations of the word and search if its an actual word.
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words, prefix + cur)

# method that gives the total number of anagrams a word has.
# same as printing_anagrams method but instead of printing it return value.
def count_anagrams(word, english_words, prefix=""):
   count = 0
   if len(word) <= 1:
       str = prefix + word

       if english_words.find(str) is True:
           return 1
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               count += count_anagrams(before + after, english_words, prefix + cur)
   return count

# given a file, max_anagrams find the word that has the most anagrams.              
def max_anagrams(english_words):
    print("input the text file name")
    file = open(input())
    max_word = None
    for word in file:
        if max_word is None:
            max_word = word.rstrip()
        # compares the number of anagrams from each word and returns the word that has the most anagrams.
        elif count_anagrams(word.rstrip(), english_words) > count_anagrams(max_word, english_words):
            max_word = word.rstrip()
    return max_word

# class for node used in AVL tree.
class AVLNode:
    
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        
    def insert(self, node):
        if node is None:
            return
        # if item is greater than node go to right node.
        if self.key < node.key:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)
        # if item is less than node go to left node.
        else:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
                
    # searches for an item in the tree and return true if is found else return false.         
    def find(self, item):
        if self.key is None or self.key.lower().rstrip() == item.lower():
            return True
        # iterate to the left if item is less than node.
        elif self.key > item:
            if self.left is None:
                return False
            else:
                return self.left.find(item)
        #iterate to the right if item is greater than node.
        else:
            if self.right is None:
                return False
            return self.right.find(item)

# gets height of each node to check if tree is balanced.                
def height(node):
    if node is None:
        return -1
    return node.height

# gets new height when tree is changed.
def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

# class for AVL tree.        
class AVLTree():
    
    def __init__(self):
        self.root = None
        
    def insert_root(self, key):
        node = AVLNode(key, None)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        self.balance(node)
    
    # method that balances tree.    
    def balance(self, node):
        while node != None:
            update_height(node)
            if height(node.left) + 2 <= height(node.right):
                if height(node.right.left) <= height(node.right.right):
                    self.rotate_left(node)
                else:
                    self.rotate_right(node.right)
                    self.rotate_left(node)
            elif height(node.right) + 2 <= height(node.left):
                if height(node.left.right) <= height(node.left.left):
                    self.rotate_right(node)
                else:
                    self.rotate_left(node.left)
                    self.rotate_right(node)
            node = node.parent
            
    # move nodes to the right if tree is unbalanced
    def rotate_right(self, node):
        x = node.left
        x.parent = node.parent
        if x.parent is None:
            self.root = x
        else:
            if x.parent.left is node:
                x.parent.left = x
            elif x.parent.right is node:
                x.parent.right = x
        node.left = x.right
        if node.left != None:
            node.left.parent = node
        x.right = node
        node.parent = x
        update_height(node)
        update_height(x)
    
    # move nodes to the left is tree is unbalanced
    def rotate_left(self, node):
        x = node.right
        x.parent = node.parent
        if x.parent is None:
            self.root = x
        else:
            if x.parent.left is node:
                x.parent.left = x
            elif x.parent.right is node:
                x.parent.right = x
        node.right = x.left
        if node.right != None:
            node.right.parent = node
        x.left = node
        node.parent = x
        update_height(node)
        update_height(x)
    
    # fine helper
    def find(self, item):
        return self.root.find(item)
        
        
class RBNode():
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1
        
    def find(self, item):
        if self.key is None: 
            return False
        elif self.key.lower().rstrip() == item.lower():
            return True
        elif self.key > item:
            if self.left is None:
                return False
            else:
                return self.left.find(item)
        else:
            if self.right is None:
                return False
            return self.right.find(item)
        
class RBTree():
    
    # nil represents a node that is None for every child in the tree
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.left = None
        self.nil.right = None
        self.nil.color = 0
        self.root = self.nil
                
    def insert(self, item):
        node = RBNode(item)
        node.left = self.nil
        node.right = self.nil
        
        x = self.root
        y = None
        while x != self.nil:
            y = x
            if x.key > node.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif y.key > node.key:
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color =  0
            return
        if node.parent.parent == None:
            return
        self.fix_insert(node)
        
    # fixes or balance the tree when a node is inserted.
    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent.parent.left == node.parent:
                uncle = node.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rotate_left(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0
        
    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        if x.right != self.nil:
            x.right.parent = node
        x.parent = node.parent
        if node.parent == None:
            self.root = x
        elif node == node.parent.right:
            node.parent.right = x
        else:
            node.parent.left = x
        x.right = node
        node.parent = x
        
    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        if x.left != self.nil:
            x.left.parent = node
        x.parent = node.parent
        if node.parent == None:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        x.left = node
        node.parent = x
    
    # find helper.
    def find(self, item):
        return self.root.find(item)
        
def main():
    word_file = open("words.txt", "r")
    print("Input 1: AVL Tree")
    print("Input 2: Red-Black Tree")
    print("Input 3: check word with most anagram from a file")
    option =int(input())
    # option 1 AVLTree
    if option == 1:
        english_words = AVLTree()
        #insert all word from file in the tree
        for word in word_file:
            english_words.insert_root(word.lower())
        print("input any word for anagram")
        word = input()
        print_anagrams(word, english_words)
        print(count_anagrams(word, english_words))
    # option 2 RBTree
    elif option == 2:
        english_words = RBTree()
        for word in word_file:
            english_words.insert(word.lower())
        print("input any word for anagram")
        word = input()
        print_anagrams(word, english_words)
        print(count_anagrams(word, english_words))
    #option 3 get word with max anagrams.
    elif option == 3:
        english_words = RBTree()
        for word in word_file:
            english_words.insert(word.lower())
        print(max_anagrams(english_words))

main()