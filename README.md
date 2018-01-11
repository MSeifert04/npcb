# npcb
Read the string representation of a NumPy array from the clipboard

For example copy the following line (for example using Ctrl + C):

    [1 2 3 4 5]

Then use `npcb.array` to convert this string representation of a NumPy array
to an actual NumPy array again:

    >>> npcb.array()
    array([1, 2, 3, 4, 5])

It's that simple.

It can handle simple dtypes (no masked arrays or structured arrays) and
multidimension arrays like:

    array([1, 2, 3, 4], dtype=uint16)

    [[0.06076787 0.93465143 0.78973447]
     [0.33608162 0.71548182 0.13196038]
     [0.10906009 0.93785047 0.96137758]]