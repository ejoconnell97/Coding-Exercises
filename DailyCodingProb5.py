def daily_prob_5():
    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair

    '''
    Implement car(pair) and cdr(pair) which return the first element and last
        element of a pair respectively

    Assumptions:
        - Each pair contains exactly two integers
    '''
    def car(p):
        print (p(first))
        return p(first)


    def cdr(p):
        print (p(last))
        return p(last)

    def first(a, b):
        return a

    def last(a, b):
        return b

    
    x = cons(1,2)
    car(x)
    cdr(x)







daily_prob_5()
