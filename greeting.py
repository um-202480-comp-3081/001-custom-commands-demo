#!/Users/kbrid/.asdf/shims/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("time")
parser.add_argument("name")
parser.add_argument("-e", "--excited", action="store_true")

args = parser.parse_args()

time = args.time
name = args.name
excited = args.excited
punct = "!"
if excited:
    punct = "!!!!!"

print(f"Good {time}, {name}{punct}")
