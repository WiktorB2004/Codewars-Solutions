def triple_double(num1, num2):
    for i in range(0,10):
        if str(num1).count(str(i)) >= 3 and str(num2).count(str(i)) == 2:
                return 1
    return 0