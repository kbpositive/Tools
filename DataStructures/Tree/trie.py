class Node:
    def __init__(self, val="", alphabet_length=26):
        self.val = val
        self.letter = [None]*alphabet_length

class Trie:
    def __init__(self,alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.alphabet = alphabet
        self.root = Node("",len(self.alphabet))

    def add(self,trie,word):
        if trie and word:
            if trie.letter[ord(word[0])-97] and len(word) > 1:
                self.add(trie.letter[ord(word[0])-97],word[1:])
            elif trie.letter[ord(word[0])-97] is None:
                trie.letter[ord(word[0])-97] = Node(word[0])
                self.add(trie.letter[ord(word[0])-97],word[1:])
            else:
                trie.letter[ord(word[0])-97] = Node(word[0])

if __name__ == '__main__':
    tr = Trie()
    for a in tr.alphabet:
        print(ord(a)-97)
    tr.add(tr.root,'test')
    traverse_test = tr.root.letter[ord('t')-97].letter[ord('e')-97].letter[ord('s')-97].letter[ord('t')-97].letter
    assert traverse_test == [None]*26
    print('pass')
