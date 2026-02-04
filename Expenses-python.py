import os
import datetime

FILE_NAME = "kakeibo.csv"


def load_data():
    """ファイルを読み込んでリストにする"""
    if not os.path.exists(FILE_NAME):
        return []
    data = []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                # 「日付,項目,金額」をバラバラにしてリストに追加
                data.append(line.split(","))
    return data


def save_data(data):
    """リストの内容をファイルに保存する"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for entry in data:
            # リストをカンマ区切りの文字列にして保存
            f.write(f"{entry[0]},{entry[1]},{entry[2]}\n")


def show_data(data):
    """一覧表示と合計金額の計算"""
    print("\n--- 収支一覧 ---")
    total = 0
    for i, entry in enumerate(data, 1):
        date, item, amount = entry
        print(f"{i}. {date} | {item} | {amount}円")
        total += int(amount)  # 金額を数値に変換して足す
    print("----------------")
    print(f"合計支出: {total}円")


def main():
    records = load_data()

    while True:
        show_data(records)
        print("1. 支出を追加  2. 終了")
        choice = input("操作を選んでください: ")

        if choice == "1":
            item = input("項目（例：昼食）: ")
            amount = input("金額（例：800）: ")

            # 数当てゲームで学んだ入力チェックを応用
            if amount.isdigit():
                date = datetime.date.today().strftime("%Y-%m-%d")
                records.append([date, item, amount])
                save_data(records)
                print("記録しました！")
            else:
                print("エラー：金額は半角数字で入力してください。")

        elif choice == "2":
            break


if __name__ == "__main__":
    main()
