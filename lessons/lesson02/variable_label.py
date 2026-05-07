"""
课时 02 示例 2：变量是"标签"，不是"盒子"
体会可变 vs 不可变对象的差异
"""


def demo_immutable():
    print("===== 不可变对象（int / str / tuple） =====")
    a = 10
    b = a
    print(f"a={a}, b={b}, id(a)={id(a)}, id(b)={id(b)}")
    print(f"a is b? {a is b}\n")

    a = 20  # 把标签 a 撕下来贴到新对象上
    print(f"重新赋值 a=20 后：")
    print(f"a={a}, b={b}")
    print(f"a is b? {a is b}（不再是同一个对象）\n")


def demo_mutable():
    print("===== 可变对象（list / dict / set） =====")
    lst1 = [1, 2, 3]
    lst2 = lst1   # 两个标签贴在同一个 list 上！
    print(f"lst1={lst1}, lst2={lst2}")
    print(f"lst1 is lst2? {lst1 is lst2}\n")

    lst1.append(4)   # 通过 lst1 修改，lst2 也会变
    print(f"通过 lst1.append(4) 修改后：")
    print(f"lst1={lst1}")
    print(f"lst2={lst2}  ← 同时变了！")
    print(f"id 还是相同的：{id(lst1)} == {id(lst2)}\n")


def demo_small_int_cache():
    print("===== 小整数缓存（Python 的小秘密） =====")
    a = 256; b = 256
    print(f"a=256, b=256, a is b? {a is b}  (在缓存范围 -5~256)")

    a = 257; b = 257
    print(f"a=257, b=257, a is b? {a is b}  (超出缓存)")

    # 但 == 始终判断值
    print(f"257 == 257? {257 == 257}")


def demo_is_vs_eq():
    print("\n===== is vs == =====")
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(f"a == b? {a == b}  (值相等)")
    print(f"a is b? {a is b}  (是不是同一个对象)")


if __name__ == "__main__":
    demo_immutable()
    demo_mutable()
    demo_small_int_cache()
    demo_is_vs_eq()
