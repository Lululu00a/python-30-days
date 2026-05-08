"""课时 02 示例 3：f-string 全特性"""

name = "Lulu"
age = 30
salary = 12345.678

# 基本插值
print(f"姓名：{name}，年龄：{age}")

# 表达式
print(f"明年 {age + 1} 岁")
print(f"姓名大写：{name.upper()}")

# 数字格式化
print(f"工资：{salary:.2f}")           # 12345.68
print(f"工资带千分位：{salary:,.2f}")  # 12,345.68
print(f"右对齐宽度 12：{salary:>12.2f}")
print(f"左对齐宽度 12：{salary:<12.2f}|")
print(f"补零宽度 10：{age:08d}")       # 00000030

# 百分比
rate = 0.0875
print(f"利率：{rate:.2%}")  # 8.75%

# 进制
n = 255
print(f"十进制 {n}, 十六进制 {n:#x}, 二进制 {n:#b}")

# 调试神器（Python 3.8+）
x = 42
y = [1, 2, 3]
print(f"{x=}")
print(f"{y=}")
print(f"{len(y)=}")
