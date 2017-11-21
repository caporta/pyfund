"""
Python Name Scopes:

(L)ocal
(E)nclosing
(G)lobal
(B)uilt-in
"""

count = 0

def show_count():
    print('count = ', count)


def set_count(c):
    """
    Declare `count` as reference to global variable or the Python runtime
    will set new, local binding of `count` (shadow) and perform no lookup
    """
    global count
    count = c
