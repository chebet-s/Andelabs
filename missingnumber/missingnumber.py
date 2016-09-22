def find_missing(arr1, arr2):
    if len(arr1) == len(arr2):
        return 0
    else:
        #Assume that arr1 is the bigger one
        BigArray = arr1 
        if len(arr2) > len(BigArray):
            BigArray = arr2
            SmallArray = arr1
        else:
            SmallArray = arr2
        for num in BigArray:
            if num not in SmallArray:
                return num
