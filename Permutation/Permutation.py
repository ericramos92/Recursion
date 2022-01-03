def perm1(nums):
    results = []
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums[:]]
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = perm1(nums)
        for perm in perms:
            perm.append(n)

        results.extend(perms)
        nums.append(n)
    return results


array = [1, 2, 3]
print(perm1(array))





































#https://www.youtube.com/watch?v=s7AvT7cGdSo