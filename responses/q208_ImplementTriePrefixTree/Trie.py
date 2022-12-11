class TrieNode:
    def __init__(self):
        # initialize an array of length 26 (point to other trienodes)
        self.children = [None] * 26
        # is this the end? (end if has no children, O(1) operation instead of scanning children array
        # in which the scan would be O(N))
        self.isEnd = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # O(n), where n is the size of word, O(n) space
        cNode = self.root
        for char in word:
            # convert lowercase letter to ascii code, then constrain to bounds 0->25 inclusive
            charIndex = ord(char) - ord('a')
            if not cNode.children[charIndex]:
                cNode.children[charIndex] = TrieNode()
            cNode = cNode.children[charIndex]
        
        cNode.isEnd = True


    def search(self, word: str) -> bool:
        # O(n), where n is the size of word, O(1) space
        cNode = self.root
        for char in word:
            charIndex = ord(char) - ord('a')
            if cNode.children[charIndex]:
                cNode = cNode.children[charIndex]
            else:
                return False
        return cNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        # O(n), where n is the size of word, O(1) space
        cNode = self.root
        for char in prefix:
            charIndex = ord(char) - ord('a')
            if cNode.children[charIndex]:
                cNode = cNode.children[charIndex]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)