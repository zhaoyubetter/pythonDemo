import re

str_ = '''PIL                 _xxtestfuzz         heapq               reprlib
__future__          abc                 hmac                requests
_abc                aifc                html                resource'''

# 按空格切割
print(re.split(r'\s+', str_))

import sys
current_module = sys.modules[__name__]