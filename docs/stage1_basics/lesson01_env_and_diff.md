# 课时 01：Python 与 C 的核心差异 + 环境搭建

> 时长：25–30 分钟
> 学完本课你将能：
> 1. 说清 Python 与 C 在执行机制、类型系统、内存管理上的差异
> 2. 在自己机器上装好 Python，跑通第一个程序
> 3. 理解并使用虚拟环境 `venv`
> 4. 用 `pip` 装包

---

## 1. Python vs C：思维上的 4 个关键转变（5 分钟）

| 维度 | C | Python |
|------|---|--------|
| 执行方式 | 编译为机器码后执行 | 解释器逐行解释（实际先编为字节码） |
| 类型系统 | 静态类型（编译期检查） | 动态类型（运行期检查） |
| 内存管理 | 手动 `malloc / free` | 自动垃圾回收（引用计数 + 标记清除） |
| 变量本质 | 一块固定大小的内存 | 指向对象的"标签"（引用） |

🧠 **类比**：
- C 的变量像"贴着标签的盒子"——盒子大小固定，里面装值
- Python 的变量像"贴在物体上的便利贴"——便利贴可以撕下来贴到别的物体上

```c
// C：变量 a 是一块内存，里面装着 10
int a = 10;
a = 20;     // 修改这块内存的值
```

```python
# Python：a 是一个标签，先贴在对象 10 上，再贴到对象 20 上
a = 10
a = 20      # 10 没变，只是 a 现在指向 20
```

---

## 2. 安装 Python（5 分钟）

### Windows
1. 访问 <https://www.python.org/downloads/>
2. 下载 Python **3.11** 或更高版本
3. ⚠️ **务必勾选 "Add Python to PATH"**
4. 打开 PowerShell 验证：
   ```powershell
   python --version
   pip --version
   ```

### macOS / Linux
```bash
# macOS（推荐 Homebrew）
brew install python@3.11

# Ubuntu / Debian
sudo apt update && sudo apt install python3.11 python3.11-venv python3-pip

# 验证
python3 --version
```

### 推荐 IDE
- **VSCode**（轻量、免费）：装 Python 扩展
- **PyCharm Community**（功能完整、免费）

---

## 3. 虚拟环境 venv（10 分钟，重点）

### 为什么需要虚拟环境？

C 项目的依赖通常是头文件 + 静态/动态库，每个项目独立。而 Python 包默认装在**全局**位置：

- 项目 A 需要 `requests==2.20`
- 项目 B 需要 `requests==2.31`
- 全局只能装一个版本 → **冲突**

虚拟环境 = 给每个项目一个**独立的 Python 解释器 + 独立的包目录**。

### 创建与使用

```powershell
# 1. 在项目目录创建虚拟环境（目录名 .venv 是约定）
python -m venv .venv

# 2. 激活
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# macOS / Linux:
source .venv/bin/activate

# 激活后，命令行前会出现 (.venv) 标记

# 3. 安装包（只影响当前虚拟环境）
pip install requests

# 4. 查看已装包
pip list

# 5. 退出虚拟环境
deactivate
```

🔍 **小窍门**：激活后执行 `where python`（Win）/ `which python`（Mac/Linux），会看到路径变成了 `.venv` 里的，说明环境隔离生效。

---

## 4. 第一个 Python 程序（5 分钟）

打开 `lessons/lesson01/hello.py`：

```python
# 这是注释。Python 用 # 而不是 //
print("Hello, Python!")

# Python 不需要 main 函数也能运行
# 但项目代码中常见这种写法（课时 09 详解）：
if __name__ == "__main__":
    name = input("请输入你的名字：")
    print(f"你好，{name}！")
```

运行方式：
```bash
# 方式 1：脚本运行
python lessons/lesson01/hello.py

# 方式 2：交互式 REPL（C 没有这种东西，强烈推荐用来试代码）
python
>>> print("hi")
>>> 1 + 1
>>> exit()
```

---

## 5. 课后练习

> 完成位置：`exercises/lesson01/`
> 参考答案：`solutions/lesson01/`（写完再看！）

详情请阅读 `exercises/lesson01/README.md`。

---

## 6. 本课时小结

- Python 是解释型、动态类型、自动内存管理的语言
- 变量是引用，不是内存盒子
- 每个项目都用独立的 `venv`，避免依赖冲突
- `python -m venv .venv` → 激活 → `pip install` → `deactivate`
