"""练习 2 参考答案：小整数缓存验证"""

a = 256
b = 256
print(f"256 is 256: {a is b}")  # True

c = 257
d = 257
print(f"257 is 257: {c is d}")  # False（在 .py 文件中）

# 解释：CPython 对 -5~256 的小整数做了对象缓存（small int cache）
# 这些值在解释器启动时就预先创建好，所有引用都指向同一对象
# 257 超出缓存范围，每次赋值都创建新对象
print("\n说明：CPython 缓存了 -5 ~ 256 的整数对象")
print(f"id(a) = {id(a)}, id(b) = {id(b)}")
print(f"id(c) = {id(c)}, id(d) = {id(d)}")
