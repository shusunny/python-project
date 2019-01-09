def unique_list(l):
    # Also possible to use list(set())
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

list = [1,1,1,1,2,2,3,3,3,3,4,5]

print(unique_list(list))