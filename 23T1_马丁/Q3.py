# You can assume that the function is called with a strictly positive
# integer as first argument and either True or False as second argument,
# if any.


def rhombus(size, shift_right=False):
    '''
    >>> rhombus(1)
    A
    >>> rhombus(1, True)
    A
    >>> rhombus(2)
     BA
    CD
    >>> rhombus(2, True)
    AB
     DC
    >>> rhombus(3)
      CBA
     DEF
    IHG
    >>> rhombus(3, True)
    ABC
     FED
      GHI
    >>> rhombus(4)
       DCBA
      EFGH
     LKJI
    MNOP
    >>> rhombus(4, True)
    ABCD
     HGFE
      IJKL
       PONM
    >>> rhombus(7)
          GFEDCBA
         HIJKLMN
        UTSRQPO
       VWXYZAB
      IHGFEDC
     JKLMNOP
    WVUTSRQ
    >>> rhombus(7, True)
    ABCDEFG
     NMLKJIH
      OPQRSTU
       BAZYXWV
        CDEFGHI
         PONMLKJ
          QRSTUVW
    '''
    pass
    # REPLACE PASS ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
