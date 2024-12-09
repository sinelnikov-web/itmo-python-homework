import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def timed_execution(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time


def synchronous_execution(n, iterations):
    for _ in range(iterations):
        fibonacci(n)


def threaded_execution(n, iterations):
    threads = []
    for _ in range(iterations):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def process_execution(n, iterations):
    processes = []
    for _ in range(iterations):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


if __name__ == "__main__":
    n = 500000
    iterations = 10

    with open("results.txt", "w") as f:
        sync_time = timed_execution(synchronous_execution, n, iterations)
        f.write(f"Synchronous execution time: {sync_time:.4f} seconds\n")

        thread_time = timed_execution(threaded_execution, n, iterations)
        f.write(f"Thread execution time: {thread_time:.4f} seconds\n")

        process_time = timed_execution(process_execution, n, iterations)
        f.write(f"Process execution time: {process_time:.4f} seconds\n")

    print(f"Results have been written to results.txt")
