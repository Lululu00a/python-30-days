"""课时 02 示例 1：5 大基础类型演示"""

# int —— 任意精度
big = 2 ** 100
print(f"2^100 = {big}")
print(f"位数 = {len(str(big))}")

# float —— 64 位浮点
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # 经典浮点误差
print(f"是否相等 0.3? {0.1 + 0.2 == 0.3}")  # False!

# bool —— 是 int 的子类
print(f"True + True = {True + True}")  # 2
print(f"isinstance(True, int) = {isinstance(True, int)}")  # True

# str —— 不可变
s = "hello"
print(f"s.upper() = {s.upper()}")
print(f"s 本身没变 = {s}")

# None —— 全局唯一
x = None
y = None
print(f"x is y? {x is y}")  # True
