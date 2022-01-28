"""
ロギングについて
"""

import logging

# 出力する範囲のレベルを指定する。
# ファイルにログを保存する場合は、filename=でファイル名を指定して保存する
logging.basicConfig(filename='test.log', level=logging.DEBUG)


logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

