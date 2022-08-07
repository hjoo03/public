import time

start_time = time.time()
a = list(range(100000))
a2 = map(lambda n: n*2, a)
end_time = time.time()

fin = end_time - start_time
print(fin)

start_time = time.time()
a = list(range(100000))
a2 = []
for i in a:
    a2.append(i*2)
end_time = time.time()

fin = end_time - start_time
print(fin)

start_time = time.time()
temp = [x*2 for x in range(100000)]
end_time = time.time()

fin = end_time - start_time
print(fin)
