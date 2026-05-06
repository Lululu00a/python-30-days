"""
课时 01 示例 2：查看 Python 运行环境
运行：python show_env.py
"""

import os
import sys

print(f"Python 版本：{sys.version.split()[0]}")
print(f"完整版本信息：{sys.version}")
print(f"工作目录：{os.getcwd()}")
print(f"解释器路径：{sys.executable}")
print(f"运行平台：{sys.platform}")
