"""练习 3 参考答案：日期字符串拆分"""

date_str = input("请输入日期（格式 YYYY-MM-DD）：") or "2026-05-08"

# split 返回 list of str，需要逐个 int() 转换
year, month, day = map(int, date_str.split('-'))

print(f"年份：{year}")
print(f"月份：{month}")
print(f"日期：{day}")
print(f"是 {year} 年的第 {month * 30 + day} 天（粗略估算）")
