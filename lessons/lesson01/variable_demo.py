"""
课时 01 示例 3：变量是"标签"，不是"盒子"
体会 Python 变量与 C 变量的差异
"""

# 1. 同一个对象有多个标签
a = [1, 2, 3]
b = a              # b 和 a 贴在同一个 list 上
b.append(4)
print(f"a = {a}")  # [1, 2, 3, 4] —— a 也变了！
print(f"b = {b}")  # [1, 2, 3, 4]
print(f"a is b? {a is b}")  # True，是同一个对象
print(f"id(a)={id(a)}  id(b)={id(b)}")

# 2. 重新赋值 = 撕下标签贴到新对象上
a = [9, 9, 9]
print(f"\n重新赋值后 a = {a}, b = {b}")
print(f"a is b? {a is b}")  # False，不再是同一个对象
