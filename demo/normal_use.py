
'''常用的'''

from datetime import datetime
print(datetime.now())

#namedtuple
from collections import namedtuple
Point = namedtuple("Point", ['x', 'y'])
p = Point(1,2)
print(p.x)
