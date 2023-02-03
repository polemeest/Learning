def find_duplicate(lst):
    lst1 = [i for i in lst if lst.count(i) > 1]
    return (sorted(set(lst1), key=lst1.index))
