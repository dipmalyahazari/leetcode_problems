class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_end=True

    def search(self,word):
        node=self.root
        
        for ch in word:
            if ch not in node.children:
                return False
            
            node=node.children[ch]
        return node.is_end

    def starts_with(self,prefix):
        node=self.root
        
        for ch in prefix:
            if ch not in node.children:
                return False
        
            node=node.children[ch]
        return True

if __name__=="__main__":
    t=Trie()
    t.insert("hello")
    t.insert("hi")
    print(t.starts_with("h"))
    print(t.search("hello"))
    print(t.search("no"))
