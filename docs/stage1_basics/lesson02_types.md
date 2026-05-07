# 课时 02：基本数据类型与变量

> 时长：25–30 分钟
> 学完本课你将能：
> 1. 掌握 Python 5 大基础类型：`int / float / bool / str / None`
> 2. 理解"变量是标签而非内存盒子"的本质
> 3. 区分 `is` 与 `==` 的差别
> 4. 熟练使用 f-string 格式化字符串
> 5. 掌握类型转换 `int()`, `str()`, `float()`

---

## 1. Python 中"一切皆对象"（3 分钟）

C 中的 `int a = 10` 是把 10 这个值"装进" a 这块内存。
Python 中的 `a = 10` 是先在内存里创建一个 `int` 对象 10，再把标签 `a` 贴上去。

```python
a = 10
print(type(a))   # <class 'int'>
print(id(a))     # 对象的"内存地址"（其实是对象 ID）
```

🔑 **核心区别**：在 Python 里，**数字、字符串、布尔值，甚至 `None` 都是对象**，都有自己的方法和属性。

```python
# 看，连数字都是对象，可以调用方法
print((10).bit_length())   # 4，10 的二进制是 1010，需要 4 位
print("hello".upper())     # HELLO
```

---

## 2. 5 大基础类型（8 分钟）

### 2.1 整数 int

```python
a = 10
b = -5
c = 0xFF        # 十六进制 = 255
d = 0b1010      # 二进制   = 10
e = 1_000_000   # 下划线分隔，提高可读性（C 没有这特性）
print(a, b, c, d, e)
```

⚡ Python 整数**没有上限**！而 C 的 `int` 有 `INT_MAX` 限制。
```python
huge = 2 ** 1000   # 算 2 的 1000 次方，毫无压力
print(huge)
```

### 2.2 浮点数 float

```python
pi = 3.14
g = 9.8
e = 1.5e3        # 科学计数法 = 1500.0
print(pi, g, e)

# ⚠️ 浮点数精度坑（与 C 一样）
print(0.1 + 0.2)   # 0.30000000000000004，不是 0.3！
```

精确计算钱、税等场景请使用 `decimal.Decimal`（课时 18 详解）。

### 2.3 布尔 bool

```python
flag = True       # 注意首字母大写！C 里是 true
done = False      # C 里是 false

# bool 实际上是 int 的子类
print(True + 1)   # 2
print(False == 0) # True
```

**真值判断**（重要！）：
```python
# 以下值都被判定为"假"
bool(0)          # False
bool(0.0)        # False
bool("")         # False（空字符串）
bool([])         # False（空列表）
bool(None)       # False

# 其他都是"真"
bool(-1)         # True
bool("False")    # True（非空字符串！）
bool([0])        # True（非空列表）
```

### 2.4 字符串 str

```python
s1 = '单引号'
s2 = "双引号"          # 单双引号等价，可互相嵌套：'He said "hi"'
s3 = """三引号
能跨多行"""
s4 = r"C:\Users\name"  # raw string，反斜杠不转义（写 Windows 路径神器）

# 字符串 + 拼接
greeting = "Hello, " + "Python"

# 字符串 * 重复
line = "-" * 30        # ------------------------------

# 索引与切片（与 C 字符数组完全不同！）
s = "Python"
print(s[0])    # P
print(s[-1])   # n （倒数第一个）
print(s[1:4])  # yth （切片：左闭右开）
print(s[::-1]) # nohtyP （反转字符串）
```

⚠️ **字符串是不可变的**！与 C 不同，你不能 `s[0] = 'X'`。

### 2.5 None — 空值

```python
result = None        # 类似 C 的 NULL，但更安全
print(type(result))  # <class 'NoneType'>

# 判断 None 用 is，不用 ==
if result is None:
    print("没有结果")
```

---

## 3. 变量是"标签"，不是"盒子"（5 分钟，重点！）

### 3.1 经典实验

```python
a = 10
b = a        # 把标签 b 也贴到对象 10 上
print(id(a), id(b))   # 两个 ID 完全相同！

a = 20       # 把标签 a 撕下来，贴到对象 20 上
print(id(a), id(b))   # ID 不一样了，b 还在 10 上
print(b)              # b 还是 10
```

### 3.2 可变对象 vs 不可变对象（重要！）

| 不可变 | 可变 |
|--------|------|
| `int / float / bool / str / tuple / None` | `list / dict / set` |

```python
# 不可变：每次"修改"其实是创建新对象
s = "hello"
print(id(s))       # 假设是 100
s = s + " world"
print(id(s))       # 变成了 200，新对象！

# 可变：原地修改
lst = [1, 2, 3]
print(id(lst))     # 假设是 300
lst.append(4)
print(id(lst))     # 还是 300！同一个对象
```

### 3.3 小整数缓存（Python 的小秘密）

```python
a = 256; b = 256
print(a is b)      # True ← 因为 -5~256 是 Python 预分配的小整数缓存

a = 257; b = 257
print(a is b)      # False ← 超出缓存范围，是两个独立对象
```

🧠 这就是为什么判断"是否是同一个对象"用 `is`，而判断"值是否相等"用 `==`。

---

## 4. f-string 格式化字符串（5 分钟）

f-string 是 Python 3.6+ 引入的字符串格式化方式，**强烈推荐用它**，简单又强大。

### 基础用法

```python
name = "Lulu"
age = 25
print(f"我叫{name}，今年{age}岁")     # 我叫 Lulu，今年 25 岁
```

### 格式化数字

```python
pi = 3.14159265

print(f"π ≈ {pi:.2f}")        # 保留 2 位小数：3.14
print(f"π ≈ {pi:.4f}")        # 保留 4 位小数：3.1416
print(f"{1234567:,}")         # 千分位分隔：1,234,567
print(f"{0.85:.1%}")          # 百分比：85.0%
print(f"{255:#x}")            # 十六进制：0xff
print(f"{10:5d}")             # 占 5 个字符宽度，右对齐：   10
print(f"{10:<5d}|")           # 左对齐：10   |
print(f"{10:>5d}|")           # 右对齐：   10|
print(f"{10:^5d}|")           # 居中：  10  |
print(f"{42:05d}")            # 0 填充：00042
```

### 表达式 / 调用方法

```python
x, y = 3, 4
print(f"{x} + {y} = {x + y}")          # 直接写表达式
print(f"{name.upper()} 长度 = {len(name)}")
```

### 调试神器（Python 3.8+）

```python
score = 95
print(f"{score=}")    # score=95  ← 自动带变量名！排查 bug 超好用
```

---

## 5. 类型转换（3 分钟）

```python
# str -> int / float
s = "123"
n = int(s)          # 123
f = float(s)        # 123.0

# int -> str
num = 99
s = str(num)        # "99"

# float -> int（截断，不四舍五入）
print(int(3.9))     # 3
print(int(-3.9))    # -3

# 字符串无法直接转 int 时会抛异常
n = int("hello")    # ValueError: invalid literal for int() with base 10: 'hello'
```

🔥 **务必记住**：用户输入 `input()` 永远返回 **str**，要做数字运算必须先转换：

```python
age = input("请输入年龄：")
print(age + 1)              # ❌ TypeError！str 不能加 int
print(int(age) + 1)         # ✅ 正确
```

---

## 6. 课后练习

> 完成位置：`exercises/lesson02/`
> 参考答案：`solutions/lesson02/`（写完再看！）

详情请阅读 `exercises/lesson02/README.md`。

---

## 7. 本课时小结

- Python 一切皆对象，包括数字和字符串
- 变量是"标签"，可以贴到任何对象上
- 不可变 vs 可变 决定了赋值/修改的行为
- f-string 是首选格式化方式
- 用 `int()` / `str()` / `float()` 显式转换类型
- `input()` 总是返回 str
