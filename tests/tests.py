from mypackage import myModule

def test_top_n ():
    """
    making sure that top n works correctly aganist certain test cases
    """

    assert myModule.top_n([6,3,8,1,4,5], 3) == [8,6,5], 'Incorrect'
    assert myModule.top_n([6,7,8,1,4,10], 2) == [10,8], 'Incorrect'
    assert myModule.top_n([6,3,8,1,4,5,44,76,1], 5) == [76,44,8,6,5], 'Incorrect'