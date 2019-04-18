from warikan import warikan


# 目標: warikanの挙動が正しいかどうかを調べるコードを書く
# 1500円で3人 -> "一人あたり: 500円, 端数: 0円"

# 入力出力のパターン
def check_warikan():
    result = warikan(1500, 3) == "1人あたり: 500円, 端数: 0円"

    if result:
        print("OK")
    else:
        print("NG")


check_warikan()  # あってる とか 間違ってるって出力
