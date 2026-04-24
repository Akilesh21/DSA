def findMaxSquareWithAllZeros(input):
    arr = [[0] * len(input[0]) for _ in range(len(input))]
    
    for i in range(len(arr[0])):
        if input[0][i] == 0:
            arr[0][i] = 1
        else:
            arr[0][i] = 0
    
    for i in range(len(arr)):
        if input[i][0] == 0:
            arr[i][0] = 1
        else:
            arr[i][0] = 0
    
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            if input[i][j] != 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 1 + min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j])
    
    maximum = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > maximum:
                maximum = arr[i][j]
    
    return maximum
