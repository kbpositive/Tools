def seq(n):
    while True:
        yield n
        n += 1

sieve = lambda x,y,z: y if x == 0 else sieve(x-1,next(z),(i for i in z if i % y != 0))

if __name__ == '__main__':
    assert sieve(1000,2,seq(2)) == 7919
    print('\npass')
    
