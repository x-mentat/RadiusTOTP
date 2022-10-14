import datetime
import time
import argparse

import cv as cv
from termcolor import colored
import pyotp as pyotp

arg_parse = argparse.ArgumentParser(description='TOTP token debug')
arg_parse.add_argument('--secret', type=str, help='Token secret', required=True)
arg_parse.add_argument('--interval', type=int, help='Code change interval, default 30', required=False, default=30)
arg_parse.add_argument('--delta', type=int, help='Delta for debug lag/forward, default 0', required=False, default=0)

try:
    args = arg_parse.parse_args()
except:
    arg_parse.print_help()
    exit(0)

totp = pyotp.TOTP(args.secret, interval=args.interval)
print(colored('Press CTRL+C for exit', 'yellow'))
try:
    while True:
        now = datetime.datetime.now()
        code_now = totp.now()
        code_delta = totp.at(now + datetime.timedelta(seconds=args.delta))
        seconds = now.strftime("%S")
        print(colored('#####################################################', 'blue'))
        if code_now == code_delta:
            print_color = 'green'
        else:
            print_color = 'red'
        print(colored('Second # %s' % seconds, 'magenta'))
        print(colored("%s now" % code_now, print_color))
        print(colored("%s -15 sec delta" % code_delta, 'green'))
        print(colored('#####################################################', 'blue'))
        time.sleep(1)
except KeyboardInterrupt:
    pass
