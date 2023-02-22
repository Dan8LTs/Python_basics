# as - псевдоним dt
import datetime as dt, time, sys, os, platform, math
# импорт конкретной функции
from math import sqrt as s
# с сайта pypi.org
# Окружения Python, pip install cowsay
import cowsay

time.sleep(3)
print("Hi!")
print(s(400))
print(dt.datetime.now().time())

print(platform.system())

print(n(12, 42, 56))

print(cowsay.get_output_string('trex', 'Hi!'))