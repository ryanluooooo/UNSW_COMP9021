
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''


    # Insert your code here
    banknote_values = [100, 50, 20, 10, 5, 2, 1]
    banknotes = dict.fromkeys(banknote_values)
    
    index = 0
    while N>0 and index<=len(banknote_values)-1:
        count,N = divmod(N,banknote_values[index])
        if count >0:
            banknotes[banknote_values[index]]=count
        index +=1
    print('Here are your banknotes:')
    for value in (banknotes):
        if banknotes[value]:
            print(f'{"${}: {}".format(value,banknotes[value]):>4}')
        
        
        



            
    # Insert your code here
  
                        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
