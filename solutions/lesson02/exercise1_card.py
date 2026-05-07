"""
练习 1 参考答案：个人名片输出
"""


def main() -> None:
    name = "张三"
    age = 25
    height = 1.785
    is_student = False

    student_str = "是" if is_student else "否"

    print("=" * 30)
    print(f"{'个人名片':^28}")     # ^ 居中
    print("=" * 30)
    print(f"姓名：{name}")
    print(f"年龄：{age} 岁")
    print(f"身高：{height:.2f} 米")
    print(f"学生：{student_str}")
    print("=" * 30)


if __name__ == "__main__":
    main()
