import tkinter as tk
from tkinter import ttk

def calculate_profit():
    try:
        red = int(red_entry.get())
        blue = int(blue_entry.get())
        yellow = int(yellow_entry.get())
        green = int(green_entry.get())
        purple = int(purple_entry.get())
        hammer = int(hammer_entry.get())
        rainbow = int(rainbow_entry.get())
    except ValueError:
        result_box.config(state="normal")
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, "⚠️ 全部の欄に数値を入力してね！")
        result_box.config(state="disabled")
        return

    # 各オーブの単価（99個で購入）
    red_unit = red / 99
    blue_unit = blue / 99
    yellow_unit = yellow / 99
    green_unit = green / 99
    purple_unit = purple / 99

    # 合計コスト（余り分含む）
    total_cost = red + blue + yellow + green + purple + hammer

    # 余りオーブ価値（9個分ずつ）
    leftover_value = (red_unit + blue_unit + yellow_unit + green_unit + purple_unit) * 9

    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, f"=== 合計コスト（余り分考慮後） ===\n{int(total_cost):,} G\n\n")
    result_box.insert(tk.END, f"=== 余りオーブ価値（参考） ===\n{int(leftover_value):,} G\n\n")
    result_box.insert(tk.END, "=== 利益シミュレーション ===\n")

    # 利益計算：A = 大成功（10個）、B = 成功（3個）
    # A + B = 30、A30-B0 から A11-B19 まで
    for A in range(30, 10, -1):
        B = 30 - A
        total_orbs = A * 10 + B * 3
        profit = total_orbs * rainbow - total_cost
        if profit >= 0:
            color = "green"
            sign = "+"
        else:
            color = "red"
            sign = "-"
        result_box.insert(tk.END, f"A{A} B{B}：{sign}{abs(int(profit)):,} G\n", color)

    result_box.tag_config("green", foreground="green")
    result_box.tag_config("red", foreground="red")
    result_box.config(state="disabled")

root = tk.Tk()
root.title("DQX 錬金利益シミュレーター v14")
root.geometry("480x600")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# 入力欄
labels = [
    "レッドオーブ（99個）", "ブルーオーブ（99個）",
    "イエローオーブ（99個）", "グリーンオーブ（99個）",
    "パープルオーブ（99個）", "光の鍛冶ハンマー（1本）",
    "虹色のオーブ（1個売値）"
]

entries = []
for label in labels:
    ttk.Label(frame, text=label).pack()
    entry = ttk.Entry(frame)
    entry.pack()
    entries.append(entry)

red_entry, blue_entry, yellow_entry, green_entry, purple_entry, hammer_entry, rainbow_entry = entries

# 実行ボタン
ttk.Button(frame, text="計算する", command=calculate_profit).pack(pady=10)

# 出力欄
result_box = tk.Text(frame, height=20, wrap="word")
result_box.pack(fill="both", expand=True)
result_box.config(state="disabled")

root.mainloop()
