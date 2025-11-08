def union_and_intersection(arr1: list[int], arr2: list[int]):
    set1, set2 = set(arr1), set(arr2)
    union = list(set1 | set2)
    intersection = list(set1 & set2)
    print("Union:", union)
    print("Intersection:", intersection)

union_and_intersection([1,2,2,1],[2,2])

