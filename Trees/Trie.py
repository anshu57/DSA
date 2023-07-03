
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
# Time Complexity : O(1)
# Space Complexity : O(1)
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")
    # Time complexity : O(m)
    # Space Complexity : O(m)  m-- length of string

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        
        if currentNode.endOfString == True:
            return True
        else:
            return False
        
    # Time Complexity : O(m)
    # Space Complexity : O(1)
    # print(newTrie.searchString("BCD"))
        
    def deleteString(root, word, index):
        ch = word[index]
        currentNode = root.children.get(ch)
        canThisNodeBeDeleted = False
        if len(currentNode.children) > 1:
            deleteString(currentNode, word, index +1)
            return False
        if index == len(word) -1:
            if len(currentNode.children) >=1:
                currentNode.endOfString = False
                return False
            else:
                root.children.pop(ch)
                return True
        if currentNode.endOfString == True:
            deleteString(currentNode, word, index +1)
            return False
        
        canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
        if canThisNodeBeDeleted == True:
            root.children.pop(ch)
            return True
        else:
            return False

        

newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")

deleteString(newTrie, "App", 0)
print(newTrie.searchString("App"))





