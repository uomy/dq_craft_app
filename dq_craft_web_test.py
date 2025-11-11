import streamlit as st

st.title("DQX 錬金利益シミュレーター v15（Web版）")

# 入力欄
red = st.number_input("レッドオーブ（99個）", min_value=0, step=100)
blue = st.number_input("ブルーオーブ（99個）", min_value=0, step=100)
yellow = st.number_input("イエローオーブ（99個）", min_value=0, step=100)
green = st.number_input("グリーンオーブ（99個）", min_value=0, step=100)
purple = st.number_input("パープルオーブ（99個）", min_value=0, step=100)
hammer = st.number_input("光の鍛冶ハンマー（1本）", min_value=0, step=100)
rainbow = st.number_input("虹色のオーブ（1個売値）", min_value=0, step=100)

if st.button("計算する"):
    # 各オーブの単価（99個で購入）
    red_unit = red / 99
    blue_unit = blue / 99
    yellow_unit = yellow / 99
    green_unit = green / 99
    purple_unit = purple / 99

    # 余りオーブ価値（9個分ずつ）
    leftover_value = (red_unit + blue_unit + yellow_unit + green_unit + purple_unit) * 9

    # 実際に使った材料コスト（余り分を引く）
    total_cost = red + blue + yellow + green + purple + hammer - leftover_value

    st.write(f"### 💰 実際の使用コスト（余り分を除く）：{int(total_cost):,} G")
    st.write(f"### ♻️ 余りオーブ価値（参考）：{int(leftover_value):,} G")

    st.markdown("## 📊 利益シミュレーション")
    results = []
    for A in range(30, 10, -1):  # A30B0 → A11B19
        B = 30 - A
        total_orbs = A * 10 + B * 3
        profit = total_orbs * rainbow - total_cost
        color = "green" if profit >= 0 else "red"
        sign = "+" if profit >= 0 else "-"
        results.append(f"<span style='color:{color}'>A{A} B{B}：{sign}{abs(int(profit)):,} G（{total_orbs}個）</span>")
    st.markdown("<br>".join(results), unsafe_allow_html=True)
