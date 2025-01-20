from typing import List


def get_digits(num: int) -> List[int]:
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num = num // 10
    return digits


def longestCommonPrefix(strs: List[str]) -> str:
    len_letters = len(strs[0])
    for s in strs[1:]:
        if len(s) < len_letters:
            len_letters = len(s)
    print(f"{len_letters=}")
    if len_letters == 0:
        return ""
    checked = set()
    max_longest = len_letters - 1
    i = len_letters // 2
    ch_first_str = strs[0][i]
    b_while = True
    while b_while:
        b_checked_positive = True
        for str in strs[1:]:
            if ch_first_str != str[i]:
                max_longest = i - 1
                i_prev = i
                i = i // 2
                b_checked_positive = False
                if i == i_prev:
                    b_while = False
                break
        if b_checked_positive:
            checked.add(i)
        break

    res = ""
    main_for_break = False
    for i in range(max_longest + 1):
        ch_first_str = strs[0][i]
        if i in checked:
            res += ch_first_str
            continue

        for str in strs[1:]:
            if ch_first_str != str[i]:
                main_for_break = True
        if main_for_break:
            break
        else:
            res += ch_first_str

    print(checked)
    return res


def test1():
    strs = ["flower", "flow", "flight"]
    res = longestCommonPrefix(strs)
    assert res == "fl"


def test2():
    strs = ["dog", "racecar", "car"]
    res = longestCommonPrefix(strs)
    assert res == ""
