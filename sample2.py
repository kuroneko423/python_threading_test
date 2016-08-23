# -*- coding: utf-8 -*-
import unittest
import selenium_sample
import threading
# import logging
import time
from datetime import datetime
from logging import getLogger,FileHandler,StreamHandler,DEBUG,INFO,Formatter

# logはlogディレクトリ配下へ格納
log_name = "operation.log"
log_path = "./log/{0}".format(log_name)

# スレッド数
t_number = 2

# スレッドの実行間隔(s)
t_span_time = 2

# ループ回数
roop = 2

# ループ間隔（正確には前回ループ内のスレッドが全て終了してからの間隔）(s)
roop_span_time = 5

# 想定テスト時間(s)
test_time = 40


# ログ設定
formatter = Formatter(fmt='%(asctime)s (%(threadName)-10s) %(message)s',
                          datefmt='%Y/%m/%d %H:%M:%S',)
logger = getLogger(__name__)
_fhandler = FileHandler(log_path,'w')
_shandler = StreamHandler()
_fhandler.setLevel(DEBUG)
_shandler.setLevel(INFO)
logger.setLevel(DEBUG)
_fhandler.formatter = formatter
logger.addHandler(_fhandler)
logger.addHandler(_shandler)

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s (%(threadName)-10s) %(message)s',
#                     filename='operation.log',
#                     datefmt='%Y/%m/%d %H:%M:%S'
#                     )

class MyThread(threading.Thread):

    def run(self):
        # logging.info('Starting...')
        logger.debug('Starting...')
        loader = unittest.TestLoader()
        # テストモジュール単位で追加
        suite = unittest.TestLoader().loadTestsFromModule(selenium_sample)
        # テストスイートを実行
        unittest.TextTestRunner(verbosity=2).run(suite)
        # logging.info('End.')
        logger.debug('End.')
        return

def testSenario():
    logger.debug('Starting...')
    loader = unittest.TestLoader()
    # テストモジュール単位で追加
    suite = unittest.TestLoader().loadTestsFromModule(selenium_sample)
    # テストスイートを実行
    unittest.TextTestRunner(verbosity=2).run(suite)
    # logging.info('End.')
    logger.debug('End.')
    return


# メイン処理
for r in range(roop):
    threads = []
    # logging.info('roop {0} starting...'.format(roop))
    logger.info('roop {0} starting...'.format(r))
    logger.info(datetime.now())
    for i in range(t_number):
        # t = MyThread()
        t = threading.Timer(i,testSenario)
        t.start()
        threads.append(t)
        # if i < (t_number - 1):
        #     time.sleep(t_span_time)

    logger.info(datetime.now())
    for thread in threads:
        thread.join(test_time)

    logger.info(datetime.now())
    if r < (roop-1):
        time.sleep(roop_span_time)
    logger.info(datetime.now())

# logger.debug('main is Ended.')