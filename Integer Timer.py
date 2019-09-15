import time


t_now = time.time()

i = 0
while i<2147483640:
    i+=1

t_later = time.time()
print( t_later - t_now)