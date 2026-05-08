"""课时 02 示例 2：变量是标签，不是盒子"""

# 演示 1：变量重新赋值，对象 id 会变
x = 5
print(f"x=5, id={id(x)}")
x = 6
print(f"x=6, id={id(x)}")  # 不一样

# 演示 2：两个变量指向同一个对象
a = [1, 2, 3]
b = a
print(f"a is b? {a is b}")  # True
b.append(4)
print(f"a = {a}")  # [1, 2, 3, 4]，a 也变了！

# 演示 3：相同值不一定是同一对象
x = [1, 2, 3]
y = [1, 2, 3]
print(f"x == y? {x == y}")  # True
print(f"x is y? {x is y}")  # False

# 演示 4：小整数缓存
m = 256
n = 256
print(f"256: m is n? {m is n}")  # True

m = 257
n = 257
print(f"257: m is n? {m is n}")  # False（!!）
