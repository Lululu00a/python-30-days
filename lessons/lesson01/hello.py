"""
课时 01 示例 1：第一个 Python 程序
运行：python hello.py
"""

# 这是注释。Python 用 # 而不是 //
print("Hello, Python!")

# Python 不需要 main 函数也能运行
# 但项目代码中常见这种写法（课时 09 详解）
if __name__ == "__main__":
    name = input("请输入你的名字：")
    print(f"你好，{name}！")
