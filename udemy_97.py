
# CSVファイルの読み込みと書き込みについて


import csv

# CSVファイルの書き込み
with open('test.csv', 'w') as csv_file:
    fieldname = ['Name', 'Count']
    # CSVに書き込む為のオブジェクトを作成する。
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    # カラムの情報を書き込む
    writer.writeheader()

    # カラムに対してデータを書き込む
    writer.writerow({'Name':'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})


# CSVファイルの読み込み
with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])