
import requests

import time
t = 0
for i in range(100):
    n = time.time()
    requests.get("http://yokiy.com")
    t += time.time() - n

print(100 / t)
