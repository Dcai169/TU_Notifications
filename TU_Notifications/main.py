import time
import datetime
from TU_Notifications import cacher

l = open('log.txt', mode='a')
l.write("{0}: Program started\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
try:
    while True:
        if round(time.time()) % 86400 == 0:
            l.write("{0}: Checking for updates\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            c = cacher.find_new_updates()
            if c is not "":
                l.write("{0}: Found new update, \"{1}\"\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),c))
finally:
    l.write("{0}: Program Stopped\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    l.close()