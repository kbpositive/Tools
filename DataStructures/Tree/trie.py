class Node:
    def __init__(self, val="", alphabet_length=26):
        self.val = val
        self.letter = [None]*alphabet_length
        self.end = False

class Trie:
    def __init__(self,alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.alphabet = alphabet
        self.root = Node("",len(self.alphabet))

    def add(self,trie,word):
        if trie:
            if word:
                if trie.letter[ord(word[0])-97] and len(word) > 1:
                    self.add(trie.letter[ord(word[0])-97],word[1:])
                elif trie.letter[ord(word[0])-97] is None:
                    trie.letter[ord(word[0])-97] = Node(word[0])
                    self.add(trie.letter[ord(word[0])-97],word[1:])
                else:
                    trie.letter[ord(word[0])-97] = Node(word[0])
                    trie.letter[ord(word[0])-97].end = True
            else:
                trie.end = True

    def print_trie(self,node,count):
        if node:
            for index,key in enumerate([l for l in node.letter if l]):
                if index > 0:
                    print('  '*count,end='')
                print(key.val,end='')
                if key.end == False:
                    print('-',end='')
                else:
                    print('\n',end='')
                self.print_trie(key,count+1)

if __name__ == '__main__':
    tr = Trie()

    tr.add(tr.root,'test')
    traverse_test = tr.root.letter[ord('t')-97].letter[ord('e')-97].letter[ord('s')-97].letter[ord('t')-97]
    assert traverse_test.letter == [None]*26
    assert traverse_test.end == True

    tr.add(tr.root,'taxes')
    tr.add(tr.root,'harry')
    tr.add(tr.root,'potter')
    tr.add(tr.root,'taste')
    tr.add(tr.root,'teacher')
    tr.add(tr.root,'parasaur')
    tr.print_trie(tr.root,0)
    print('pass')
