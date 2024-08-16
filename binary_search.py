def bin_search(arr, target_value):
    minn = 0 # min is 0 since the counting starts from 0
    maxx = len(arr) - 1 # the max is set to length of the array since 
    gss = 0
    
    # condition checking: this loop while run as long as maxx > minn
    while maxx > minn:
        # first guess is the average of minn and maxx
        gss = arr[(minn + maxx) // 2]

        if arr.index(gss) == arr.index(target_value):
            return arr.index(gss)
        elif arr.index(gss) < arr.index(target_value):  
            minn = arr.index(gss) + 1
        elif arr.index(gss) > arr.index(target_value):
            maxx = arr.index(gss) - 1
    
    # -1 will be returned if target value is not in the list 
    return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
target = int(input("Enter a prime number: "))
result = bin_search(primes, target)
print("Data point found at index ", result)
