from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    print(nums)
    len_nums = len(nums)
    res = []
    to_check = set()
    to_check_a = set()

    for i in range(len_nums - 2):
        a = nums[i]
        if a in to_check_a:
            continue
        else:
            to_check_a.add(a)

        low = i + 1
        high = len_nums - 1
        print(f"{i=} {low=} {high=}")
        # ii = 0
        while low < high:
            b = nums[low]
            c = nums[high]
            print(f"{i=} {low=} {high=} {a=} {b=} {c=}")

            if a + b + c == 0:
                if frozenset({a, b, c}) not in to_check:
                    to_check.add(frozenset({a, b, c}))
                    res.append([a, b, c])
                low += 1
                high -= 1

            elif a + b + c < 0:
                low += 1
            else:
                high -= 1

            # ii += 1
            # if ii > 50:
            #     res.append(None)
            #     return res
            #     break

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
    assert res == [[-1, -1, 2], [-1, 0, 1]]


def test4():
    nums = [-2, 0, 0, 2, 2]
    res = threeSum(nums)
    assert res == [[-2, 0, 2]]
