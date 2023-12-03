# files in aoc/ are 01a.py, find biggest number and prefer b over a, and import that file

import datetime
import importlib
import os


now = datetime.datetime.now()
day = str(now.day)
if len(day) == 1:
    day = "0" + day


files = os.listdir("aoc")
files = [f for f in files if f.endswith(".py")]
files = [f for f in files if f.startswith(day)]

if len(files) == 0:
    print("No files found for day {}".format(day))
    exit()

if len(files) == 1:
    print("Running {}".format(files[0]))
    importlib.import_module("aoc." + files[0][:-3])

if len(files) == 2:
    filename = f"{day}b.py"
    if filename in files:
        print("Running {}".format(filename))
        importlib.import_module("aoc." + filename[:-3])
    else:
        print("Unexpected files found for day {}".format(day))
        exit()