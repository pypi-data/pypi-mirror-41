The function ``flatten(*argv)`` takes an arbitrary amount of tuples and returns the sum of of each indices' value. The tuples should have the same length.
    | *Example:*
    | >>> from tuple_flatten import flatten
    | >>> flatten((1, 5), (2, 7))
    | (3, 12)::

It is not necessary for all tuples to be equally sized, as long as each tuple in the arguments is either shorter or equally sized as its predecessor.
    | *Example:*
    | >>> flatten((1, 7), (3,))
    | (4, 7)::
