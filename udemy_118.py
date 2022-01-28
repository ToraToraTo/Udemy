"""
[DEFAULT]
debuk = False

[web_server]
host = 172.0.0.1
port = 80

[db_server]
host = 172.0.0.1
port = 3306

Configファイルを作成して、アプリの設定ファイルとしてConfigファイルを使う。
"""

import configparser

# configファイルの作成
"""
config = configparser.ConfigParser()

config['DEFAULT'] = {
    'debuk': True
}
config['web_server'] = {
    'host': '172.10.0.1',
    'port': '80'
}
config['db_server'] = {
    'host': '172.10.0.1',
    'port': '3306'
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)
"""

# cinfigファイルの読み込み
config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])