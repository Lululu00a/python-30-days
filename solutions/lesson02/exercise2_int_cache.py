"""
练习 2 参考答案：验证 Python 小整数缓存（-5 ~ 256）
"""


def check(x: int, y: int) -> None:
    print(f"a={x}, b={y}, a is b? {x is y}")


def main() -> None:
    a, b = 256, 256
    check(a, b)

    a, b = 257, 257
    check(a, b)

    a, b = -5, -5
    check(a, b)

    a, b = -6, -6
    check(a, b)

    print("\n结论：Python 缓存了 -5 到 256 的小整数对象，")
    print("      在此范围内同值变量共享同一对象，所以 is 返回 True。")
    print("      超出范围会创建新对象，is 返回 False，但 == 始终判断值相等。")


if __name__ == "__main__":
    main()
