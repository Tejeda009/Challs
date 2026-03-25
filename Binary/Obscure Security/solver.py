def swap(a1):
    for i in range(len(a1)):
        result = len(a1)
        if ( i >= a1 ):
            break
        a1[i] += a1[i + 1]
        a1[i + 1] += a1[i]
        a1[i] = a1[i + 1] - a1[i]
        a1[i + 1] = a1[i + 1] - a1[i] - a1[i]
    
    return a1
