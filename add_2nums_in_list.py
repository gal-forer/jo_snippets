
n = 10
arr = [1, 1, 1, 2, 5, 5, 6, 7, 10, 19, 19]
# for n in arr:
#     print n

prev = arr[0]-1
res = False
for num in arr:
    if num > n:
        break
    else:
        if num != prev:
            if n-num in arr and n-num != num:
                res = True
                break
            prev = num
print res

