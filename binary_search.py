def bin_search(arr, target_value):
    minn = 0
    maxx = len(arr) - 1
    gss = 0

    # condition checking
    while gss != target_value:
        index_target = arr.index(target_value)
        target_value = arr[index_target]
        
        # first guess is the average of minn and maxx
        gss = arr[(minn + maxx) // 2]

        if gss == target_value:
            return arr.index(target_value)
        elif gss < target_value:
            minn = arr.index(gss) + 1
        elif gss > target_value:
            maxx = arr.index(gss) - 1
    
    return -1

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
target = int(input("Enter a prime number: "))
result = bin_search(data, target)
print("Data point found at index ", result)
