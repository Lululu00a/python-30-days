"""
练习 3 参考答案：日期字符串拆分
"""


def parse_date(s: str) -> tuple[int, int, int]:
    """把 'YYYY-MM-DD' 形式的字符串拆成 (年, 月, 日) 元组"""
    parts = s.split("-")
    if len(parts) != 3:
        raise ValueError(f"无效日期格式：{s}，期望 YYYY-MM-DD")

    year, month, day = (int(p) for p in parts)
    return year, month, day


def main() -> None:
    samples = ["2024-01-15", "1999-12-31", "2026-06-01"]
    for s in samples:
        y, m, d = parse_date(s)
        print(f"{s} -> {y}年{m}月{d}日")


if __name__ == "__main__":
    main()
