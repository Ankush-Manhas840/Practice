arr = [10, 22, 12, 3, 0, 6]

maxSoFar = arr[-1]
result = [arr[-1]]
for x in range(len(arr)-2, -1, -1):
    if arr[x] > maxSoFar:
        result.append(arr[x])
        maxSoFar = arr[x]
result.reverse()
print(result)
