''' ord(c) returns the encoding of character c.
    chr(e) returns the character encoded by e.
'''
def f(n):
    '''
    >>> f(1)
    A
    >>> f(2)
     A
    CBC
    >>> f(3)
      A
     CBC
    EDCDE
    >>> f(4)
       A
      CBC
     EDCDE
    GFEDEFG
    >>> f(30)
                                 A
                                CBC
                               EDCDE
                              GFEDEFG
                             IHGFEFGHI
                            KJIHGFGHIJK
                           MLKJIHGHIJKLM
                          ONMLKJIHIJKLMNO
                         QPONMLKJIJKLMNOPQ
                        SRQPONMLKJKLMNOPQRS
                       UTSRQPONMLKLMNOPQRSTU
                      WVUTSRQPONMLMNOPQRSTUVW
                     YXWVUTSRQPONMNOPQRSTUVWXY
                    AZYXWVUTSRQPONOPQRSTUVWXYZA
                   CBAZYXWVUTSRQPOPQRSTUVWXYZABC
                  EDCBAZYXWVUTSRQPQRSTUVWXYZABCDE
                 GFEDCBAZYXWVUTSRQRSTUVWXYZABCDEFG
                IHGFEDCBAZYXWVUTSRSTUVWXYZABCDEFGHI
               KJIHGFEDCBAZYXWVUTSTUVWXYZABCDEFGHIJK
              MLKJIHGFEDCBAZYXWVUTUVWXYZABCDEFGHIJKLM
             ONMLKJIHGFEDCBAZYXWVUVWXYZABCDEFGHIJKLMNO
            QPONMLKJIHGFEDCBAZYXWVWXYZABCDEFGHIJKLMNOPQ
           SRQPONMLKJIHGFEDCBAZYXWXYZABCDEFGHIJKLMNOPQRS
          UTSRQPONMLKJIHGFEDCBAZYXYZABCDEFGHIJKLMNOPQRSTU
         WVUTSRQPONMLKJIHGFEDCBAZYZABCDEFGHIJKLMNOPQRSTUVW
        YXWVUTSRQPONMLKJIHGFEDCBAZABCDEFGHIJKLMNOPQRSTUVWXY
       AZYXWVUTSRQPONMLKJIHGFEDCBABCDEFGHIJKLMNOPQRSTUVWXYZA
      CBAZYXWVUTSRQPONMLKJIHGFEDCBCDEFGHIJKLMNOPQRSTUVWXYZABC
     EDCBAZYXWVUTSRQPONMLKJIHGFEDCDEFGHIJKLMNOPQRSTUVWXYZABCDE
    GFEDCBAZYXWVUTSRQPONMLKJIHGFEDEFGHIJKLMNOPQRSTUVWXYZABCDEFG
    '''
    if n <1:
        return

    # 1. A开始
    # 2.从中间开始，对称
    # 3.每行都是奇数
    # 4.左边空格数
    # 5.反转
    # 6.Z 后面是A

    # 打印有两种，一种是放到列表
    # 边打印边输出

    offset = 0

    for i in range(1, n + 1):
        space = ''
        for _ in range(n - i):
            space += ' '
        print(space, end='')
        center = chr(65+offset)
        if offset == 25:
            offset = 0
        else:
            offset += 1
        track = []
        pointer_c = offset
        for j in range(i-1):
            #print(chr(pointer), end='')
            track.append(chr(65 + pointer_c))
            if pointer_c < 25:
                pointer_c += 1
            else:
                pointer_c = 0
        for k in range(-1, -len(track) - 1, -1):
            print(track[k], end='')
        print(center,end='')
        for l in range(len(track)):
            print(track[l],end='')

        print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # f(3)
