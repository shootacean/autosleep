import pandas as pd

if __name__ == "__main__":

    # CSVを受け取って各日の起床時間をリスト出力する
    csv = pd.read_csv("data/AutoSleep-20240101-to-20240208.csv")

    # 06:15より早く起きている日をカウントする
    csv["起床時刻"] = csv["起床時間"].str.split(" ").str.get(1)
    judge = csv["起床時刻"] <= "06:15:00"

    # カウント / 月の日数 で達成率を算出する
    print(
        "{} / {} = {}%".format(
            judge.sum(),
            csv["起床時刻"].size,
            (judge.sum() / csv["起床時刻"].size) * 100,
        )
    )
