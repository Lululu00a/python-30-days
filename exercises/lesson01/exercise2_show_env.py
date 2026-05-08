import os
import sys
def main() -> None:
    print(f"Python 版本：{sys.version.split()[0]}")
    print(f"工作目录：{os.getcwd()}")
    print(f"解释器路径：{sys.executable}")
if __name__ == "__main__":
    main()  