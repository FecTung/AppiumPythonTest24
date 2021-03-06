# -*- coding:utf-8 -*
import os
import sys
import time

def os_version(device_name):
  """
  Get mobile os Version \n
  By device id
  """
  return os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_name)).read()[0:-1]

def str_sub(content, num):
  ct = content.replace('[', '').replace(']', '')
  return ct.split(':')[num].strip()

def get_devices():
  """
  Get devices id through adb\n
  And return
  """
  # phone_brand = []
  serial_num = []
  # if os.popen("adb get-state").read() != "device":
  #   os.popen("adb kill-server")
  #   os.popen("adb start-server")
  #   time.sleep(2)

  device_list = os.popen("adb devices -l").read()
  if "model" not in device_list:
    print("-> Did not detect any Device.")
    sys.exit()
  else:
    serial_num = [sn.split()[0] for sn in device_list.split('\n') if sn and not sn.startswith('List')]
    # for sn in serial_num:
    #   for mi in os.popen("adb -s {0} shell getprop".format(sn)):
    #     if "ro.build.fingerprint" in mi:
    #       model = str_sub(mi,1).split('/')
    #       phone_brand.append(model[0])
  devices_info = serial_num

  # if len(devices_info) > 1:
  #   print(devices_info)
  #   device_id = input(" \n -> Please input mobile brand to connect:")
  #   return device_id
  # elif len(devices_info) == 1:
  #   return devices_info[0]

  return devices_info