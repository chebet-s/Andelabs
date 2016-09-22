def find_max_min(lst):

    max_no = lst[0]
    min_no = lst[0]
    arrayMinMax = []

    for value in lst:
        if value < min_no:
            min_no = value
        elif value > max_no:
            max_no = value

    if max_no == min_no:
        arrayMinMax.append(len(lst))
        return arrayMinMax
    else:
        arrayMinMax.append(min_no)
        arrayMinMax.append(max_no)
        return arrayMinMax
