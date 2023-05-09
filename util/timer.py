import time


def timer(func):
    start = time.time()
    func()
    print(f"--- {format(time.time() - start, '.2f')} seconds ---")
