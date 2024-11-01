def top_n (items, n):
    """ Returns the top n items in an array, in desc order

    Args: 
        items (array): list or array like object
        n (int): number of items to return

    Return: 
        array: top n items in desc order

    Egs:
        >>> top_n([6,3,8,1,4,5], 3)
        [8,6,5]
    """

    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: # If the left item is greater than the right item
                items[j], items[j+1] = items[j+1], items[j] # swap the two items

     # Get the last n items in the list
    top_j = items[-n:] 

    # Return in descending order
    return top_j[::-1]



