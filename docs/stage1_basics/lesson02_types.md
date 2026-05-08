# 课时 02：基本数据类型与变量

> 时长：25–30 分钟
> 学完本课你将能：
> 1. 掌握 Python 5 大基础类型：`int / float / bool / str / None`
> 2. 理解"变量是标签而非内存盒子"的本质
> 3. 区分 `is` 与 `==` 的差别
> 4. 熟练使用 f-string 格式化字符串
> 5. 掌握类型转换的常用套路

---

## 1. Python 5 大基础类型

| 类型 | C 对应 | 示例 | 备注 |
|------|--------|------|------|
| `int` | `int / long / long long` | `42`, `-7`, `10**100` | **任意精度**，不会溢出 |
| `float` | `double` | `3.14`, `1e-9` | 64 位浮点 |
| `bool` | `_Bool` | `True`, `False` | 是 `int` 的子类！`True == 1` |
| `str` | `char[]` | `"hi"`, `'你好'` | **不可变**，Unicode 原生 |
| `NoneType` | `NULL` 概念 | `None` | 全局唯一对象 |

```python
a = 10**50       # OK，Python int 没有上限
b = True + 1     # 2（bool 是 int 子类）
c = None         # 不是 0，不是 False，是"啥都没有"
print(type(a), type(b), type(c))
```

> 💡 **C 思维要扔掉**：Python 没有 `unsigned`、没有 `short / long`、没有 `char`（字符就是长度为 1 的 str）。

---

## 2. 变量是"标签"，不是"盒子"

C 语言里：
```c
int x = 5;   // 在栈上分配 4 字节，把 5 写进去
x = 6;       // 把那 4 字节内容覆盖成 6
```

Python 里：
```python
x = 5    # 创建对象 5，把标签 x 贴上去
x = 6    # 创建对象 6，把标签 x 撕下来贴到 6 上（5 没人引用就被回收）
```

**核心区别**：
- C 的变量名 = 内存地址，赋值是"写内存"
- Python 的变量名 = 引用（标签），赋值是"换贴对象"

用 `id()` 验证：

```python
x = 5
print(id(x))      # 比如 140234567890
x = 6
print(id(x))      # 不一样了！
```

### 不可变 vs 可变

- **不可变**：`int / float / bool / str / tuple / None`
- **可变**：`list / dict / set`

不可变对象"修改"其实是创建新对象：
```python
s = "hello"
s += " world"   # 实际是创建了新字符串 "hello world"，s 标签换贴
```

---

## 3. `is` vs `==`

| 比较 | 含义 | C 类比 |
|------|------|--------|
| `a == b` | **值**相等 | `strcmp(a, b) == 0` |
| `a is b` | **同一对象**（同一个 id） | `a == b`（指针比较） |

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True，值相等
print(a is b)   # False，不是同一个 list 对象

c = a
print(a is c)   # True，同一个对象
```

### 小整数缓存陷阱

```python
x = 256
y = 256
print(x is y)   # True

x = 257
y = 257
print(x is y)   # False（!!!）
```

CPython 把 `-5 ~ 256` 这些常用小整数预先缓存了，所以同样的值用的是同一个对象。**这是实现细节，不要依赖它！判断值相等永远用 `==`，判断 None 用 `is`：**

```python
if x is None:    # ✅ 推荐
    ...
if x == None:    # ❌ 不规范
    ...
```

---

## 4. f-string 格式化（重点！）

### 基本用法

```python
name = "Lulu"
age = 30
print(f"我叫 {name}，今年 {age} 岁")
```

### 表达式求值

```python
print(f"明年我 {age + 1} 岁")
print(f"姓名大写：{name.upper()}")
```

### 数字格式化

```python
pi = 3.14159265
print(f"{pi:.2f}")        # 3.14（保留 2 位小数）
print(f"{pi:10.2f}")      # 右对齐，宽度 10
print(f"{pi:<10.2f}")     # 左对齐
print(f"{1234567:,}")     # 1,234,567（千分位）
print(f"{0.85:.1%}")      # 85.0%（百分比）
print(f"{255:#x}")        # 0xff（十六进制）
print(f"{8:08b}")         # 00001000（补零二进制）
```

### 调试神器（Python 3.8+）

```python
x = 42
print(f"{x=}")            # x=42（自动带变量名！）
```

---

## 5. 类型转换

```python
int("42")         # 42
int("42", 16)     # 66（按 16 进制解析）
int(3.9)          # 3（截断，不是四舍五入）
float("3.14")     # 3.14
str(42)           # "42"
bool(0)           # False
bool("")          # False
bool([])          # False
bool("False")     # True（!!!非空字符串都是真）
```

### Python 的"假值"

只有这些是 `False`：
```python
False, None, 0, 0.0, "", [], {}, set(), ()
```

其他**都是 True**！这点和 C 不同（C 只看是否为 0）。

---

## 6. 实践对比：同一个任务，C vs Python

**任务**：读两个数，输出它们的和与平均值（保留 2 位小数）。

**C 版本**：
```c
#include <stdio.h>
int main(void) {
    double a, b;
    scanf("%lf %lf", &a, &b);
    printf("sum=%.2f, avg=%.2f\n", a + b, (a + b) / 2);
    return 0;
}
```

**Python 版本**：
```python
a, b = map(float, input("输入两个数（空格分隔）：").split())
print(f"sum={a+b:.2f}, avg={(a+b)/2:.2f}")
```

3 行 vs 7 行，少了类型声明、少了取地址、少了格式串里的 `%`。

---

## 📌 本课要记住的 5 件事

1. ⭐ Python 一切皆对象，**变量是引用（标签）**
2. ⭐ `int` 任意精度、`bool` 是 `int` 子类
3. ⭐ 判断 `None` 用 `is None`，判断值用 `==`
4. ⭐ 不可变对象"修改"实际是创建新对象
5. ⭐ f-string 是格式化首选，`{x=}` 是调试神器

---

## 🎯 下一步

→ 完成 `exercises/lesson02/README.md` 中的练习
→ 做完后看 `solutions/lesson02/` 对照答案

