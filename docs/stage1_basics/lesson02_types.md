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
| `str` | `char *` / `char[]` | `"hi"`, `'你好'` | **不可变**，Unicode 原生 |
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
int x = 5;   