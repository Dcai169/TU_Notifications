import time
import datetime
from TU_Notifications import cacher, logger

start_str = "{0}: Program started\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(start_str)
logger.write_log(start_str)

try:
    while True:
        if round(time.time()) % 3600 == 0:
            check_str = "{0}: Checking for updates\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print(check_str)
            logger.write_log(check_str)
            c = cacher.find_new_updates()
            if c is not "":
                update_str = "{0}: Found new update, \"{1}\"\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), c)
                print(update_str)
                logger.write_log(update_str)
        time.sleep(1800)
finally:
    stop_str = "{0}: Program Stopped\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(stop_str)
    logger.write_log(stop_str)