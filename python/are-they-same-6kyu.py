def comp(array1, array2):
    res = []
    if array1 != None and array2 != None:
        if len(array1) == 0 and len(array2) != 0:
            return False
        for e in array1:
            if e*e in array2:
                res.append(True)
                array2.remove(e*e)
            else:
                res.append(False)
        return all(res)
    else:
        return False