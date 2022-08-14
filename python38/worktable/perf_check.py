def perf_check():
    import time
    start = time.time()
    for i in range(100000):
        a = i ** 5
        print(a)
    end = time.time()
    perf_time = end - start
    print(perf_time)

if __name__ == "__main__":
    perf_check()
