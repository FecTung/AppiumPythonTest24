# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import HTMLTestRunner
import configparser
import traceback
from conf.appium_config import logging
from tests.settings import Settings
from tests.candy_crush import CandyCrush
from tests.map import GoogleMaps
from tests.camera import Camera
from tests.browser import GoogleChrome
from tests.messaging import Messaging
from tests.music_local import GoogleMusic
from tests.music_network import Tune
from tests.video_local import Video
from tests.video_network import Youtube
from tests.dialer import Dialer

def runTest():
  times = 1
  timeout = time.time() + 60*1  # 24h = 60*60*24
  timestr = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))

  filename = "./logs/"+timestr+".html"
  with open(filename , 'wb') as f:
    while True:
      if time.time() > timeout:
        logging.info('TEST OVER')
        break
      else:
        runner = HTMLTestRunner.HTMLTestRunner(
          stream=f,
          title=u'Test Report: {0}'.format(times),
          description=u'Test reports by TG'
        )
        logging.info('Test Times: {0}'.format(times))
        times+=1
        runner.run(suite())

def suite():
  suite = unittest.TestSuite()
  test = [
    # Settings('test_get_memory_status'),
    # Settings('test_bluetooth_disable'),
    # Settings('test_bluetooth_enable'),
    # Settings('test_wlan_disable'),
    # Settings('test_wlan_enable'),
    # CandyCrush('test_candy_crush'),
    # Camera('test_take_picture'),
    # Messaging('test_SMS_MO'),
    # Messaging('test_MMS_MO'),
    # GoogleMaps('test_multi_layers'),
    # GoogleChrome('test_ten_websites'),
    # GoogleMusic('test_music_palyback'),
    Tune('test_music_network'),
    # Video('test_play_video'),
    # Youtube('test_video_network'),
    # Dialer('test_MOViLTE'),
    # Dialer('test_MOVoLTE'),
    # Dialer('test_MTVoLTE'),
    # Dialer('test_Vo2Vi2Vo'),
  ]
  suite.addTests(test)
  return suite

if __name__ == "__main__":
  try:
    runTest()
  except KeyboardInterrupt as ki:
    logging.info('KeyboardInterrupt: {0}'.format(ki))
    logging.debug('KeyboardInterrupt: {0}'.format(traceback.format_exc()))
  except KeyError as ke:
    logging.info('KeyError: {0}'.format(ke))
    logging.debug('KeyError: {0}'.format(traceback.format_exc()))
  except AttributeError as ae:
    logging.info('AttributeError: {0}'.format(ae))
    logging.debug('AttributeError: {0}'.format(traceback.format_exc()))
  except Exception as e:
    logging.info('Exception: {0}'.format(e))
    logging.debug('Exception: {0}'.format(traceback.format_exc()))
  finally:
    print('Please check the Reports.')