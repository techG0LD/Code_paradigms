def flatten_and_sort(lst):
    out = []
    for item in lst:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)
            

    return sorted(out)

nested = [0,-2,5,4,[5,344,4,19],[215,8585965]]

out = flatten_and_sort(nested)
print(out)
print(nested)

'''

'''