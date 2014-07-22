if __name__=='__main__':
    subtotal = 12.32
    tax = subtotal * 0.07
    total = subtotal + tax

    '''
    The 0.2f format specifier after the colons says,
    from left to right: for values lower than one,
    make sure a zero is displayed on the left side of the decimal point;
    show two places after the decimal;
    format the input value as a float
    '''
    print("Sub: ${0:0.2f} Tax: ${1:0.2f} Total: ${total:0.2f}".format(
        subtotal, tax, total=total)
        )

    orders = [('burger', 2, 5),('fries', 3.5, 1),('cola', 1.75, 3)]
    '''
    {0:10s}    The s means it is a string variable,
               the 10 means it should take up ten characters.
    {1: ^9d}   The d represents an integer value.
               The 9 tells us the value should take up nine characters.
               With integers the extra characters are zeros, by default.
               So we explicitly specify a space (immediately after the colon)
               as a padding character.
               The carat character ^ tells us that the number should be
               aligned in the center of this available padding;
               The specifiers have to be in the right order,
               although all are optional:
               Fill first, then align, then the size, and finally, the type.
    {2: <8.2f} Space as the fill character,
               we use the < to align to the left space of eight characters.
               Further, the float should be formatted to two decimal places.
    {2: >7.2f} Space as the fill character,
               we use the > to align to the right space of seven characters.
               Further, the float should be formatted to two decimal places.
    '''
    print("PRODUCT QUANTITY PRICE SUBTOTAL")
    for product, price, quantity in orders:
        subtotal = price * quantity
        print("{0:10s}{1: ^9d} ${2: <8.2f}${3: >7.2f}".format(
            product,
            quantity,
            price,
            subtotal)
            )

    '''
    The 'type' character for different types can affect formatting output.
    s, d, and f types, for strings, integers, and floats.
    Most of the other format specifiers are alternative versions of these;
    for example:
    d represents decimal format for integers
    b represents binary format for integers
    o represents octal format for integers
    X represents hexadecimal for integers
    n is for formatting integer separators in the current locale's format.
    For floating-point numbers, the % type will multiply by 100
    and format a float as a percentage.

    more at=> http://docs.python.org/3.3/library/string.html#formatspec
    '''
    print("decimal=> {0:d}".format(9)) #prints 9
    print("binary=> {0:b}".format(5)) #prints 100 => (1x4 + 0x2 + 1x1)
    print("octal=> {0:o}".format(9)) #prints 11 => (1x8 + 1x1)
    print("hexadecimal=> {0:X}".format(27)) #prints 1B => (1x16 + 11x1)
    print("current locale's format=> {0:n}".format(1001)) #prints 1001 or 1,001
    print("percentage=> {0:.2%}".format(0.3)) #prints 30.00% => (0.3x100)
    
    
