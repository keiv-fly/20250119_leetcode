from typing import List


def maxArea(height: List[int]) -> int:
    max_a = 0
    # 1st and last
    min_height_1st = min(height[0], height[-1])
    max_a = min_height_1st * (len(height) - 1)
    j_max_a = len(height) - 1

    print(f"len_height: {len(height)}")
    print(f"min_height_1st: {min_height_1st}")

    # quaters
    i = len(height) // 4
    j = len(height) * 3 // 4
    if i != j:
        min_height_quaters = min(height[i], height[j])
        print(f"min_height_quaters: {min_height_quaters}")
        a_quaters = min_height_quaters * (j - i)
        if a_quaters > max_a:
            max_a = a_quaters
            j_max_a = j
    print(max_a)

    j_max_height = 0
    for j in range(len(height)):
        if height[j] > height[j_max_height]:
            j_max_height = j

    j_array = set()
    for j in range(len(height)):
        if j< j_max_height:
            continue
        j_array.add(j)

    height_j_max_a = height[j_max_a]
    i_count = 0
    for i in range(len(height)):
        if height[i] < min_height_1st:
            continue
        if height[i] == 0:
            continue
        if height[i] * (j_max_a - i) < max_a:
            continue
        if i_count < 100:
            print(f"i:{i} Hyp_area:{height[i] * (j_max_a - i)} len_j_array:{len(j_array)}")
            # print(f"i:{i} Hyp_area:{height[i] * (j_max_a - i)} len_j_array:{len(j_array)}, j_array:{" ".join([str(x) for x in j_array])}")
            # print(f"")
        i_count += 1
        j_array_copy = j_array.copy()
        for j in j_array_copy:
            # print(f"j:{j} Hyp_area:{height[i] * (j_max_a - i)} len_j_array:{len(j_array)}, j_array:{" ".join([str(x) for x in j_array])}")
            if j <= i:
                j_array.remove(j)
                continue
            if height[j] < min_height_1st:
                j_array.remove(j)
                continue
            # if height[j] < height_j_max_a:
            #     j_array.remove(j)
            #     continue
            if height[j] < max_a/(j - i):
                j_array.remove(j)
                continue
            # print(f"hi")
            min_height = min(height[i], height[j])
            test_a = (j - i) * min_height
            if test_a > max_a:
                max_a = test_a
                j_max_a = j
                height_j_max_a = height[j_max_a]
    return max_a


