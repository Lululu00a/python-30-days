"""
练习 5 参考答案：BMI 计算器
综合应用：input、类型转换、if-elif、f-string
"""


def evaluate(bmi: float) -> str:
    """根据 BMI 值返回体型评估"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"


def main() -> None:
    # input() 永远返回 str，必须显式转 float
    height = float(input("请输入你的身高（米）："))
    weight = float(input("请输入你的体重（千克）："))

    bmi = weight / (height ** 2)
    advice = evaluate(bmi)

    print(f"你的 BMI 是 {bmi:.1f}，体型评估：{advice}")


if __name__ == "__main__":
    main()
