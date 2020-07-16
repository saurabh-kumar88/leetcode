class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()
    
    # helper method - hash key gen
    def _charToIndex(self, ch):
        return ord(ch)-ord('a')
    
    
    # Add child
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pCrawl = self.root 
        length = len(word) 
        for level in range(length): 
            index = self._charToIndex(word[level]) 
  
            # if current character is not present 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
  
        # mark last node as leaf 
        pCrawl.isEndOfWord = True

        
    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        pCrawl = self.root 
        length = len(word) 
        for level in range(length): 
            index = self._charToIndex(word[level]) 
            print(index," - ", level)
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
  
        if ( pCrawl != None and pCrawl.isEndOfWord ):
            return True

        return False 
        

    def startsWith(self, prefix: str) -> bool:
        
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pCrawl = self.root 
        length = len(prefix)         
        
        for level in range(length): 
            index = self._charToIndex( prefix[level] ) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index]
        return True
        


# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":
    obj = Trie()
    obj.insert("apple")
    obj.insert("apology")
    obj.insert("aeroplane")
    
    # print( obj.search("apple") ) 
    print( obj.startsWith(prefix="Jada") )