
n = 23
arr = [1, 1, 1, 2, 5, 5, 6, 8, 10, 5, 19]
# for n in arr:
#     print n

prev = arr[0]-1
for num in arr:
    if num > n:
        print 'false'
        break
    else:
        if num != prev:
            if n-num in arr:
                print 'true'
                break
            prev = num
print 'false'

