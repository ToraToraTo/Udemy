
# CSVファイルの読み込みと書き込みについて


import csv

with open('test.csv', 'w') as csv_file:
    fieldname = ['Name', 'Count']
    # CSVに書き込む為のオブジェクトを作成する。
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()