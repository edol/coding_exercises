def merge(arr1,arr2):
    res = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    
    res.extend(arr1[i:])
    res.extend(arr2[j:])

    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)


if __name__ == '__main__':
    arr1 = [1,4,7,9,10]
    arr2 = [2,3,4,5,6]
    print(merge(arr1,arr2))
    arr = [5,3,8,6,3,4,8,9,18,15,10]
    print(merge_sort(arr))