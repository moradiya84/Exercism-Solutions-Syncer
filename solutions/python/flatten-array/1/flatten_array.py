def flatten(iterable):
    if iterable == None:
        return []
    if isinstance(iterable,int):
        return [iterable]
    l = []
    flat = []
    for item in iterable:
        for i in flatten(item):
            flat.append(i)
    return flat
