import os
import datetime

FILE_NAME = "kakeibo.csv"
BUDGET_NAME = "budget.txt"


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
    budget = load_budget()
    """一覧表示と合計金額の計算"""
    print(f"\n今月の予算額 {budget}円")
    print("\n--- 収支一覧 ---")
    total = 0
    for i, entry in enumerate(data, 1):
        date, item, amount = entry
        print(f"{i}. {date} | {item} | {amount}円")
        total += int(amount)  # 金額を数値に変換して足す
    print("----------------")
    print(f"合計支出: {total}円")
    print(f"残り予算額: {budget - total}円")
    if budget - total < 0:
        print(f"予算額を超過しています")


def save_budget(budget_amount):
    """今月の予算を保存します"""
    with open(BUDGET_NAME, "w", encoding="utf-8") as f:
        f.write(str(budget_amount))


def load_budget():
    if not os.path.exists(BUDGET_NAME):
        budget_amount = input("今月の予算額を入力してください")
        save_budget(budget_amount)
        print("今月の予算額を保存しました")
    with open(BUDGET_NAME, "r", encoding="utf-8") as f:
        content = f.read().strip()
        return int(content) if content.isdigit() else 0


def main():
    records = load_data()

    while True:
        show_data(records)
        print("1. 支出を追加  2. 支出を削除する 3. 予算額を更新する 4. 終了")
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
        if choice == "2":
            if not records:
                print("削除する支出がありません。")
                continue
            try:
                show_data(records)
                delete_num = int(input("削除したい支出の番号を入力して下さい"))
                removed = records.pop(delete_num - 1)
                save_data(records)  # 変更のたびに保存
                print(f"「{removed}」を削除しました。")
            except (ValueError, IndexError):
                print("正しい番号を入力してください。")
        elif choice == "3":
            try:
                budget_amount = input("更新したい予算額を入力して下さい")
                save_budget(budget_amount)
            except (ValueError, IndexError):
                print("正しい内容を入力してください。")

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
