"""
课时 02 示例 1：Python 5 大基础类型演示
运行：python types_demo.py
"""


def demo_int():
    print("===== 整数 int =====")
    a = 10
    b = -5
    c = 0xFF        # 十六进制
    d = 0b1010      # 二进制
    e = 1_000_000   # 下划线分隔，仅为可读性，不影响数值
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

    # Python 整数无上限
    huge = 2 ** 100
    print(f"2^100 = {huge}")
    print(f"位数：{huge.bit_length()}")


def demo_float():
    print("\n===== 浮点 float =====")
    pi = 3.14159
    g = 9.8
    sci = 1.5e3   # 科学计数法
    print(f"pi={pi}, g={g}, sci={sci}")

    # 浮点精度坑
    print(f"0.1 + 0.2 = {0.1 + 0.2}  (不是 0.3！)")


def demo_bool():
    print("\n===== 布尔 bool =====")
    print(f"True + 1 = {True + 1}")        # 2，bool 是 int 子类
    print(f"False == 0 -> {False == 0}")   # True

    # 真值判断
    print(f"bool(0)     = {bool(0)}")
    print(f"bool('')    = {bool('')}")
    print(f"bool([])    = {bool([])}")
    print(f"bool('hi')  = {bool('hi')}")
    print(f"bool([0])   = {bool([0])}")


def demo_str():
    print("\n===== 字符串 str =====")
    s = "Python"
    print(f"s[0]    = {s[0]}")     # 索引
    print(f"s[-1]   = {s[-1]}")    # 倒数索引
    print(f"s[1:4]  = {s[1:4]}")   # 切片
    print(f"s[::-1] = {s[::-1]}")  # 反转

    # 常用方法
    print(f"upper() = {s.upper()}")
    print(f"lower() = {s.lower()}")
    print(f"len()   = {len(s)}")


def demo_none():
    print("\n===== None =====")
    result = None
    print(f"result = {result}, type = {type(result).__name__}")
    print(f"result is None? {result is None}")


if __name__ == "__main__":
    demo_int()
    demo_float()
    demo_bool()
    demo_str()
    demo_none()
