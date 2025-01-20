from typing import List


def get_digits(num: int) -> List[int]:
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num = num // 10
    return digits


def intToRoman(num: int) -> str:
    symbols = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    substraction_digit = {0: "I", 1: "X", 2: "C"}

    digits = get_digits(num)
    # digits.reverse()
    print(digits)
    res = ""
    rem_num = num
    ii = 0
    while rem_num != 0:
        digits = get_digits(rem_num)
        i = len(digits) - 1
        digit = digits[i]
        print(f"ii:{ii} rem_num:{rem_num} digits:{digits}")
        if digit != 4 and digit != 9:
            for k, v in symbols.items():
                if rem_num >= k:
                    res += v
                    rem_num -= k
                    break
        else:
            res += substraction_digit[i]
            rem_num += 10**i

        ii += 1
        if ii > 100:
            break

    return res


def test1():
    num = 3749
    res = intToRoman(num)
    assert res == "MMMDCCXLIX"
