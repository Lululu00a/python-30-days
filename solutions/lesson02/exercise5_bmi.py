"""练习 5 参考答案：BMI 计算器"""

height = float(input("请输入身高（米）：") or "1.75")
weight = float(input("请输入体重（千克）：") or "70")

bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "偏瘦"
elif bmi < 24:
    result = "正常"
elif bmi < 28:
    result = "偏胖"
else:
    result = "肥胖"

print(f"你的 BMI 是 {bmi:.2f}，结论：{result}")