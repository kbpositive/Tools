class Node:
    def __init__(self, symbol="", alphabet_length=26):
        self.symbol = symbol
        self.letters = [None]*alphabet_length
        self.end = False

class Trie:
    def __init__(self,alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.alphabet = alphabet
        self.root = Node("",len(self.alphabet))

    def add(self,trie,word):
        if trie:
            if word:
                if trie.letters[ord(word[0])-97] and len(word) > 1:
                    self.add(trie.letters[ord(word[0])-97],word[1:])
                elif trie.letters[ord(word[0])-97] is None:
                    trie.letters[ord(word[0])-97] = Node(word[0])
                    self.add(trie.letters[ord(word[0])-97],word[1:])
                else:
                    trie.letters[ord(word[0])-97].symbol = word[0]
                    trie.letters[ord(word[0])-97].end = True
            else:
                trie.end = True

    def print_trie(self,node,count):
        if node:
            for index,key in enumerate([l for l in node.letters if l]):
                if index > 0:
                    print('  '*count,end='')
                print(key.symbol,end='')
                if key.end == False:
                    print('-',end='')
                else:
                    print('\n',end='')
                    if key.letters != [None]*len(self.alphabet):
                        print('  '*count+key.symbol,end='-')

                self.print_trie(key,count+1)

if __name__ == '__main__':
    tr = Trie()

    tr.add(tr.root,'test')
    traverse_test = tr.root.letters[ord('t')-97].letters[ord('e')-97].letters[ord('s')-97].letters[ord('t')-97]
    assert traverse_test.letters == [None]*26
    assert traverse_test.end == True

    tr.add(tr.root,'taxes')
    tr.add(tr.root,'harry')
    tr.add(tr.root,'potter')
    tr.add(tr.root,'taste')
    tr.add(tr.root,'tasty')
    tr.add(tr.root,'tasteless')
    tr.add(tr.root,'teacher')
    tr.add(tr.root,'parasaur')
    tr.add(tr.root,'general')
    tr.add(tr.root,'generalize')
    tr.add(tr.root,'generalization')
    tr.add(tr.root,'generalizational')
    tr.add(tr.root,'generalizationalize')
    tr.add(tr.root,'generalizationalization')

    tr.print_trie(tr.root,0)
    print('pass')
