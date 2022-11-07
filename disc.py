def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t)== x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b,x) 
        if path:
            return [label(t)]+path
    #
    #
    #
    #
    #
    #
    #
    #
    # #Correct Version
    # if is_leaf(t) and label(t) != x:
    #     return None
    # elif label(t) == x:
    #     return [label(t)]
    # else:
    #     for b in branches(t):
    #         if find_path(b, x):
    #             return [label(t)] +find_path(b, x)




def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

