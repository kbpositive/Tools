class Node:
    def __init__(self, symbol="", alphabet_length=26):
        self.symbol = symbol
        self.letters = [None]*alphabet_length
        self.end = False

class Tree:
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

    def print_trie(self,node,depth):
        for count,character in enumerate([letter for letter in node.letters if letter]):
            if count > 0:
                print('  '*depth,end='')
            print(character.symbol,end='')
            if character.end == False:
                print('-',end='')
            else:
                print('\n',end='')
                if character.letters != [None]*len(self.alphabet):
                    print('  '*(depth+1),end='')
            self.print_trie(character,depth+1)

if __name__ == '__main__':
    tr = Tree()

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
    tr.add('tastefull')
    tr.add('teacher')
    tr.add('parasaur')
    tr.add('general')
    tr.add('generalize')
    tr.add('generalization')
    tr.add('generalizational')
    tr.add('generalizationalize')
    tr.add('generalizationalization')

    tr.print_trie(tr.root,0)
    print('\npass')
