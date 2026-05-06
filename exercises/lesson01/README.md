# 课时 01 课后练习

> 请在本目录下完成以下 3 道练习。完成后再去 `solutions/lesson01/` 对答案。

---

## 练习 1：搭建虚拟环境（动手实操）

1. 在你电脑上**任意位置**新建文件夹 `study_env_test`
2. 在该文件夹中创建虚拟环境 `study_env`
3. 激活它
4. 安装 `requests` 库
5. 运行 `pip list`，把输出保存为本目录下的 `exercise1_piplist.txt`

**提示命令**：
```powershell
mkdir study_env_test
cd study_env_test
python -m venv study_env
.\study_env\Scripts\Activate.ps1
pip install requests
pip list > exercise1_piplist.txt
```

---

## 练习 2：环境信息脚本

在本目录下创建 `exercise2_show_env.py`，要求打印：
- Python 版本号（提示：`sys.version`）
- 当前工作目录（提示：`os.getcwd()`）
- Python 解释器路径（提示：`sys.executable`）

**预期输出示例**：
```
Python 版本：3.11.7
工作目录：D:\Videos\pythonTools\python-30-days\exercises\lesson01
解释器路径：D:\Videos\pythonTools\python-30-days\.venv\Scripts\python.exe
```

---

## 练习 3：思考题（写文档）

在本目录下创建 `exercise3_thinking.md`，用 200 字以内回答：
> 为什么 Python 不需要 `main` 函数也能运行？这种设计的优缺点是什么？

提示思考方向：
- 解释型 vs 编译型
- 脚本式编程的便利
- 大型项目中可能带来的问题
