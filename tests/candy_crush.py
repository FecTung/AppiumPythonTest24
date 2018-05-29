# -*- coding:utf-8 -*-
"""
02. Launch Game: Launch a popular App Store game (currently Candy Crush), navigate the menu, then quit.
"""
import os
import sys
import unittest

from time import sleep

sys.path.append("..")
from conf import appium_config
from aptools.apconstants import Commands, C_CandyCrush
from aptools.aputils import logging, PATH


class CandyCrush(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.driver = appium_config.my_webdriver(app=C_CandyCrush.APP, app_path=PATH('../apps/CandyCrushSaga.apk'))

  def test_candy_crush(self):
    prefix = C_CandyCrush.PREFIX
    sleep(30)
    logging.info('{0}: START'.format(prefix))
    login_close_x = C_CandyCrush.LOGIN_CLOSE_X
    login_close_y = C_CandyCrush.LOGIN_CLOSE_Y
    settings_x = C_CandyCrush.SETTINGS_X
    settings_y = C_CandyCrush.SETTINGS_Y
    os.popen('adb shell input tap {0} {1}'.format(login_close_x, login_close_y))
    logging.info('{0}: Close Logging popup.'.format(prefix))
    sleep(3)
    os.popen('adb shell input tap {0} {1}'.format(settings_x, settings_y))
    sleep(3)
    logging.info('{0}: Open settings.'.format(prefix))
    logging.info('{0}: END'.format(prefix))

  @classmethod
  def tearDownClass(self):
    self.driver.quit()
