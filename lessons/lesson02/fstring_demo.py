"""
课时 02 示例 3：f-string 格式化全攻略
"""

name = "Lulu"
age = 25
pi = 3.14159265

# ----- 基础 -----
print(f"我叫 {name}，今年 {age} 岁")

# ----- 数字格式化 -----
print(f"π ≈ {pi:.2f}")          # 保留 2 位小数
print(f"π ≈ {pi:.4f}")          # 保留 4 位小数
print(f"千分位：{1234567:,}")    # 1,234,567
print(f"百分比：{0.85:.1%}")     # 85.0%
print(f"十六进制：{255:#x}")     # 0xff
print(f"二进制：{10:#b}")        # 0b1010

# ----- 对齐与填充 -----
print(f"|{10:5d}|")     # 默认右对齐
print(f"|{10:<5d}|")    # 左对齐
print(f"|{10:>5d}|")    # 右对齐
print(f"|{10:^5d}|")    # 居中
print(f"|{42:05d}|")    # 0 填充

# ----- 表达式 / 函数调用 -----
x, y = 3, 4
print(f"{x} + {y} = {x + y}")
print(f"{name.upper()} 长度 = {len(name)}")

# ----- 调试神器（Python 3.8+） -----
score = 95
print(f"{score=}")           # score=95，自动带变量名
print(f"{name=}, {age=}")    # 多个变量同时调试
