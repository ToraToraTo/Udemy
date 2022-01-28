"""
yamlファイルについて

web_server
  host: 172.0.0.1
  port: 80

db_server
  host: 172.0.0.1
  port: 3306
"""

import yaml

with open('config.yml', 'w') as yaml_fileL:
    yaml.dump({
        'web_server': {
            'host': '172.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '172.0.0.1',
            'port': 3306
        }
    }, yaml_fileL)


# yamlファイルの読み込み
with open('config.yml', 'r') as yaml_fileL:
    data = yaml.safe_load(yaml_fileL)
    print(data, type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])

