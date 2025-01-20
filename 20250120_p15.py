from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    len_nums = len(nums)
    res = []
    to_check = set()
    to_check_c = {}
    for i, x in enumerate(nums):
        if x not in to_check_c.keys():
            to_check_c[x] = {i}
        else:
            to_check_c[x].add(i)

    for i in range(len_nums):
        a = nums[i]
        for j in range(i + 1, len_nums):
            b = nums[j]
            c = -a - b
            if frozenset({a, b, c}) not in to_check:
                to_check.add(frozenset({a, b, c}))
                c_indices = to_check_c.get(c)
                if c_indices is not None:
                    for c_index in c_indices:
                        if c_index != i and c_index != j:
                            res.append([a, b, c])
                            break
    return res


def test1():
    nums = [0, 1, 1]
    res = threeSum(nums)
    assert res == []


def test2():
    nums = [0, 0, 0]
    res = threeSum(nums)
    assert res == [[0, 0, 0]]


def test3():
    nums = [-1, 0, 1, 2, -1, -4]
    res = threeSum(nums)
    assert res == [[-1, 0, 1], [-1, -1, 2]]
