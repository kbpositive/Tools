class Node:
    def __init__(self, symbol="", alphabet_length=26):
        self.symbol = symbol
        self.letters = [None]*alphabet_length
        self.end = False

class Trie:
    def __init__(self,alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.alphabet = alphabet
        self.root = Node("",len(self.alphabet))

    def add(self,word):
        current = self.root
        for letter in word:
            if current.letters[ord(letter)-97] is None:
                current.letters[ord(letter)-97] = Node(letter)
            current = current.letters[ord(letter)-97]
        current.end = True

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

    tr.add('test')
    traverse_test = tr.root.letters[ord('t')-97].letters[ord('e')-97].letters[ord('s')-97].letters[ord('t')-97]
    assert traverse_test.letters == [None]*26
    assert traverse_test.end == True

    tr.add('taxes')
    tr.add('harry')
    tr.add('potter')
    tr.add('taste')
    tr.add('tasty')
    tr.add('tasteless')
    tr.add('teacher')
    tr.add('parasaur')
    tr.add('general')
    tr.add('generalize')
    tr.add('generalization')
    tr.add('generalizational')
    tr.add('generalizationalize')
    tr.add('generalizationalization')

    tr.print_trie(tr.root,0)
    print('pass')
